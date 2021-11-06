FROM python
# RUN apt-get update && apt-get install net-tools && apt-get install curl
COPY . projeto
WORKDIR projeto
RUN pip install -r ./support/requirements.txt
RUN chown root wait-for-it.sh
RUN chmod 4755 wait-for-it.sh
#CMD ["./wait-for-it.sh", "172.17.0.6:5432", "--", "python", "load.py"]
CMD ["python", "load.py"]
# CMD ["python","manage.py","makemigrations"]
# CMD ["python","manage.py","migrate"]
# CMD ["python","manage.py","runserver", "172.30.0.5:5000"]