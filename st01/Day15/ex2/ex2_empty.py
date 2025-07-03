def readfile(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return [char for char in content if char in ('O', '-')]


...