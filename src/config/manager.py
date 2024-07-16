import configparser
import os
import argparse


class Config:
    def __init__(self, config_file="config.ini"):
        """
        Initialize the Config object by reading from the config file, command line
        arguments, and environment variables.
        """
        parser = argparse.ArgumentParser(description="Webpage Monitor Configuration")
        parser.add_argument("--url", type=str, help="URL of the webpage to monitor")
        parser.add_argument(
            "--shelf-path",
            type=str,
            help="Path to the shelf file for storing webpage content",
        )
        parser.add_argument("--topic", type=str, help="Notification topic")
        parser.add_argument("--ntfy-server", type=str, help="ntfy server URL")
        parser.add_argument(
            "--check-interval", type=int, help="Interval between checks in seconds"
        )
        parser.add_argument(
            "--no-notification-interval",
            type=int,
            help="Interval in minutes to notify if no new listings are found",
        )
        parser.add_argument(
            "--telegram-bot-auth", type=str, help="Telegram bot authentication token"
        )
        parser.add_argument("--telegram-chat-id", type=str, help="Telegram chat ID")
        args = parser.parse_args()

        self.config = configparser.ConfigParser()
        self.config.read(config_file)

        self.config = configparser.ConfigParser()
        self.config.read(config_file)

        self.URL = args.url or os.getenv("URL", self.config["DEFAULT"]["URL"])
        self.SHELF_PATH = args.shelf_path or os.getenv(
            "SHELF_PATH", self.config["DEFAULT"]["SHELF_PATH"]
        )
        self.TOPIC = args.topic or os.getenv("TOPIC", self.config["DEFAULT"]["TOPIC"])
        self.NTFY_SERVER = args.ntfy_server or os.getenv(
            "NTFY_SERVER", self.config["DEFAULT"]["NTFY_SERVER"]
        )
        self.CHECK_INTERVAL = args.check_interval or int(
            os.getenv("CHECK_INTERVAL", self.config["DEFAULT"]["CHECK_INTERVAL"])
        )
        self.NO_NOTIFICATION_INTERVAL = args.no_notification_interval or int(
            os.getenv(
                "NO_NOTIFICATION_INTERVAL",
                self.config["DEFAULT"]["NO_NOTIFICATION_INTERVAL"],
            )
        )
        self.TELEGRAM_BOT_AUTH = args.telegram_bot_auth or os.getenv(
            "TELEGRAM_BOT_AUTH", self.config["DEFAULT"].get("TELEGRAM_BOT_AUTH", None)
        )
        self.TELEGRAM_CHAT_ID = args.telegram_chat_id or os.getenv(
            "TELEGRAM_CHAT_ID", self.config["DEFAULT"].get("TELEGRAM_CHAT_ID", None)
        )
        self.SHELF_PATH = args.shelf_path or os.getenv(
            "SHELF_PATH", self.config["DEFAULT"]["SHELF_PATH"]
        )
        self.TOPIC = args.topic or os.getenv("TOPIC", self.config["DEFAULT"]["TOPIC"])
        self.NTFY_SERVER = args.ntfy_server or os.getenv(
            "NTFY_SERVER", self.config["DEFAULT"]["NTFY_SERVER"]
        )
        self.CHECK_INTERVAL = args.check_interval or int(
            os.getenv("CHECK_INTERVAL", self.config["DEFAULT"]["CHECK_INTERVAL"])
        )
        self.NO_NOTIFICATION_INTERVAL = args.no_notification_interval or int(
            os.getenv(
                "NO_NOTIFICATION_INTERVAL",
                self.config["DEFAULT"]["NO_NOTIFICATION_INTERVAL"],
            )
        )
