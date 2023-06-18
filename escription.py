from main import *

encrypted = []
text_encrypted = ''

def escription(fileName):
    with open(f'{fileName}.txt', 'r') as file:
        lines = file.readlines()
        for word in lines:
            for character in word:
                ascii = ord(character)
                code_ascii.append(ascii)
        for ascii in code_ascii:
            code_encrypted.append(ascii * n)
    file.close()
    with open(f'{fileName}.txt', 'w') as file:
        for i in range(len(code_encrypted)):
            encrypted.append(str(code_encrypted[i]))
        text_encrypted = ' '.join(encrypted)
        file.write(text_encrypted)

    

