import random
import time

from config.manager import Config
from wbm_notifier.fetcher import fetch_webpage, parse_webpage
from wbm_notifier.notifier import send_notification
from wbm_notifier.storage import get_previous_content, store_content


def main():
    """
    Main function to monitor the webpage and send notifications on content change.
    """
    config = Config()

    last_notification_time = time.time()
    while True:
        content = fetch_webpage(config.URL)
        areas = parse_webpage(content)

        for entry in areas:
            title = "New apartment available!"

            message = f"Area: {entry['area']}\n"
            message += f"Address: {entry['address']}\n"
            message += f"Price: {entry['price']}\n"
            message += f"Size: {entry['size']}\n"
            message += f"Rooms: {entry['rooms']}\n"
            message += f"Features: {entry['features']}\n"

            link = f"https://www.wbm.de{entry['link']}"
            image_url = f"https://www.wbm.de{entry['image_url']}"

            if not get_previous_content(config.SHELF_PATH, message):
                send_notification(
                    title,
                    message,
                    link,
                    image_url,
                    config.TOPIC,
                )

                last_notification_time = time.time()

                store_content(
                    config.SHELF_PATH,
                    message,
                    True,
                )

        current_time = time.time()
        if (
            current_time - last_notification_time
            >= config.NO_NOTIFICATION_INTERVAL * 60
        ) and random.random() < 0.05:
            send_notification(
                "No new apartments",
                "Still running with no issues! Just nothing new found!",
                "",
                "",
                config.TOPIC,
            )
            last_notification_time = current_time

        time.sleep(config.CHECK_INTERVAL)


if __name__ == "__main__":
    main()
