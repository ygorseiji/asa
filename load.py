# Usado para fazer a inicialização do servidor
import os
os.system("python manage.py makemigrations")
os.system("python manage.py migrate")
os.system("python manage.py runserver 5000")