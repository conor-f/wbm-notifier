import shelve


def get_previous_content(shelf_path, key):
    print(f"Gotten key (get): {key}")
    with shelve.open(shelf_path) as shelf:
        print(shelf.get(key, False))
        return shelf.get(key, False)


def store_content(shelf_path, key, content):
    print(f"Gotten key (store): {key}")
    print(content)
    with shelve.open(shelf_path) as shelf:
        shelf[key] = content
