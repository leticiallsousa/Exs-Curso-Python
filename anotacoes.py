# adicionar o end em um print para decidir o que vai no fim da linha
# exemplo:
print('oi, ', end='')  # o end com nada nas aspas, fez com que o print de baixo subisse para a linha de cima
print('meu nome é Letícia')

# \033[(style;text;back)m
# \033[0;00;00m
# style: 0 (None); 1 (Bold); 2 (Underline); 3 (Negative);
# text: 30 (Branco); 31 (Vermelho; 32 (Verde); 33 (Amarelo); 34 (Azul); 35 (Roxo); 36 (Ciano); 37 (Cinza);
# back: 40 (Branco); 41 (Vermelho; 42 (Verde); 43 (Amarelo); 44 (Azul); 45 (Roxo); 46 (Ciano); 47 (Cinza);
# Exemplo:
print('\033[1;30;41mOlá Mundo!\033[m')

# dados = {}  ou dados = dict() para criar um dicionário
dados = {"nome": 'Letícia', "sexo": 'F', "idade": 15} 
dados["idade"] = 16 # modifica o dicinário
del dados["idade"] # deleta um elemento do dicionário
print(dados)
print(dados.values()) # vai printar os valores/conteúdos do dicionário
print(dados.keys()) # vai printar as chaves/etiquetas/categorias do dicionário
print(dados.items()) # vai printar ambos

# para um print formatado:
filme = {'título':'Star Wars', 'ano': '1977'}
for k, v in filme.items(): # precisa usar o items, values ou keys!!!
    print(f"O {k} é {v}")

# é possível colocar dicionários dentro de listas e também dentro de outros dicionários
locadora = [filme]
avengers = {'título': 'Avengers', 'ano': '2012'}
matrix = {'título': 'Matrix', 'ano': '1999'}
locadora.append(avengers) # posso adicionar o dicionário à lista com o append
locadora.append(matrix)
print(locadora[0]['ano']) # vai retornar '1977'
print(locadora[2]['título']) # vai retornar 'Matrix'

estado = dict()
brasil = list()
for n in range(0,3):
    estado['nome'] = str(input('Qual o nome do estado?'))
    estado['uf'] = str(input('Qual a UF do estado?'))
    # brasil.append(estado) como são duas listas diferentes, vai acabar criando uma ligação 
    # entre elas, e sempre que modificar o estado, também vai modificar o brasil, deixando 
    # os 3 itens iguais ao último estado escrito
    # brasil.append(estado[:]) usaríamos isso se estivéssemos lidando apenas com listas, mas
    # não funciona com dicionários, então existe uma função apenas para isso: .copy()
    brasil.append(estado.copy())
print(brasil)

for e in brasil: # vai entrar na lista do brasil pra acessar os estados
    for k, v in e.items(): # vai acessar o conteúdo de cada estado
        print(f'O campo {k} tem valor {v}')


help(input) # mostra informações sobre o comando input, pode usar pra qualquer função
print(input.__doc__) # mostra informações sobre o input, pode usar pra qualquer função

