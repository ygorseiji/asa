def filtraAssentos(assentos, idVoo = False):
    from sistema.models import Voo, Compra

    if idVoo:
        voos = Voo.objects.filter(id=idVoo)
    else:
        voos = Voo.objects.all()
    disponiveis = []

    for v in voos:
        compras = Compra.objects.filter(idVoo=v.id, cancelada=False).order_by('-idVoo__preco')
        if len(compras) > 0:
            compradas = 0
            for c in compras:
                compradas = compradas + c.quantidade
            if v.assentos - compradas >= int(assentos):
                disponiveis.append(v)
        else:
            disponiveis.append(v)
    return disponiveis


def createTicket(idNumb):
    from hashlib import md5
    myHash = md5(str.encode(f"{idNumb}")).hexdigest()
    return myHash


def popularBase():
    from sistema.models import Cidade, Aeroporto, Compra, Conexao, Voo
    from django.contrib.auth.models import User

    users = User.objects.all()
    users.delete()

    User.objects.create_superuser('ygorseiji', 'ygor15hb@gmail.com', 'ygor159951')

    cidades = Cidade.objects.all()
    cidades.delete()
    aeroportos = Aeroporto.objects.all()
    aeroportos.delete()
    compras = Compra.objects.all()
    compras.delete()
    conexoes = Conexao.objects.all()
    conexoes.delete()
    voos = Voo.objects.all()
    voos.delete()

    cidade = Cidade(id=1, nome='São Paulo',uf='SP')
    cidade.save()
    cidade = Cidade(id=2, nome='Rio de Janeiro',uf='RJ')
    cidade.save()
    cidade = Cidade(id=3, nome='Belo Horizonte',uf='MG')
    cidade.save()
    cidade = Cidade(id=4, nome='Porto Velho',uf='RO')
    cidade.save()
    cidade = Cidade(id=5, nome='Manaus',uf='AM')
    cidade.save()
    cidade = Cidade(id=6, nome='Rio Branco',uf='AC')
    cidade.save()
    cidade = Cidade(id=7, nome='Campo Grande',uf='MS')
    cidade.save()
    cidade = Cidade(id=8, nome='Macapá',uf='AP')
    cidade.save()
    cidade = Cidade(id=9, nome='Brasília',uf='DF')
    cidade.save()
    cidade = Cidade(id=10, nome='Boa Vista',uf='RR')
    cidade.save()
    cidade = Cidade(id=11, nome='Cuiabá',uf='MT')
    cidade.save()
    cidade = Cidade(id=12, nome='Palmas',uf='TO')
    cidade.save()
    cidade = Cidade(id=13, nome='Teresina',uf='PI')
    cidade.save()
    cidade = Cidade(id=14, nome='Belém',uf='PA')
    cidade.save()
    cidade = Cidade(id=15, nome='Goiânia',uf='GO')
    cidade.save()
    cidade = Cidade(id=16, nome='Salvador',uf='BA')
    cidade.save()
    cidade = Cidade(id=17, nome='Florianópolis',uf='SC')
    cidade.save()
    cidade = Cidade(id=18, nome='São Luís',uf='MA')
    cidade.save()
    cidade = Cidade(id=19, nome='Maceió',uf='AL')
    cidade.save()
    cidade = Cidade(id=20, nome='Porto Alegre',uf='RS')
    cidade.save()
    cidade = Cidade(id=21, nome='Curitiba',uf='PR')
    cidade.save()
    cidade = Cidade(id=22, nome='Fortaleza',uf='CE')
    cidade.save()
    cidade = Cidade(id=23, nome='Recife',uf='PE')
    cidade.save()
    cidade = Cidade(id=24, nome='João Pessoa',uf='PB')
    cidade.save()
    cidade = Cidade(id=25, nome='Aracaju',uf='SE')
    cidade.save()
    cidade = Cidade(id=26, nome='Natal',uf='RN')
    cidade.save()
    cidade = Cidade(id=27, nome='Vitória',uf='ES')
    cidade.save()

    aeroporto = Aeroporto(id=1, nome='Guarulhos',idCidade_id=1)
    aeroporto.save()
    aeroporto = Aeroporto(id=2, nome='Hercílio Luz',idCidade_id=17)
    aeroporto.save()
    aeroporto = Aeroporto(id=3, nome='Afonso Pena',idCidade_id=21)
    aeroporto.save()
    aeroporto = Aeroporto(id=4, nome='Confins',idCidade_id=3)
    aeroporto.save()
    aeroporto = Aeroporto(id=5, nome='Santos Dumont',idCidade_id=2)
    aeroporto.save()
    aeroporto = Aeroporto(id=6, nome='Salgado Filho',idCidade_id=20)
    aeroporto.save()

    voo = Voo(id=1, assentos=500, preco=1100,idAeroportoDestino_id=2, idAeroportoOrigem_id=3, data='2022-06-30')
    voo.save()
    voo = Voo(id=2, assentos=1200, preco=2700,idAeroportoDestino_id=5, idAeroportoOrigem_id=3, data='2023-04-06')
    voo.save()
    voo = Voo(id=3, assentos=3000, preco=350,idAeroportoDestino_id=5, idAeroportoOrigem_id=1, data='2021-02-08')
    voo.save()
    voo = Voo(id=4, assentos=1000, preco=500,idAeroportoDestino_id=4, idAeroportoOrigem_id=2, data='2025-12-02')
    voo.save()
    voo = Voo(id=5, assentos=800, preco=8000,idAeroportoDestino_id=4, idAeroportoOrigem_id=5, data='2022-09-07')
    voo.save()

    conexao = Conexao(idAeroportoDestino_id=2, idAeroportoOrigem_id=3)
    conexao.save()
    conexao = Conexao(idAeroportoDestino_id=5, idAeroportoOrigem_id=3)
    conexao.save()
    conexao = Conexao(idAeroportoDestino_id=5, idAeroportoOrigem_id=1)
    conexao.save()
    conexao = Conexao(idAeroportoDestino_id=4, idAeroportoOrigem_id=2)
    conexao.save()
    conexao = Conexao(idAeroportoDestino_id=4, idAeroportoOrigem_id=5)
    conexao.save()

    compra = Compra(quantidade=5, cancelada=False, eticket="644d752f2ecdd9f66cca3a7a9aea03ff;", idUsuario_id=1, idVoo_id=1)
    compra.save()
    compra = Compra(quantidade=15, cancelada=False, eticket="241c5d19f8ad5e22b58c3035c1a9951e; 3960a51eb58c9935a9d42b2d50cced87; 8d000ee6e36ef9fcfef3f2bb0c217eb5; ", idUsuario_id=1, idVoo_id=2)
    compra.save()
    compra = Compra(quantidade=1, cancelada=False, eticket="ed60641f532cf884cccc9bcc761b297b; ", idUsuario_id=2, idVoo_id=2)
    compra.save()
    compra = Compra(quantidade=10, cancelada=True, eticket="08a26af057186ba4e1670a99f370327b; ", idUsuario_id=2, idVoo_id=3)
    compra.save()
    compra = Compra(quantidade=4, cancelada=False, eticket="ab47989e220001a14ff889bd15fa5be1; 36588df15e9411613b4d2899aafe86a3; 5aff638143c486b2aafa01f8dc8af021; ", idUsuario_id=1, idVoo_id=5)
    compra.save()

    return 'base inserida com sucesso!'