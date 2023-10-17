#Finalizado
# crie um prog que leia os 3 lados de um triangulo
# verificar se os lados de um polígono formam um triangulo
# informar o tipo de triangulo formado
print('Para formar um Triangulo: ')
ladoA = int(input('Digite o tamanho do lado A: '))
ladoB = int(input('Digite o tamanho do lado B: '))
ladoC = int(input('Digite o tamanho do lado C: '))
if ladoA < (ladoB + ladoC) and ladoB < (ladoA + ladoC) and ladoC < (ladoA + ladoB):
    print(f'\nOs lados formam um triangulo.\n')
    if (ladoA == ladoB) and (ladoA == ladoC):
        print('\n - Equilatero\n')
    elif (ladoA == ladoB) or (ladoA == ladoC) or (ladoB == ladoC):
        print('\n - Isósceles\n')
    else:
        print('\n - Escaleno\n')
else:
    print(f'\nOs lados NÃO formam um triangulo\n')


