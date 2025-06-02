# Avaliação Técnica – Automação de Testes
Este projeto contém testes automatizados para o frontend e a API do Serverest, utilizando Python e Selenium (para E2E) e a biblioteca `requests` (para API).

## Objetivo

Avaliar habilidades em automação de testes aplicando boas práticas de desenvolvimento, organização e escrita de testes automatizados, garantindo a qualidade de fluxos essenciais da aplicação Serverest.

* **Frameworks/Bibliotecas:**
    * Selenium WebDriver (para automação de UI)
    * `requests` (para testes de API)
    * `pytest` (para execução e estruturação dos testes)
    * `webdriver-manager` (para gerenciamento automático de drivers de navegador)
* **Organização do Projeto:** Padrões de projeto (ex: Page Object Model), separação de responsabilidades.

## Cenários Automatizados

### Frontend (E2E) - `https://front.serverest.dev/`

Os testes de frontend simulam fluxos reais de usuário, como:

* **Fluxo de Cadastro e Login:**
    * Cadastro de um novo usuário com dados dinâmicos.
    * Login bem-sucedido com o usuário recém-cadastrado.
* **Login com Credenciais Inválidas:**
    * Tentativa de login com email e/ou senha incorretos.
    * Verificação da mensagem de erro esperada.
* **Fluxo de Adição de Produto ao Carrinho:**
    * Login de um usuário existente
    * Obtenção dinâmica do nome de um produto na página Home.
    * Adição do produto à "Lista de Compras" na página Home.
    * Navegação para a página "Minha Lista de Compras".
    * Adição do produto da "Lista de Compras" para o "Carrinho" real.(em contrução)

### Pré-requisitos

* Python 3.x instalado.
* Navegador Google Chrome (e uma conexão com a internet para o `webdriver-manager` baixar o driver).

### Passos para Instalação

1.  **Clone o Repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO_AQUI>
    cd serverest_automation
    ```
2.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    * O `webdriver-manager` irá baixar e gerenciar automaticamente o driver do Chrome.

### Execução dos Testes
* **Executar todos os testes:**
    ```bash
    pytest
    ```
* **Executar apenas testes de frontend:**
    ```bash
    pytest tests/frontend/
    ```
* **Executar apenas testes de API:**
    ```bash
    pytest tests/api/
    ```
* **Executar um arquivo de teste específico:**
    ```bash
    pytest tests/frontend/test_add_produto_frontend.py
    ```
## Boas Práticas Adotadas

* **Page Object Model (POM):** Usado para testes de UI, separando elementos e interações da lógica de teste.
* **Separação de Responsabilidades:** Lógica de API em clientes dedicados (`api_clients`), geração de dados em `utils/data_generator.py`, e utilitários diversos em `utils/`.
* **Fixtures Pytest:** Utilizadas extensivamente em `conftest.py` para setup e teardown de recursos (WebDriver, clientes de API, dados de teste), promovendo reusabilidade e limpeza do ambiente.