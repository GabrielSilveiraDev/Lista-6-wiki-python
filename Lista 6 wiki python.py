#Lista 6 wiki python
""
#Exercício 1:

string1 = str(input('Digite a primeira string: '))
string2 = str(input('Digite a segunda string: '))

palavra1 = string1.split()
palavra2 = string2.split()

string1.split()
string2.split()

print(f'Tamanho de "{palavra1}": {len(string1)} caracteres  ')
print(f'Tamanho de "{palavra2}": {len(string2)} caracteres  ')

if len(string1) == len(string2):
    print('As duas strings tem o mesmo tamanho ')

elif len(string1) != len(string2):
    print('As duas strings tem tamanhos diferentes ')

if string1 == string2:
    print('As duas strings possuem o mesmo conteúdo ')

elif string1 != string2:
    print('As duas strings possuem conteúdo diferente')


""

#Exercício 2:

nome = str(input('Digite seu nome: '))
nome.split()

print("Nome invertido e em maiusculo:", nome.upper()[:: -1])


""

#Exercício 3:

nome = str(input('Digite seu nome: '))

nome.split()

for i in nome:
    print(f'{i.upper()}')


""

#Exercício 4:

nome = str(input('Digite seu nome: '))

nome.split()

for i in range(len(nome)):
    if i != 0:
        print()
    for j in range(0,i):

        print(f'{nome[j].upper()}',end='')


""

#Exercício 5:

nome = str(input('Digite seu nome: '))

nome.split()


for i in range(len(nome)):
    if i != 0:
        print()
    for j in range(i,len(nome)):

        print(f'{nome[j-i].upper()}',end='')


""

#Exercício 6:

mes = 0

data = str(input('Digite sua data de nascimento sem / '))

data.split()

if data[2]+data[3] == '01':

    mes = 'Janeiro'

elif data[2]+data[3] == '02':

    mes = 'Fevereiro'

elif data[2]+data[3] == '03':

    mes = 'Março'

elif data[2]+data[3] == '04':

    mes = 'Abril'

elif data[2]+data[3] == '05':

    mes = 'Maio'

elif data[2]+data[3] == '06':

    mes = 'Junho'

elif data[2]+data[3] == '07':

    mes = 'Julho'

elif data[2]+data[3] == '08':

    mes = 'Agosto'

elif data[2]+data[3] == '09':

    mes = 'Setembro'

elif data[2]+data[3] == '10':

    mes = 'Outubro'

elif data[2]+data[3] == '11':

    mes = 'Novembro'

elif data[2]+data[3] == '12':

    mes = 'Dezembro'


print(f'Você nasceu em {data[0]+data[1]} de {mes} de {data[4]+data[5]+data[6]+data[7]}')

""

#Exercício 7:

string = str(input('Digite uma string: '))

string.split()

print(string.count(' '))
print(string.count('a'))
print(string.count('e'))
print(string.count('i'))
print(string.count('o'))
print(string.count('u'))

""

#Exercício 8:

nome = str(input('Digite uma palavra: '))
lista = nome.split()
nome.split()
palavra = lista[0]
if nome.upper()[:: -1] == palavra.upper():
    print(f'{nome.upper()} é um palindromo')

else:
    print(f'{nome.upper()} não é um palindromo')

""

#Exercício 9:

cpf = str(input('Digite seu CPF: '))
cpf.split()

if int(cpf[0]) <= 9 and int(cpf[1]) <= 9 and int(cpf[2]) <= 9 and (cpf[3]) == '.' and int(cpf[4]) <= 9 and int(cpf[5]) <= 9 and int(cpf[6]) <= 9 and (cpf[7]) == '.' and int(cpf[8]) <= 9 and int(cpf[9]) <= 9 and int(cpf[10]) <= 9 and (cpf[11]) == '-' and int(cpf[12]) <= 9 and int(cpf[13]) <= 9:
    print(f'o CPF {cpf} é válido.')

else:
    print('CPF inválido')


