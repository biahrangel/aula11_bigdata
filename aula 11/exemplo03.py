#biblioteca 

from modulos.operacoes import calcula_dobro, calcula_metade, calcula_quadrado, calcula_triplo
import random
import subprocess


subprocess.run('cls', shell=True) # serve para limpar o terminal 
n = random.randint(1, 10) # gera numeros aleatorios 

print (f'numero sorteado: {n}')

print (' [1] - dobro\n [2] - triplo\n [3] - quadrado\n [4] - metade')

opcao = int(input('\n Escolha uma opcao acima: '))

match opcao: 
     case 1:
        resposta = calcula_dobro(n)

     case 2:
        resposta = calcula_triplo (n)

     case 3: 
        resposta = calcula_quadrado (n)

     case 4: 
        resposta = calcula_metade (n)

     case _: 
         print('\nOpcao inválida!')


print(f'Resultado: {resposta}')
# print ('Fim!')
