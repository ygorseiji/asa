from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from sistema.models import *
from projetoContainer import utils


def index(request):
    return render(request, 'index.html', {})


def base(request):
    status = utils.popularBase()
    return render(request, 'base.html', {'status': status})


@api_view(['POST'])
def apiLogin(request):
    data = {'status': 'erro', 'session_key' : ''}
    email = request.data['email']
    password = request.data['password']
    username = User.objects.get(email=email).username
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        data['status'] = 'usuario logado'
        data['session_key'] = request.session.session_key
    return JsonResponse(data)


@api_view(['GET'])
def apiLogout(request):
    data = {'status': 'erro'}
    if sessionValida(request):
        logout(request)
        data['status'] = 'usuario deslogado'
    return JsonResponse(data)


def sessionValida(request):
    from datetime import datetime
    from django.contrib.sessions.models import Session
    s = Session.objects.get(session_key=request.session.session_key)
    s.expire_date = s.expire_date.replace(tzinfo=None)
    return datetime.now() < s.expire_date and request.user.is_authenticated


@api_view(['GET'])
def retornaAeroporto(request):
    data = list()
    aeroportos = Aeroporto.objects.all()
    for aero in aeroportos:
        aero_json = {}
        aero_json['id'] = aero.id
        aero_json['nome'] = aero.nome
        aero_json['cidade'] = aero.idCidade.nome
        data.append(aero_json)
    return JsonResponse(data, safe=False)


@api_view(['GET'])
def retornaAeroportoPorOrigem(request):
    data = list()
    origem = request.GET['aeroporto']
    conexoes = Conexao.objects.filter(idAeroportoOrigem__nome=origem)
    for conex in conexoes:
        conex_json = {}
        conex_json['id'] = conex.idAeroportoDestino.id
        conex_json['nome'] = conex.idAeroportoDestino.nome
        conex_json['cidade'] = conex.idAeroportoDestino.idCidade.nome
        data.append(conex_json)
    return JsonResponse(data, safe=False)


@api_view(['GET'])
def retornaVoo(request):
    data = list()
    dia = request.GET['dia']
    voos = Voo.objects.filter(data=dia)
    for voo in voos:
        voo_json = {}
        voo_json['id'] = voo.id
        voo_json['assentos'] = voo.assentos
        voo_json['preco'] = voo.preco
        voo_json['origem_aeroporto'] = voo.idAeroportoOrigem.nome
        voo_json['origem_cidade'] = voo.idAeroportoOrigem.idCidade.nome
        voo_json['destino_aeroporto'] = voo.idAeroportoDestino.nome
        voo_json['destino_cidade'] = voo.idAeroportoDestino.idCidade.nome
        data.append(voo_json)
    return JsonResponse(data, safe=False)


@api_view(['GET'])
def pesquisaVoo(request):
    data = list()
    assentos = request.GET['assentos']
    voos = utils.filtraAssentos(assentos)
    for voo in voos:
        voo_json = {}
        voo_json['id'] = voo.id
        voo_json['assentos'] = voo.assentos
        voo_json['preco'] = voo.preco
        voo_json['origem_aeroporto'] = voo.idAeroportoOrigem.nome
        voo_json['origem_cidade'] = voo.idAeroportoOrigem.idCidade.nome
        voo_json['destino_aeroporto'] = voo.idAeroportoDestino.nome
        voo_json['destino_cidade'] = voo.idAeroportoDestino.idCidade.nome
        data.append(voo_json)
    return JsonResponse(data, safe=False)


@api_view(['GET'])
def efetuaCompra(request):
    data = list()
    assentos = request.GET['assentos']
    idVoo = request.GET['idVoo']
    voos = utils.filtraAssentos(assentos, idVoo)
    idUsuario = request.user.id
    if idUsuario is None:
        data.append({'status':'erro', 'motivo':'usuario deslogado'})
        return JsonResponse(data, safe=False)
    if len(voos) == 0: #nao disponivel
        data.append({'status':'erro', 'motivo':'quantidade desejada nao disponivel no voo desejado'})
    else: #disponivel
        from datetime import datetime
        etickets = ''
        for i in range(int(assentos)):
            etickets = etickets + utils.createTicket(str(idUsuario) + str(i) + str(datetime.now())) + '; '
        compra = Compra(quantidade = int(assentos), cancelada = False, eticket = etickets, idUsuario_id=idUsuario, idVoo_id=int(idVoo))
        compra.save()
        compra_json = {}
        compra_json['status'] = 'assentos reservados e compra efetuada com sucesso'
        compra_json['localizador'] = compra.id
        compra_json['etickets'] = etickets
        data.append(compra_json)
    return JsonResponse(data, safe=False)