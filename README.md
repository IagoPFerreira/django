# Django

Esse é um repositório onde estão algumas aplicações criadas durante o meu estudo sobre Django

Cada diretório é um pequeno projeto diferente, cada projeto está armazenado em uma branch diferente

Django é um framework de desenvolvimento web de código aberto, escrito em Python. Ele foi projetado para simplificar o processo de criação de aplicativos web complexos e robustos, permitindo que os desenvolvedores foquem em escrever código de alta qualidade, seguindo as melhores práticas de desenvolvimento.

Se quiser saber com maiores detalhes sobre o Django, acesse a [documentação](https://docs.djangoproject.com/en/4.2/) ou acesse o repositório do [github](https://github.com/django/django/tree/main/django) onde as estruturas e arquivos são bem exploradas e explicadas

O Django possui alguns comandos que facilitam o desenvolvimento, criando arquivos padrões com o mínimo necessário para rodar uma aplicação, alguns desses comandos são:

- `django-admin startproject nome_do_projeto .` - Esse comando cria o arquivo `manage.py` no diretório onde o comando foi rodado e no mesmo nível cria também um diretório com o nome do projeto com os arquivos `__init__.py`, `asgi.py`, `settings.py`, `urls.py` e `wsgi.py`.
- `django-admin startapp nome_do_app` - Esse comando cria um diretório com o nome do app fornecido, dentro dele são criados os arquivos `__init__.py`, `admin.py`, `apps.py`, `models.py`, `tests.py` e `views.py`.
