frase = input('Escreva uma frase: ')
print(f'Nessa frase a letra A parece {frase.upper().count("A")} vezes\n'
      f'Ela aparece na posição {frase.upper().find("A")+1} pela primeira vez\n'
      f'Ela aparece na posição {frase.upper().rfind("A")+1} pela útima vez')
