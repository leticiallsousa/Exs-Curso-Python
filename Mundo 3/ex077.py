palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar',
            'Mercado', 'Trabalhador', 'Futuro')
vogais = tuple()
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra.lower()}', end=' ')
