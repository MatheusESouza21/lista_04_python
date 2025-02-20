#Peça ao ususario para inserir um numero que deseja a tabuada e em seguida exibir a tabuada para o número
num = int(input('Digite um número: '))
i = 1
for i in range(11):
    x = num * i
    print('{} x {} = {}'.format(num,i,x))