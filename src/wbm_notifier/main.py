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

                store_content(
                    config.SHELF_PATH,
                    message,
                    True,
                )

        time.sleep(config.CHECK_INTERVAL)


if __name__ == "__main__":
    main()
