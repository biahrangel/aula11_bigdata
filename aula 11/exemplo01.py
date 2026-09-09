
def calcula_dobro (x):
    r = x * 2
    return r


def calcula_triplo (y):
    r = y * 3
    return r


def calcula_quadrado (z):
    r = z ** 2
    return r


def calcula_metade (a):
    r = a / 2
    return r

 
n = int (input('Informe o numero: '))

# print('\n ###### Menu de opcoes ######')

# print (30*'=')

print (' [1] - dobro\n [2] - triplo\n [3] - quadrado\n [4] - metade')

opcao = int(input('\n Escolha uma opcao acima: '))

match opcao: 
     case 1:
        # dobro = n * 2
        # print(f'\nO dobro é: {dobro}')
        resposta = calcula_dobro(n)

     case 2:
        #  triplo = n * 3
        #  print(f'\nO triplo é: {triplo}')
        resposta = calcula_triplo (n)

     case 3: 
        #  quadrado = n ** 2
        #  print(f'\nO quadrado é: {quadrado}')
        resposta = calcula_quadrado (n)

     case 4: 
        resposta = calcula_metade (n)


     case _: 
         print('\nOpcao inválida!')


print(f'Resultado: {resposta}')
# print ('Fim!')


