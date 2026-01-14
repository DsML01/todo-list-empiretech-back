# Todo List API (EmpireTech)

API RESTful para gerenciamento de tarefas, desenvolvida com Flask

## 🛠️ Tecnologias utilizadas

* **Linguagem:** Python 3.13
* **Framework:** Flask (Application Factory & Blueprints)
* **Persistência:** SQLAlchemy (SQLite)
* **Validação:** Pydantic v2 (Schemas de entrada/saída)
* **QA:** Ruff (Lint/Format) & Pytest (Testes unitários/integração)
* **Tooling:** Poetry (Dependências) & Taskipy (Automação)

## 🏗️ Estrutura do Projeto

* `models.py`: Modelagem de dados SQLAlchemy.
* `schemas.py`: Contratos Pydantic com regras de validação (ex: `min_length=10` para títulos).
* `routes.py`: Endpoints REST e lógica de aplicação.
* `settings.py`: Configurações via `pydantic-settings` (.env).
* `run.py`: Ponto de entrada do servidor.

## 🚀 Execução

1. **Instalação:**
```bash
poetry install

```

2. **Ambiente:**
Configure o `.env` seguindo o `.env.example`.

3. **Comandos rápidos (Taskipy):**
* Iniciar API: `task run`
* Rodar Testes: `task test`
* Formatar código: `task format`


## 🔌 API Reference

| Método | Endpoint | Validação | Status Sucesso |
| --- | --- | --- | --- |
| **GET** | `/api/tasks` | `TaskRead` | 200 OK |
| **POST** | `/api/tasks` | `TaskCreate` | 201 Created |
| **PATCH** | `/api/tasks/<id>` | `TaskUpdate` | 200 OK |
| **DELETE** | `/api/tasks/<id>` | - | 204 No Content |

## 🧪 Qualidade e Cobertura

O projeto utiliza **Pytest** com banco de dados SQLite em memória (`:memory:`) para isolamento dos testes.

* **Cobertura de Código:** 97% (Relatório disponível via `task coverage`).
* **Padrão de Código:** PEP 8 estrito (79 caracteres) via Ruff.