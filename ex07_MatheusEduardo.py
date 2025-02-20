#Peça ao usuario para inserir seu nome e um numero. Se o numero for menor que 10, exiba o nome dele esse numero de vezes caso contrario exiba a mensagem "numero muito alto"
nome = input('Digite seu nome: ')
num = int(input('Digite um número menor que 10: '))
if num < 10:
    for i in range(num):
        print(nome)
else:
    print('Número muito alto.')
