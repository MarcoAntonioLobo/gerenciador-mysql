# gerenciador-mysql

Este projeto é uma aplicação web simples para gerenciar bancos de dados MySQL rodando em containers Docker.  
Com ele, você pode criar, listar e remover bancos MySQL facilmente usando uma interface web acessível no navegador local pela porta 8080.

---

## Para que serve

- Facilita a criação rápida de containers MySQL com banco, usuário e senhas configuráveis  
- Permite listar todos os bancos MySQL em execução via Docker  
- Permite remover containers de bancos MySQL que não são mais necessários  
- Tudo controlado por uma interface web simples e amigável, sem usar terminal

---

## Tecnologias utilizadas

- Python 3  
- Flask (framework web)  
- Docker SDK para Python  
- HTML para interface simples

---

## Como usar

### Pré-requisitos

- Docker instalado e rodando  
- Python 3 instalado  
- Bibliotecas Python instaladas (use `requirements.txt` ou instale manualmente)

### Instalação

1. Clone o repositório:

   git clone https://github.com/MarcoAntonioLobo/gerenciador-mysql.git  
   cd gerenciador-mysql

2. Crie e ative ambiente virtual (opcional):

   python3 -m venv venv  
   source venv/bin/activate  # Linux/Mac  
   venv\Scripts\activate     # Windows

3. Instale as dependências:

   pip install flask docker

### Rodando a aplicação

   python app.py

Acesse http://localhost:8080 no navegador.

---

## Estrutura do projeto

- `app.py`: código principal da aplicação e gerenciamento Docker  
- `templates/`: arquivos HTML (`index.html`, `criar.html`)

---

## Observações

- A aplicação gerencia containers MySQL via Docker local  
- Senhas configuráveis via formulário; se vazio, senha root é gerada automaticamente  
- Permissões Docker necessárias para o usuário rodar a aplicação

---

## Possíveis melhorias

- Autenticação para a interface web  
- Edição de bancos já criados  
- Exibição de logs e status dos containers  
- Suporte para outros bancos (PostgreSQL, MariaDB, etc)

---

## Licença

MIT License

---

## Autor

Marco Lobo — marcoantoniolobo82@gmail.com