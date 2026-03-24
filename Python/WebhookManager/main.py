# main.py
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Webhook Manager Pro")

class WebhookPayload(BaseModel):
    event_type: str
    data: dict
    source: str

@app.post("/v1/process")
async def process_webhook(payload: WebhookPayload, x_api_key: str = Header(None)):
    # Simulação de validação de segurança (Sênior!)
    if x_api_key != "motech_secret_key":
        raise HTTPException(status_code=403, detail="Acesso não autorizado")
    
    print(f"Evento {payload.event_type} recebido de {payload.source}")
    return {"status": "success", "message": "Dados processados com sucesso"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
