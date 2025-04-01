# TESTE-DE-API
Este projeto utiliza uma aplicação frontend em **Vue.js** que interage com um backend em **Python** para buscar registros de operadoras de saúde em um arquivo CSV. A API é testada e documentada com **Postman**.

## Tecnologias Utilizadas

- **Vue.js**: Framework JavaScript para criar a interface de usuário (frontend).
- **Python (Flask)**: Linguagem de programação usada para criar a API de backend que processa as buscas.
- **Postman**: Ferramenta para testar e documentar a API.

## Como Executar o Projeto

### 1. Instalar Dependências

Para rodar o projeto, é necessário instalar as dependências tanto do frontend (Vue.js) quanto do backend (Python).

#### Backend (Python)

No diretório `/teste`, instale as dependências para o backend com `pip`. Se você ainda não tiver um ambiente virtual, pode criar um e instalar as dependências:

1. **Criar um ambiente virtual** (preferi utilizar):

   ```bash
   py -m venv venv
   
2. **Ativar o ambiente virtual:**

   ```bash
   venv\Scripts\activate

3. **Instalar as dependências:**

   ```bash
   py -m pip install flask pandas flask-cors

#### Frontend (Vue.js)
No diretório /frontend, instale as dependências do Vue.js com npm:
1. Instalar o Node.js e o npm (caso ainda não tenha instalado);
2. Instalar as dependências:
   Navegue até a pasta do frontend e execute:
   ```bash
   npm install

### 2. Rodar o Backend (Python)
  No diretório /TESTE-DE-API, execute o script Python para que possa rodar a API:
  ```bash
  py server.py
```
A API estará disponível na URL: http://localhost:5000

### 3. Rodar o Frontend (Vue.js)
  No diretório /frontend, execute o servidor de desenvolvimento Vue.js:
  ```bash
  npm run serve
```
A aplicação frontend estará disponível na URL: http://localhost:8080

### 4. Testando a API com Postman
Importar a coleção do Postman: Baixe a coleção Operadoras-API.postman_collection.json (ou crie a sua própria) para testar as rotas da API e usar das requests para testar a API.

## Funcionalidade
A aplicação permite que você busque operadoras de saúde por razão social, registro na ANS ou o seu representante. Os resultados são retornados a partir de um arquivo CSV e são exibidos em cartões arredondados na interface do Vue.js, com as seguintes informações:

Registro ANS
Razão Social
Representante
Data de Registro
