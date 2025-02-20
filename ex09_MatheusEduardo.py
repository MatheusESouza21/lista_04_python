#Faça um programa que pergunte em que direção o usuario deseja apontar
#cima (C ou c) se ele selecionar para cima peça um numero superior e conte de um ate esse numero
#se ele selecionar para baixo (B ou b) peça-lhe para ele inserir um numero abaixo de 20 e em seguida faça a contagem regressiva de 20 ate esse numero
#se ele digitar algo diferente de cima ou baixo exiba a mensagem "direção invalida"
direcao = input('Deseja apontar para cima ou para baixo? (C ou B): ').upper()
if direcao == 'C':
    num = int(input('Digite um número superior: '))
    for i in range(1, num + 1):
        print(i)
elif direcao == 'B':
    num = int(input('Digite um número menor que 20: '))
    if num < 20:
        for i in range(20, num - 1, - 1):
            print(i)
    else:
        print('Número alto demais')
else:
    print('Direção inálida')