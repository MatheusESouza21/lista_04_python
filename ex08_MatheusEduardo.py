#Defina uma variavel chamada "total" como 0. Peça ao ususario para inserir 5 numeros e, apos cada entrada pergunte se ele deseja que esse numero seja incluido (S ou s  N ou n). 
# Se ele desejar adicione o numero ao total. Se ele nao quiser inclui-lo nao o adicione ao total. Depois dele inserir os 5 numeros
total = 0
for i in range(5):
    num = int(input('Insira o {}° número: '.format(i+1)))
    resp = input('Deseja adicionar ao total?(S ou N): ').upper()
    if resp == 'S':
        total = total + num
print('Total: {}'.format(total))