""

#Exercício 10:


while True:

    num = str(input('Digite Um número até 99: '))

    if 0 <= int(num) <= 99:
        break

num.split()

dezena = 0
unidade = 0

if num[0] != '1':

    if num[0] == '2':

        dezena = 'Vinte'

    elif num[0] == '3':

        dezena = 'Trinta'

    elif num[0] == '4':

        dezena = 'Quarenta'

    elif num[0] == '5':

        dezena = 'Cinquenta'

    elif num[0] == '6':

        dezena = 'Sessenta'

    elif num[0] == '7':

        dezena = 'Setenta'

    elif num[0] == '8':

        dezena = 'Oitenta'

    elif num[0] == '9':

        dezena = 'Noventa'

    if num[1] == '1':

        unidade = 'Um'

    elif num[1] == '2':

        unidade = 'Dois'

    elif num[1] == '3':

        unidade = 'Três'

    elif num[1] == '4':

        unidade = 'Quatro'

    elif num[1] == '5':

        unidade = 'Cinco'

    elif num[1] == '6':

        unidade = 'Seis'

    elif num[1] == '7':

        unidade = 'Sete'

    elif num[1] == '8':

        unidade = 'Oito'

    elif num[1] == '9':

        unidade = 'Nove'

    if num[0] == '0' and num[1] != '0':

        print(unidade)

    elif num[0] == '0' and num[1] == '0':

        print('Zero')

    elif num[0] != 0 and num[1] == '0':

        print(dezena)

    else:
        print(f'{dezena} e {unidade}')

if num[0] == '1':

    if num[1] == '0':

        print('Dez')

    elif num[1] == '1':

        print('Onze')

    elif num[1] == '2':

        print('Doze')

    elif num[1] == '3':

        print('Treze')

    elif num[1] == '4':

        print('Catorze')

    elif num[1] == '5':

        print('Quinze')

    elif num[1] == '6':

        print('Dezesseis')

    elif num[1] == '7':

        print('Dezessete')

    elif num[1] == '8':

        print('Dezoito')

    elif num[1] == '9':

        print('Dezenove')


""

#Exercício 11:

""

from random import randint

f = open('arqv.txt','r')
palavras = []

for line in f:
    line = line.strip()
    palavras.append(line)

f.close()

aleatorio = randint(0,len(palavras)-1)
palavra = palavras[aleatorio]
lista = []

for i in range(len(palavra)):

    if palavra[i] == '-':
        lista.append('-')

    elif palavra[i] == 'ç':
        lista.append('ç')

    elif palavra[i] == 'é':
        lista.append('é')

    elif palavra[i] == 'á':
        lista.append('á')

    elif palavra[i] == 'í':
        lista.append('í')

    elif palavra[i] == 'ó':
        lista.append('ó')

    elif palavra[i] == 'ô':
        lista.append('ô')

    elif palavra[i] == 'â':
        lista.append('â')

    elif palavra[i] == 'ê':
        lista.append('ê')

    elif palavra[i] == 'ã':
        lista.append('ã')

    else:
        lista.append('_')

palavraCompleta = palavra.split()
conterros = 0
contador2 = 0

for j in lista:
    print(f'{j.upper()}', end=' ')
print()

while True:

    cont = 0
    contador2 = 0

    tentativa = str(input('Digite uma letra: '))

    if tentativa.upper() == palavraCompleta[0].upper():
        print(f'Você venceu.\nA palavra era {palavra.upper()}')
        break

    for i in range(len(palavra)):
        if tentativa.upper() == palavra[i].upper():
            lista[i] = tentativa
            contador2 += 1

    for k in range(len(palavra)):

        if palavra[k].upper() == lista[k].upper():
            cont += 1

    if contador2 == 0:
        conterros += 1

        print(f'Você errou pela {conterros}º vez')
        if conterros == 6:
            print(f'Você perdeu.\nA palavra era {palavra.upper()}')
            break

    for j in lista:
        print(f'{j.upper()}', end=' ')
    print()
    if cont == len(palavra):
        print(f'Você venceu.\nA palavra era {palavra.upper()}')
        break

