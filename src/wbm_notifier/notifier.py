import requests
import apprise
from config.manager import Config

config = Config()
NTFY_SERVER = config.NTFY_SERVER


def send_notification(title, message, link, image_link, topic):
    # Send notification via ntfy
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
    # Send notification via Telegram if credentials are provided
    if config.TELEGRAM_BOT_AUTH and config.TELEGRAM_CHAT_ID:
        send_telegram_notification(title, message, link)

def send_telegram_notification(title, message, link):
    apobj = apprise.Apprise()
    apobj.add(f"tgram://bot{config.TELEGRAM_BOT_AUTH}/{config.TELEGRAM_CHAT_ID}/")
    apobj.notify(
        body=f"{message}\n\n{link}",
        title=title,
    )
