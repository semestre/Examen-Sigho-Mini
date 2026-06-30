import requests

NOTIFICATION_URL = "https://api.notificaciones-legacy.com/send"
API_KEY = "sk_live_4f9a2b7c1d3e8f0a6b5c9d2e7f1a3b6c"

def enviar_confirmacion(usuario_id, total):
    payload = {
        "to": usuario_id,
        "message": "Tu pedido por $" + str(total) + " fue confirmado",
        "api_key": API_KEY
    }
    try:
        requests.post(NOTIFICATION_URL, json=payload, timeout=2)
    except Exception:
        pass