""

#Exercício 12:

telefone = str(input('Digite o seu telefone, apenas os números: '))

if '-' in telefone:
    telefone = telefone.replace('-','')

lista = telefone

if len(lista) <= 7:

    while len(telefone) != 8:
        print(f'Telefone possui {len(telefone)} dígitos. Vou acrescentar o digito três na frente.')
        telefone = '3'+telefone
print('Telefone corrigido sem formatação: ',end='')

for i in telefone:
    print(f'{i}',end='')
print()
lista = telefone.split()
print('Telefone corrigido com formatação: ',end='')
for i in range (len(telefone)):

    if i == 4 and telefone[4] != '-':

        print('-',end='')

    print(f'{telefone[i]}',end='')
print()



""


#Exercício 13:

from random import randint

f = open('arqv 1.txt','r')
palavras = []

for line in f:
    line = line.strip()
    palavras.append(line)

f.close()

j = randint(0,len(palavras)-1)

palavra = palavras[j]
lista = []
listaAleatorio = []

while len(lista) != len(palavra):

    k = randint(0, len(palavra)-1)
    if k not in listaAleatorio:
        listaAleatorio.append(k)
        lista.append(palavra[k])
palavraCompleta = palavra.split()
conterros = 0

for j in lista:
    print(f'{j.upper()}', end=' ')
print()

while True:

    tentativa = str(input('Digite a palavra: '))

    if tentativa.upper() == palavraCompleta[0].upper():
        print(f'Você venceu.\nA palavra era {palavra.upper()}')
        break

    else:
        conterros += 1

        print(f'Você errou pela {conterros}º vez')
        if conterros == 6:
            print(f'Você perdeu.\nA palavra era {palavra.upper()}')
            break

""

#Exercício 14:

palavra = str(input('Digite uma palavra para traduzi-la pro alfabeto leet spek: '))
lista = []

for i in range(len(palavra)):

    if palavra[i].upper() == 'A':

        lista.append('4')

    elif palavra[i].upper() == 'B':

        lista.append('13')

    elif palavra[i].upper() == 'C':

        lista.append('(')

    elif palavra[i].upper() == 'D':

        lista.append('[)')

    elif palavra[i].upper() == 'E':

        lista.append('3')

    elif palavra[i].upper() == 'F':

        lista.append('|=')

    elif palavra[i].upper() == 'G':

        lista.append('6')

    elif palavra[i].upper() == 'H':

        lista.append('|-|')

    elif palavra[i].upper() == 'I':

        lista.append('|')

    elif palavra[i].upper() == 'J':

        lista.append('.]')

    elif palavra[i].upper() == 'K':

        lista.append('|<')

    elif palavra[i].upper() == 'L':

        lista.append('1')

    elif palavra[i].upper() == 'M':

        lista.append('|Y|')

    elif palavra[i].upper() == 'N':

        lista.append('/\/')

    elif palavra[i].upper() == 'O':

        lista.append('0')

    elif palavra[i].upper() == 'P':

        lista.append('|>')

    elif palavra[i].upper() == 'Q':

        lista.append('0,')

    elif palavra[i].upper() == 'R':

        lista.append('|2')

    elif palavra[i].upper() == 'S':

        lista.append('5')

    elif palavra[i].upper() == 'T':

        lista.append('7')

    elif palavra[i].upper() == 'U':

        lista.append('[_]')

    elif palavra[i].upper() == 'V':

        lista.append('\/')

    elif palavra[i].upper() == 'W':

        lista.append('\/\/')

    elif palavra[i].upper() == 'X':

        lista.append('}{')

    elif palavra[i].upper() == 'Y':

        lista.append('`/')

    elif palavra[i].upper() == 'Z':

        lista.append('2')

for i in lista:
    print(f'{i}',end=' ')

""