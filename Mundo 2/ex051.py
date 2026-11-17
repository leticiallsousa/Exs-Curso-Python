primeiro = int(input('Qual o primeiro termo dessa PA? '))
r = int(input('Qual a razão dessa PA? '))
dez = primeiro + 9*r
print('PA = {', end='')
for pa in range(primeiro, dez+1, r):
    if pa == dez:
        print(pa, end='}')
    else:
        print(pa, end=', ')

