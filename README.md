# My-mangas 🥭

Este é o projeto de front-end com python que serve os dados coletados do banco para o front-end, utilizando as linguagens **TypeScript** e **Python**.

## 📂 Estrutura do Projeto

Este repositório contém o código-fonte da api da aplicação. Para visualizar o projeto completo, incluindo front-end e API, veja as outras partes do sistema:

- [**Front-end**](https://github.com/GustavoSilverio/my-mangas-front): Uma aplicação com uma interface simples que mostra o catálogo de mangás disponiveis na plataforma.
- [**Automação/Web-Scraper**](https://github.com/GustavoSilverio/my-mangas-scraper): Um script em Python que coleta dados de mangás de uma plataforma online. Utiliza bibliotecas nativas de Python e multi-threading para maximizar a eficiência.

## ⚖️ Aviso Legal

Este projeto é apenas um exemplo técnico e **não deve ser usado para distribuir conteúdo protegido por direitos autorais** sem a devida autorização dos proprietários dos direitos. Nenhum conteúdo de mangás é incluído neste repositório.

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE). Sinta-se à vontade para utilizar o código como base para seus próprios projetos, respeitando os termos da licença.

## 🛠️ Como Rodar o Projeto (Obrigatório python instalado na maquina)

1. Clone o repositório:
   ```bash
   git clone https://github.com/GustavoSilverio/my-mangas-api.git
    ```
2. Crie um ambiente virtual:
    ```bash
    python -m venv .venv
    ```
3. Ative o ambiente virtual
    ```bash
    .venv\scripts\activate
    ```
4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
5. Crie um arquivo .env na raiz do projeto e as seguintes variáveis:
    ```env
    # connection string para o mongo
    MONGO_BASE_URL='mongodb+srv://USER:SENHA@********.mongodb.net/'

    # adicione a origem de onde vai receber as requisições, normalmente em http://localhost:3000 (onde o front está rodando)
    ORIGIN='http://localhost:3000'

    # essa seria a chave de acesso para a api, coloque o valor que desejar, essa key vai ser pedida no front para poder logar
    ACCESS_KEY='mX8JbZ7c4vNp2Qw5LdRt6Fy9KsGhVqP3jCnTkYzB'

    # esse secret seria uma chave especial para criar os tokens, pode adicionar o valor que desejar
    TOKEN_SECRET='B9wR2vG6pMdJ4kVfHn7sTqXzL8CrYm3xQa5NtKjP'
    ```
6. Rode o projeto:
    ```bash
    python main.py
    ```
