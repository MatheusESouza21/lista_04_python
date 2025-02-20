#Faça um programa que pergunte quantas pessoas o usuário deseja convidar para uma festa.
#	Se ele digitar um número abaixo de 10, peça os nomes e após cada nome exiba a mensagem: "[nome] está convidado para a festa". 
#	Se ele inserir um número 10 ou superior, exiba a mensagem "Muitas pessoas".
pessoas = int(input('Quantas pessoas deseja convidar? '))
if pessoas < 10:
    for i in range(pessoas):
        nomes = input('Qual o nome da {}° pessoa? '.format(i+1))
        print('{} está convidado para a festa'.format(nomes))
else:
    print('Muitas pessoas')


