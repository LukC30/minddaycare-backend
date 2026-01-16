# Mind Daycare - Backend

Este é o backend para o projeto Mind Daycare, desenvolvido com FastAPI.

## 🚀 Como Executar

1.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Execute a aplicação:**
    Use o Uvicorn para iniciar o servidor.
    ```bash
    uvicorn app.main:app --reload
    ```
    A API estará disponível em `http://127.0.0.1:8000`.

## 📚 API Endpoints

A seguir estão os endpoints disponíveis na API.

| Método | Rota                  | Descrição                               |
|--------|-----------------------|-------------------------------------------|
| GET    | `/v1/user/test`       | Rota de teste para verificar se a API está no ar. |
| POST   | `/v1/user/`           | Cria um novo usuário.                     |
| GET    | `/v1/user/all-users`  | Retorna uma lista com todos os usuários.  |
| GET    | `/v1/user/{id}`       | Busca e retorna um usuário pelo seu `id`.   |
| PUT    | `/v1/user/`           | Atualiza as informações de um usuário.    |
| DELETE | `/v1/user/`           | Deleta um usuário.                        |

## ⚙️ Tecnologias

- Python 3
- FastAPI
- Uvicorn