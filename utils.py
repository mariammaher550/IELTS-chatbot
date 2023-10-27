def open_file(filepath):
    with open(filepath, 'r') as f:
        return f.read()