import shelve


def get_previous_content(shelf_path, key):
    with shelve.open(shelf_path) as shelf:
        return shelf.get(key, False)


def store_content(shelf_path, key, content):
    with shelve.open(shelf_path) as shelf:
        shelf[key] = content
