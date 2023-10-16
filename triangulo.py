# crie um prog que leia os 3 lados de um triangulo
# verificar se os lados de um polígono formam um triangulo
# informar o tipo de triangulo formado
print('Para formar um Triangulo: ')
ladoA = int(input('Digite o tamanho do lado A: '))
ladoB = int(input('Digite o tamanho do lado B: '))
ladoC = int(input('Digite o tamanho do lado C: '))
if ladoA < (ladoB + ladoC) and ladoB < (ladoA + ladoC) and ladoC < (ladoA + ladoB):
    print(f'Os lados formam um triangulo')
else:
    print(f'Os lados NÃO formam um triangulo')