def contador(i, f, p): # cria uma função personalizada para o seu código
    """ 
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    # abrindo e fechando 3 aspas duplas abaixo do def, dá pra fazer sua própria resposta
    # pro comando de help
help(contador)

def soma(a, b, c):
    soma = a+b+c
    print(f'A soma é {soma}')
# desse jeito, se a pessoa informar menos de três valores, vai dar erro
# para não dar erro, o ideal seria deixar todos os valores como opcionais
def soma(a=0, b=0, c=0):
    soma = a+b+c
    print(f'A soma é {soma}')
# dessa forma mesmo que nenhum valor seja informado, não vai dar erro

# para que o usuário possa informar quantos valores quiser e mesmo assim dar certo, todos os
# valores precisam ser * :
def soma(*num):
    soma = sum(num)
    print(f'A soma é {soma}')
soma(3,4,5,6,7,8,9)


# considere o código seguinte:
n = 2
def teste():
    x = 1
    print(f'x vale {x}')
    print(f'n vale {n}')
    # nessa área, quando a função for utilizada, tudo vai ocorrer normalmente
# mas se eu for tentar utilizar a variável x fora da função, vai dar erro:
# print(f'x vale {x}') vai dar erro porque x só foi declarado como uma variável local
print(f'n vale {n}') # não vai dar erro porque n foi declarado como uma variável global


# considere esse outro código:
a = 1 # criei uma variável global
def teste(b): # como a variável a foi usada como parâmetro, o b tem o valor de a
    b += 2 # a(1) + b(2) = 3
    print(f'B vale {b}') # vai mostrar B vale 3
    global a
    a = 5   # esse valor NÃO VAI substituir o outro valor de a, vai ser criada outra
            # variável com mesmo nome, para que isso não aconteça, deixe claro que quer
            # usar a variável a global no inicio do código
    # agora sim quando modificar o a, será modificado o a global
teste(a) 

def somar(a=0, b=0, c=0):
    soma = a+b+c
    return soma
    # antes só era possível usar o resultado da soma dentro da função, com o return é
    # possível retornar o resultado para uma variável, print, ou usar esse resultado de
    # qualquer forma

r1 = somar(1, 4, 7)
r2 = somar(3, 8, 5)
r3 = somar(2, 4, 6)
print(f'Os resultados das somas são respectivamente: {r1}, {r2}, {r3}.')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print(f'O número {num} é par!')
else:
    print(f'O número {num} não é par!')


def fatorial(n=1):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f

numero = int(input('Digite um número: '))
print(f'O fatorial de {numero} é igual a {fatorial(numero)}')

# 

lista_frutas = ['maçã', 'banana', 'laranja']
texto = ', '.join(lista_frutas)
print(texto)

# 

frutas = ['maçã', 'banana', 'laranja']
for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")

#
    
for numero in range(10):
    if numero == 5:
        continue  # Pula para a próxima iteração quando o valor é 5
    print(numero)

#
dicionario_frutas = {'maçã': 3, 'banana': 5, 'laranja': 2}
valor = dicionario_frutas.pop('maçã')  # Remove a chave 'maçã' e obtém o valor (3)
# Agora, valor contém o valor associado à chave 'maçã', e a chave 'maçã' é removida do dicionário.

ultimo_item = dicionario_frutas.popitem()
print(ultimo_item)  # Exemplo de saída: ('banana', 6)
# O método popitem() remove e retorna o último par chave-valor inserido no dicionário:

valor_maça = dicionario_frutas.get('maçã', 0)
# Neste caso, 0 é o valor padrão que será retornado se a chave 'maçã' não existir no dicionário dicionario_frutas


# A escolha de ensinar ou não sobre conjuntos (set) em um curso de Python pode depender dos objetivos específicos do curso e do público-alvo. Vamos analisar algumas considerações:
# Sets em Python:
# Sem Duplicatas: Conjuntos são úteis quando você precisa de uma coleção de elementos únicos. Eles garantem que não há duplicatas, o que pode ser útil em diversas situações.
# Operações de Conjunto: Sets suportam operações de conjunto, como união, interseção e diferença, o que pode ser útil par
# Desempenho: Em termos de desempenho, conjuntos podem ser mais eficientes para verificar a existência de um elemento (por causa de sua implementação interna baseada em tabela de hash).
# Quando Usar Conjuntos:
# Remoção de Duplicatas: Se você precisa armazenar uma coleção de elementos únicos e não se preocupa com a ordem, um conjunto é uma escolha eficiente.
# Operações de Conjunto: Se você precisa realizar operações de conjunto (união, interseção, etc.), conjuntos são uma escolha natural.
# Verificação de Existência: Se você precisa verificar rapidamente se um elemento está presente na coleção, conjuntos oferecem uma busca eficiente.
# Quando Não Usar Conjuntos:
# Ordem Importante: Se a ordem dos elementos é importante para sua aplicação, conjuntos não preservam a ordem dos elementos.
# Duplicatas Importantes: Se você precisa permitir duplicatas em sua coleção, conjuntos não são a escolha adequada.

# if 2==2:
#    raise TipoDeExcecao("Mensagem de erro opcional")
# serve pra levantar uma exceção em uma determinada parte do código (você escolhe)

# lambda parametro: retorno
