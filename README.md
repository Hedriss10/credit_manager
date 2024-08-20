# Credit Manager - Banco Master

**Credit Manager** é uma aplicação web desenvolvida para o setor financeiro de crédito do **Banco Master**. A aplicação visa modernizar e automatizar o processo de análise e aprovação de crédito, proporcionando uma interface amigável e eficiente para os analistas de crédito.

## Tecnologias Utilizadas

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS (Bootstrap), JavaScript
- **Banco de Dados:** SQLite (pode ser facilmente substituído por outro SGBD)
- **Migrações de Banco de Dados:** Flask-Migrate
- **Formulários:** Flask-WTF

## Funcionalidades

- **Adicionar Solicitações de Crédito:** Permite que analistas de crédito insiram novas solicitações de crédito, especificando o nome do cliente e o valor solicitado.
- **Visualizar Solicitações de Crédito:** Mostra uma tabela com todas as solicitações de crédito, incluindo ID, nome do cliente, valor solicitado, status, e data de criação.
- **Persistência dos Dados:** Utiliza SQLite como banco de dados padrão, com suporte para migrações de esquema através do Flask-Migrate.
- **Design Responsivo:** Interface amigável e responsiva, construída com Bootstrap e customizada com CSS.

## Estrutura do Projeto

```plaintext
credit_manager/
│
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       └── scripts.js
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   └── credit.html
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── forms.py
│
├── migrations/
│
├── .env
├── config.py
├── requirements.txt
└── run.py
```

### Descrição dos Arquivos

- **`app/__init__.py`**: Configuração inicial da aplicação Flask e integração com o banco de dados.
- **`app/models.py`**: Definição das entidades do banco de dados, neste caso, o modelo `Credit`.
- **`app/routes.py`**: Define as rotas da aplicação, lidando com a navegação e funcionalidades principais.
- **`app/forms.py`**: Define os formulários utilizando Flask-WTF para entrada de dados dos usuários.
- **`app/templates/`**: Contém os templates HTML que compõem a interface da aplicação.
  - **`base.html`**: Template base que é estendido por outros templates.
  - **`index.html`**: Página principal que lista todas as solicitações de crédito.
  - **`credit.html`**: Página para adicionar uma nova solicitação de crédito.
- **`app/static/css/styles.css`**: Arquivo de estilo customizado para a aplicação.
- **`app/static/js/scripts.js`**: Arquivo JavaScript para funcionalidades de frontend.
- **`config.py`**: Configurações gerais da aplicação, como chave secreta e URI do banco de dados.
- **`.env`**: Arquivo de ambiente para configurações sensíveis, como `SECRET_KEY` e `DATABASE_URL`.
- **`requirements.txt`**: Lista de dependências Python necessárias para rodar a aplicação.
- **`run.py`**: Script principal para rodar a aplicação Flask.

## Instalação

### 1. Pré-requisitos

- **Python 3.7+**
- **Pip** (gerenciador de pacotes do Python)

### 2. Clonando o Repositório

```bash
git clone https://github.com/seu_usuario/credit_manager.git
cd credit_manager
```

### 3. Configuração do Ambiente Virtual

Recomenda-se o uso de um ambiente virtual para isolar as dependências do projeto.

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### 4. Instalando Dependências

```bash
pip install -r requirements.txt
```

### 5. Configurando as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```plaintext
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///db.sqlite3
```

### 6. Inicializando o Banco de Dados

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

### 7. Executando a Aplicação

```bash
python run.py
```

A aplicação estará disponível em `http://127.0.0.1:5000/`.

## Utilização

### Adicionar uma Solicitação de Crédito

1. Navegue até a página "Add Credit" usando a barra de navegação.
2. Preencha o nome do cliente e o valor do crédito.
3. Clique em "Submit" para adicionar a solicitação.

### Visualizar Solicitações de Crédito

- A página inicial lista todas as solicitações de crédito, onde você pode visualizar detalhes como o nome do cliente, valor do crédito, status e data de criação.

## Padrões de Projeto e Design System

- **Padrão MVC (Model-View-Controller):** O projeto utiliza o padrão MVC para separar a lógica de negócios, a camada de apresentação e a lógica de controle, facilitando a manutenção e a escalabilidade.
- **Design System:** A aplicação utiliza Bootstrap para garantir uma interface consistente e responsiva. CSS customizado foi adicionado para adaptar o design ao branding do Banco Master.
- **Arquitetura Modular:** A estrutura do projeto é modular, permitindo fácil extensão e adição de novas funcionalidades.

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Se você encontrar bugs ou quiser sugerir melhorias, abra uma issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Desenvolvido com ♥ por Hedris Pereira para o setor financeiro de crédito do Banco Master.

---

Esse README fornece uma explicação clara e detalhada sobre como configurar e utilizar a aplicação, além de destacar as boas práticas e padrões adotados. Se precisar de mais alguma coisa, estou aqui para ajudar!