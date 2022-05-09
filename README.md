#  CRUD (Create, Retrieve, Update e Delete)

- _Create_: Criar ou adicionar novos regsitros em uma tabela de banco de dados.
- _Retrieve_: Ler, recuperar ou buscar todos ou algunss resgistros da tabela de um banco de dados.
- _Update_: Atualizar ou corrijir os registros existentes em uma tabela de banco de dados.  
- _Delete_: Excluir os registros existentes em uma tabela de banco de dados.



## COMANDOS

### Iniciar um novo projeto

```
django-admin startproject AGContatos
```

### Criar aplicativo dentro do projeto

```
python manage.py startapp Contatos
```

### Executar servidor

```
python .\manage.py runserver
```

### Instalar plugin/módulo do MySQL

```
pip install mysqlclient
```

### Colocar os arquivos na pasta migrations

```
python .\manage.py makemigrations
```

### Gerar a tabela no banco de dados

```
python .\manage.py migrate
```

### Criar o usuário da área administrativa

```
python .\manage.py createsuperuser
```

### Instalar a biblioteca Crispy Forms

```
pip install django-crispy-forms
```

