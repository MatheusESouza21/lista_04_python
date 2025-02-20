#Peça um numero abaixo de 50 e em seguida faça uma contagem regressiva de 50 ate esse número, certificando-se de mostrar o numero que eles inseriram na saida
num = int(input('Digite um número abaixo de 50: '))
if num <50:
    for i in range(50, num - 1, - 1):
        print(i)
else:
    print('Número alto demais')