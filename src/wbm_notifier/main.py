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
        parsed_content = parse_webpage(content)

        previous_content = get_previous_content(config.SHELF_PATH, config.URL)

        if parsed_content != previous_content:
            send_notification("Webpage content has changed!", config.TOPIC)
            store_content(config.SHELF_PATH, config.URL, parsed_content)

        time.sleep(config.CHECK_INTERVAL)


if __name__ == "__main__":
    main()
