import requests

NOTIFICATION_URL = "https://api.notificaciones-legacy.com/send"

def enviar_confirmacion(usuario_id, total):
    payload = {"to": usuario_id, "message": "Tu pedido por $" + str(total) + " fue confirmado"}
    requests.post(NOTIFICATION_URL, json=payload, timeout=2)
