import string
from unicodedata import normalize

f = str(input('Digite uma frase: '))
f = normalize('NFKD', f.replace(' ', '')).encode('ascii', 'ignore').decode('ASCII').translate\
    (str.maketrans('', '', string.punctuation)).lower()
print(f)
if f == f[::-1]:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')
