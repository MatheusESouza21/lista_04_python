#Faça um programa que solicite ao usuario para digitar o seu nome e um numero qualquer e em seguida exiba seu nome varias vezes de acordo com o numero que ele digitou
nome = input('Digite seu nome: ')
n = int(input('Digite um número: '))
for i in range(n):
    print(nome)