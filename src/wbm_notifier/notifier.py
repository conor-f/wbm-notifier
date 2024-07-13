import requests
from config.manager import Config

config = Config()
NTFY_SERVER = config.NTFY_SERVER


def send_notification(title, message, link, image_link, topic):
    url = f"{NTFY_SERVER}/{topic}"
    response = requests.post(
        url,
        data=message.encode("utf-8"),
        headers={
            "Click": link,
            "Title": title,
            "Icon": image_link,
            "Priority": "5",
            "Tags": "house",
        },
    )
    response.raise_for_status()
