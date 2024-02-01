import os


def adicionar_tarefa(tarefas, nome_tarefa):
    # tarefa: nome da tarefa
    # completada: indicar se essa tarefa ja foi completada ou nao
    tarefa = { 'nome': nome_tarefa, 'completada': False }
    tarefas.append(tarefa)
    print(f"\nA tarefa '{nome_tarefa}' foi adicionada com sucesso!\n")
    input('Pressione qualquer tecla para voltar ao menu principal.')
    return

def ver_tarefas(tarefas):
    print('\nLista de tarefas:\n')

    for indice, tarefa in enumerate(tarefas, start=1):
        status = '✓' if tarefa['completada'] else ' '
        nome_tarefa = tarefa['nome']
        print(f'{indice}. [{status}] {nome_tarefa}')

    input('\nPressione qualquer tecla para voltar ao menu principal.')
    return

def ver_tarefas_aux(tarefas):
    print('\nLista de tarefas:\n')

    for indice, tarefa in enumerate(tarefas, start=1):
        status = '✓' if tarefa['completada'] else ' '
        nome_tarefa = tarefa['nome']
        print(f'{indice}. [{status}] {nome_tarefa}')

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = indice_tarefa - 1

    if indice_tarefa_ajustado < 0 or indice_tarefa_ajustado >= len(tarefas):
        print(f"\nTarefa '{indice_tarefa}' não encontrada.")
        input('\nPressione qualquer tecla para voltar ao menu principal.')
        return

    tarefas[indice_tarefa_ajustado]['nome'] = novo_nome_tarefa

    print(f"\nTarefa '{indice_tarefa}' atualizada para '{novo_nome_tarefa}'")
    input('\nPressione qualquer tecla para voltar ao menu principal.')
    return


tarefas = []

while True:
    os.system('cls')
    
    print('\nMenu do Gerenciador de Lista de Tarefas:\n')
    print('1. Adicionar tarefa')
    print('2. Ver tarefa')
    print('3. Atualizar tarefa')
    print('4. Completar tarefa')
    print('5. Deletar tarefas completadas')
    print('6. Sair')

    escolha = int(input('\nDigite a sua escolha: '))
    if escolha == 1:
        os.system('cls')
        nome_tarefa = input('\nDigite o nome da tarefa que deseja adicionar: ')
        adicionar_tarefa(tarefas, nome_tarefa)

    elif escolha == 2:
        os.system('cls')
        ver_tarefas(tarefas)

    elif escolha == 3:
        os.system('cls')
        ver_tarefas_aux(tarefas)
        indice_tarefa = int(input('\nDigite o número da tarefa que deseja atualizar: '))
        novo_nome = input('\nDigite o novo nome da tarefa: ')
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
    
    elif escolha == 6:
        print('\nPrograma finalizado.')
        break


 