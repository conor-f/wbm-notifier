import os
import unittest
from unittest.mock import patch
from config.manager import Config


class TestConfigOrder(unittest.TestCase):
    @patch.dict(
        os.environ,
        {
            "URL": "http://env-url.com",
            "SHELF_PATH": "/env/shelf/path",
            "TOPIC": "env-topic",
            "NTFY_SERVER": "http://env-ntfy-server.com",
            "CHECK_INTERVAL": "30",
            "NO_NOTIFICATION_INTERVAL": "30",
        },
    )
    @patch(
        "sys.argv",
        [
            "manager.py",
            "--url",
            "http://cli-url.com",
            "--shelf-path",
            "/cli/shelf/path",
            "--topic",
            "cli-topic",
            "--ntfy-server",
            "http://cli-ntfy-server.com",
            "--check-interval",
            "10",
        ],
    )
    @patch("configparser.ConfigParser.read", return_value=None)
    @patch(
        "configparser.ConfigParser.__getitem__",
        return_value={
            "URL": "http://config-url.com",
            "SHELF_PATH": "/config/shelf/path",
            "TOPIC": "config-topic",
            "NTFY_SERVER": "http://config-ntfy-server.com",
            "CHECK_INTERVAL": "20",
            "NO_NOTIFICATION_INTERVAL": "1000",
        },
    )
    def test_argument_order(self, mock_config_read, mock_config_getitem):
        config = Config()

        self.assertEqual(config.URL, "http://cli-url.com")
        self.assertEqual(config.SHELF_PATH, "/cli/shelf/path")
        self.assertEqual(config.TOPIC, "cli-topic")
        self.assertEqual(config.NTFY_SERVER, "http://cli-ntfy-server.com")
        self.assertEqual(config.CHECK_INTERVAL, 10)


if __name__ == "__main__":
    unittest.main()
