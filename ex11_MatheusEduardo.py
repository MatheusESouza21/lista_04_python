"""
Você é um desenvolvedor de sistemas trabalhando em um projeto colaborativo com sua equipe.
Para garantir que todas as tarefas do projeto sejam concluídas dentro do prazo, você decide criar um pequeno programa para controlar o status das tarefas.
O programa deve permitir que você insira o nome de cada tarefa e indique se ela está concluída ou não.
No final, o programa deve apresentar um resumo com o total de tarefas, quantas estão concluídas e quantas ainda estão pendentes.
Desenvolva um programa em Python que:
1.	Solicite ao usuário o número de tarefas a serem inseridas.
2.	Para cada tarefa, solicite o nome da tarefa e se ela está concluída (aceitando "sim", "s", "não" ou "n").
3.	Conte e exiba o número de tarefas concluídas e não concluídas.
"""
tarefas = int(input('Número de tarefas: '))
concluidas = 0
nconcluidas = 0
for i in range(tarefas):
    nome = input('Nome da {}° tarefa: '.format(i+1))
    aceitacao = input(('Está cocluida? (sim, s ou não, n): ')).lower()
    if aceitacao == 's' or 'sim':
        concluidas = + 1
    elif aceitacao == 'n' or 'nao':
        nconcluidas = + 1   
    else:
        print('Resposta inválida')
    print('Tarefas concluídas: {} Tarefas não concluídas: {}'.format(concluidas,nconcluidas))

    
