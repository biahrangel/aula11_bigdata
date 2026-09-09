# soma, subtracao, multiplicacao e divisao 

def soma (x, y):
    a = n1 + n2
    return a


def subtracao (x, y):
    a = n1 - n2
    return a


def multiplicacao (x, y):
    a = n1 * n2
    return a


def divisao (x, y):
    a = n1 / n2
    return a



n1 = int (input('Informe o primeiro numero: '))
n2 = int (input('Informe o segundo numero: '))

print (' [1] - soma\n [2] - subtracao\n [3] - multiplicacao\n [4] - divisao')

alternativa = int(input('\n Escolha uma alternativa acima: '))

match alternativa:
    case 1: 
        a = soma (n1, n2)

    case 2: 
        a = subtracao (n1, n2)

    case 3: 
        a = multiplicacao (n1, n2)
    
    case 4:
        a = divisao (n1, n2)

print (f'Resposta: {a}')