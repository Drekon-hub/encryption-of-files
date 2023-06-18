def write_file(fileName, content):
    with open(f'{fileName}.txt', 'w') as file:
        file.write(content)
