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

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = indice_tarefa - 1

    if indice_tarefa_ajustado < 0 or indice_tarefa_ajustado >= len(tarefas):
        print(f"\nTarefa '{indice_tarefa}' não encontrada.")
        input('\nPressione qualquer tecla para voltar ao menu principal.')
        return

    if tarefas[indice_tarefa_ajustado]['completada'] == True:
        print(f"\nTarefa '{indice_tarefa}' já está completada.")

        input('\nPressione qualquer tecla para voltar ao menu principal.')
        return
    
    tarefas[indice_tarefa_ajustado]['completada'] = True

    print(f"\nTarefa '{indice_tarefa}' completada com sucesso.")
    input('\nPressione qualquer tecla para voltar ao menu principal.')
    return

def deletar_tarefa_completada(tarefas, indice_tarefa):
    indice_tarefa_ajustado = indice_tarefa -1

    if indice_tarefa_ajustado < 0 or indice_tarefa_ajustado >= len(tarefas):
        print(f"\nTarefa '{indice_tarefa}' não encontrada.")
        input('\nPressione qualquer tecla para voltar ao menu principal.')
        return
    
    if tarefas[indice_tarefa_ajustado]['completada'] != True:
        print(f"\nTarefa '{indice_tarefa}' não está completada!.")

        input('\nPressione qualquer tecla para voltar ao menu principal.')
        return
    
    tarefas.remove(tarefas[indice_tarefa_ajustado])

    print(f"\nTarefa '{indice_tarefa}' deletada com sucesso.")
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
    print('5. Deletar tarefa completada')
    print('6. Sair')

    try:
        escolha = int(input('\nDigite a sua escolha: '))
    except:
        print('\nEscolha Inválida!')
        input('\nDigite qualquer tecla para voltar ao menu principal.')
        continue
        
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
        try:
            indice_tarefa = int(input('\nDigite o número da tarefa que deseja atualizar: '))
        except ValueError:
            print('\nEntrada inválida. Por favor, digite um número inteiro.')
            input('\nPressione qualquer tecla para voltar ao menu principal.')
            continue

        novo_nome = input('\nDigite o novo nome da tarefa: ')
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
    
    elif escolha == 4:
        os.system('cls')
        ver_tarefas_aux(tarefas)
        try:
            indice_tarefa = int(input('\nDigite o número da tarefa que deseja completar: '))
        except ValueError:
            print('\nEntrada inválida. Por favor, digite um número inteiro.')
            input('\nPressione qualquer tecla para voltar ao menu principal.')
            continue

        completar_tarefa(tarefas, indice_tarefa)
    
    elif escolha == 5:
        os.system('cls')
        ver_tarefas_aux(tarefas)
        try:
            indice_tarefa = int(input('\nDigite o número da tarefa que deseja deletar: '))
        except ValueError:
            print('\nEntrada inválida. Por favor, digite um número inteiro.')
            input('\nPressione qualquer tecla para voltar ao menu principal.')
            continue
        
        deletar_tarefa_completada(tarefas, indice_tarefa)

    elif escolha == 6:
        print('\nPrograma finalizado.')
        break

    else:
        print('\nEscolha inválida.')
        input('\nPressione qualquer tecla para voltar ao menu principal.')


 