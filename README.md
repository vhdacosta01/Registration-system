# Registration System

Sistema de cadastro e login desenvolvido como projeto de estudo para praticar desenvolvimento Backend com Python e Flask.

O projeto permite criar contas, armazenar usuários em um banco de dados SQLite, realizar login com senha protegida por hash e controlar sessões de usuários autenticados.

## Como executar o projeto
- 1º passo: clone o repositório 
git clone https://github.com/SEU-USUARIO/Registration-system.git

- 2º passo: acesse a pasta do projeto
cd Registration-system

- 3º passo: crie um ambiente virtual
python -m venv .venv

- 4º passo: ative o ambiente virtual criado 
.venv\Scripts\activate

- 5º passo: pip install -r requirements.txt
instale as dependências necessárias

- 6º passo: execute o servidor Flask e acesse o endereço
python run.py

## Tecnologias utilizadas

### Front-end
- HTML
- CSS

### Back-end
- Python
- Flask
- SQLite
- Werkzeug
- Javascript

## Funcionalidades

- Cadastro de usuários
- Armazenamento de usuários no SQLite
- Hash de senhas
- Login de usuários
- Verificação de senha
- Sessão de usuário
- Proteção da página Dashboard
- Logout

## Estrutura do projeto

Registration-system/
│
├── app/
│   ├── config/
│   │   └── database.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   └── router.py
│   │
│   ├── static/
│   │   └── css
│   │        └── style.css
│   │   └── js
│   │        └── form-validation.js
│   │
│   ├── templates/
│   │   ├── login.html
│   │   ├── register.html
│   │   └── dashboard.html
│   │
│   └── __init__.py
│
├── run.py
├── requirements.txt
├── .gitignore
└── README.md


