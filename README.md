# ASA_projetoContainer
Repositório para o projeto Container de ASA.

> Usabilidade:<br>
Para inicializar o django app e o postgre app basta rodar o comando:<br> 
```shell
docker-compose up
```

A comunicação entre os containeres é dada por meio da subrede ```172.30.0.0/24``` (django-asa-network). O django app utiliza o ip ```172.30.0.5``` e possui a porta 5000 exposta enquanto o postgres db utiliza o ip ```172.30.0.6``` com a porta 5432 exposta.
