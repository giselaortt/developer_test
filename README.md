# Take5 - Contratação Desenvolvedor Back-end
Olá, este é o teste para contratação de um desenvolvedor Back-end

Para a realização deste teste você precisará ter conhecimentos dos seguintes items:

1. Git
2. Django
3. Django Rest Framework
4. PL-SQL (MySQL, MSSQL)

É importante que você sinalize no documento anexo a este projeto caso não tenha domínio em algum dos itens descritos acima.
Caso tenha alguma dúvida fique a vontade para pesquisar na internet sobre.


# Teste

## Parte 1 (3 partes) - _Git, Todo mundo junto_
_Esta etapa irá nos apresentar os seus conhecimentos de Git._
* Dê um fork deste projeto

* Crie uma branch dentro do seu fork com o seu email como nome. 
```
git branch ms.giselaortt@gmail.com
git checkout ms.giselaortt@gmail.com
```

* Para os próximos passos, gostaríamos que você efetuasse os pushs conforme sua evolução.

Utilize commits que pontuem o está sendo carregado para o repositório, pois depois de você outras pessoas poderão utilizar o mesmo repositório/branch para dar continuidade ao seu trabalho.


## Parte 2 (3 Partes) - _Welcome to the Django_
_Esta etapa irá mostrar os seus conhecimentos de Django._
* Dentro do diretório deste projeto, inicialize um projeto Django, com o nome de "take5"
```
django-admin startproject take5 
```

* Rode as migrações do seu projeto para inicializar as tabelas do django
```
python3 manage.py makemigrations
python3 manage.py migrate
```

* Inicie o servidor e verifique se sua aplicação está funcionando
```
python3 manage.py runserver
```

* Dentro do projeto, inicialize uma aplicação chamada "survey"

rodar o seguinte comando dentro do diretorio take5:
```
python3 manage.py startapp survey
```

* Inclua survey no projeto take5
> write app name to settings.py on INSTALLED_APPS

* Crie modelos para sua aplicação: 
  - Survey (Pesquisa)
  - SurveyQuestion (Perguntas da pesquisa)
  - SurveyQuestionAlternative (Alternativas para as perguntas da pesquisa)
  - SurveyUserAnswer (Respostas dos usuários para a Pesquisa)
* Gere a migração do Banco de Dados para que suas tabela sejam criadas
* Cadastre uma pesquisa utilizando uma das formas abaixo descritas

Opções para cadastrar a pesquisa:
1. Criar uma pesquisa utilizando o Painel do Django
2. Criar uma pesquisa utilizando o Shell (_Caso opte por esta opção é necessário inserir os comandos utilizados no arquivo shell.py localizado neste projeto_)

para abrir a shell do django:
```
python manage.py shell
```

exemplo  de como inserir uma entrada no banco:
```
from mysite.blog.models import Blog
b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
b.save()
```

retirado (daqui)[https://django-portuguese.readthedocs.io/en/1.0/topics/db/queries.html].
Ou apos instanciar a classe: 

```
b.name = 'Beatles Blog'
```

## Parte 3 (3 Partes) - _Show me the money_
_Esta etapa irá mostrar os seus conhecimentos de Django Rest Framework._
* Instale o Django Rest Framework no projeto, utilizando o PIP e incluindo ele no seu settings.py
``` pip install djangorestframework ```
then insert 'rest_framework' on installed apps.

* Crie uma view para apresentar suas pesquisas, associando ela a uma URL do seu projeto


* Crie um serializer para pegar Survey, SurveyQuestion e SurveyQuestionAlternative. Tente utilizar o prefetch_related nas queries para diminuir a quantidade de queryes necessárias para a apresentação dos dados


* Acesse a página da sua pesquisa e copie o JSON de resultado para o arquivo result.json situado no diretório raiz deste projeto

# Boa Sorte

Qualquer dúvida entrar em contato com Alexandre Sanches (alexandre@take5.com.br)


> How to local deploy :

Command to know my ip address:``` hostname -I ```

add  ``` ALLOWED_HOSTS =[ 'localhost','my_ip_here' ] ``` on ``` settings.py ``` 

add the paths to the urls.py file, linking each path to a view.

deploy locally with

``` python manage.py runserver localhost:8080 ``` and access ``` localhost:8080 ``` from the browser.


