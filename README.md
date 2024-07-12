# WBM Notifier

# Type annotations
type VENV_DIR: str


## About

WBM Notifier is a python package that monitors a webpage, and provides
notifications using ntfy.sh when the contents change.

It does this by running on a schedule. Each time it runs, it gets a webpage,
parses it using BeautifulSoup, and checks a Python Shelf to see if the content
is different from previous runs. It then stores the new webpage on the shelf.
If the content is different from the previous run, then it sends a POST
request to ntfy.sh saying that the content has changed.



## Configuration Precedence

The configuration variables are determined in the following order of precedence:
1. Environment Variables
2. `config.ini` file
