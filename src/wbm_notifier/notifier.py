import requests
from config.manager import Config

config = Config()
NTFY_SERVER = config.NTFY_SERVER


def send_notification(title, message, link, topic):
    url = f"{NTFY_SERVER}/{topic}"
    response = requests.post(
        url,
        data=message.encode("utf-8"),
        headers={
            "Click": link,
            "Title": title,
        },
    )
    response.raise_for_status()
