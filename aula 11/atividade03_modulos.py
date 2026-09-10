from modulos.operacoes_fundamentais import soma, subtracao, divisao, multiplicacao

import random
import subprocess

subprocess.run ('cls', shell=True)
n1 = random.randint (11, 100)
n2 = random.randint (1, 10)

print(f'primeiro numero sorteado: {n1}')
print(f'segundo numero sorteado: {n2}')


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