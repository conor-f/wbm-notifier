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
        args = parser.parse_args()

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
