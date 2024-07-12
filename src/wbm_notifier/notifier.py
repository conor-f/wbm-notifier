import requests
from config.manager import Config

config = Config()
NTFY_SERVER = config.NTFY_SERVER


def send_notification(message, topic):
    url = f"{NTFY_SERVER}/{topic}"
    response = requests.post(url, data=message.encode("utf-8"))
    response.raise_for_status()
