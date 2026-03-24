# 🐍 Webhook Manager API

Uma API robusta desenvolvida para atuar como um middleware de recebimento e processamento de dados via Webhooks.

### 🚀 Tecnologias e Conceitos Aplicados:
- **FastAPI:** Framework moderno de alta performance para Python.
- **Pydantic:** Validação rigorosa de esquemas de dados (JSON).
- **Segurança:** Implementação de autenticação via Header personalizado (X-API-Key).
- **Arquitetura Backend:** Estrutura focada em escalabilidade e facilidade de integração com outras automações (como n8n).

### 🛠️ Como executar este projeto:
1. Instale as dependências necessárias:
   `pip install fastapi uvicorn`
2. Inicie o servidor localmente:
   `python main.py`
3. Acesse a documentação interativa da API em:
   `http://localhost:8000/docs`
