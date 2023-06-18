from create_file import *
from write_file import *
from escription import *
from decryption import *
#variable
p = 7
q = 13
n = p * q
code_ascii = []
code_encrypted = []
content = 'Yair y Melissa\nAmor For Ever'
fileName = 'Melissa'


if __name__ == "__main__":
    # fileName = input('fileName: ')
    # content = input('content: ')
    # create_file(fileName)
    # write_file(fileName, content)
    escription(fileName)
    # decryption(fileName)
    pass