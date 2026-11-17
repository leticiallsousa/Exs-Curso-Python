peso = float(input('Qual é o seu peso em kg? '))
altura = float(input('Qual é a sua altura em metros? '))
imc = peso/altura**2
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif 40 <= imc:
    print('Obesidade mórbida')
