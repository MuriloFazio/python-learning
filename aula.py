### global
from pyrsistent import b


#nome = 'Filipe'

idade = 30

#print(nome, idade)

def aniverseirio(a):
    ### escopo da funcao aniverseirio
    a = 2
    return a+1

dert = aniverseirio(idade)

#print(dert)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa('Pera', 26)

pessoa2 = Pessoa('Ferro', 26)

pessoa2 = 'dert'

#print(pessoa2.idade)




def pera(a, b):
    print('Chamei o Pera '+'\nmeu tio')
    return a+b

#print(pera(14,33))


def meu_tio(a, b):
    c = 3
    print('Chamei meu tio', c)
    return a*b

#print(meu_tio(5,4))


nome1 = 'Isa'
nome2 = 'Fredy'
nome3 = 'Baguinho'

familia = ['Isa', nome2, nome3]

#print(pera(pera(1,2),2) + meu_tio(2,3))


def chama(nome, numero):
    if nome == 'chama meu nome' and numero == 2:
        print('Pedro Sampaio')
    else:
        print('Errou')



#chama('chama meu nome', 2)


dicionario = {'arroz': 'Murrrilo', 'bitxona' : 'Ferro', 'fruta' : 'Pera'}

#print(dicionario['bitxona'])



def chama(nome, numero):
    if nome == 'chama meu nome' and numero == 2:
        print('Pedro Sampaio')
    elif nome == 'chama meu nome' and numero == 3:
        print('quase lá')
    elif nome == 'chama meu nome' and numero == 4:
        print('quase lá')
    else:
        print('Errou')
    print('sai fora') 

#chama('chama meu nome', 3)

frutas = ['maça', 'laranja', 'kiwi', 'pera']

#nome = input('Digite seu nome ')

#while nome != 'Pera':
#    nome = input('Digita seu nome ')
#    if nome == 'Pera':
#        print('Viadao')
#    elif nome == 'Filipe':
#        print('Trouxa')
#    elif nome == 'Murilo':
#        print('gay')


import requests

#cep = input('digite seu cep: \n')

#logradouro = requests.get('https://viacep.com.br/ws/'+cep+'/json/')

#print(logradouro.status_code)

#print(logradouro.json())

#for key, valor in logradouro.json().items():
#    print(key,valor)


card = input('Fala o bixinho: ')

request = requests.get('https://api.scryfall.com/cards/named?fuzzy='+card)

#for key, valor in request.json().items():
#    print(key,valor)

print(request.json(power))
