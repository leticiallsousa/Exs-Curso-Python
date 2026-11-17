expressao = str(input('Digite uma expressão: '))
pilha = []
for p in expressao:
    if p == '(':
        pilha.append(p)
    if p == ')':
        if len(pilha) == 0:
            pilha.append(p)
            break
        pilha.pop(0)

if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')
