
# 🚗 **Sistema de Venda de Carros — Django**

Aplicação web desenvolvida com Django para gerenciamento e venda de veículos. O sistema permite cadastrar, visualizar, editar e excluir carros, além de manter um controle automático de estoque e valor total dos veículos disponíveis.

## 📌 Sobre o projeto

Este projeto simula um sistema utilizado por lojas de veículos para gerenciar seu estoque de carros. O foco principal está no desenvolvimento do backend com Django, utilizando templates HTML simples para o frontend.

A aplicação implementa operações completas de CRUD e utiliza recursos do Django como ORM, Class-Based Views e signals para automação de processos.

    ⚙️ Funcionalidades
    🚘 Cadastro de veículos
    📋 Listagem de carros disponíveis
    🔍 Busca por modelo
    ✏️ Edição de informações
    ❌ Exclusão de veículos

## 📊 Controle automático de estoque:

* Quantidade total de carros
* Valor total do inventário

🖥️ ***Interface simples com templates HTML***

## 🛠️ Tecnologias utilizadas

* Python 3
* Django
* SQLite3
* HTML5
* CSS3

## 🗂️ Estrutura do projeto

    carros/
    │
    ├── app/
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    │
    ├── cars/
    │   ├── models.py
    │   ├── views.py
    │   ├── signals.py
    │   ├── forms.py
    │   ├── templates/
    │   └── ...
    │
    ├── db.sqlite3
    └── manage.py

## 🚀 Como executar o projeto


#### Clone o repositório
git clone 

#### Entre na pasta
cd carros

#### Crie o ambiente virtual
python -m venv venv

#### Ative o ambiente
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

#### Instale as dependências
pip install -r requirements.txt

### ***requirements***
annotated-types==0.7.0
anyio==4.13.0
asgiref==3.11.1
certifi==2026.2.25
colorama==0.4.6
distro==1.9.0
Django==6.0.4
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
idna==3.11
jiter==0.14.0
openai==2.32.0
pillow==12.2.0
pydantic==2.13.3
pydantic_core==2.46.3
sniffio==1.3.1
sqlparse==0.5.5
tqdm==4.67.3
typing-inspection==0.4.2
typing_extensions==4.15.0
tzdata==2026.1

#### Execute as migrações
python manage.py migrate

#### Rode o servidor
python manage.py runserver

🌐 **Acesso**

    http://127.0.0.1:8000/

📊 **Diferenciais do projeto**

* Uso de signals (post_save e post_delete) para atualização automática do inventário
* Aplicação de boas práticas com Django ORM
* Estrutura organizada e escalável

# 👨‍💻 Autor

# **Leonardo Sales**
