palavra = input('Diga algo: ')
print(f'Tipo primitivo: {type(palavra)}\n'
      f'Só tem espaços: {palavra.isspace()}\n'
      f'É alfanúmerico: {palavra.isalnum()}\n'
      f'É alfabético: {palavra.isalpha()}\n'
      f'É numérico: {palavra.isnumeric()}\n'
      f'Está em maiúsculas: {palavra.isupper()}\n'
      f'Está em minúsculas: {palavra.islower()}\n'
      f'Está capitalizada: {palavra.istitle()}')
