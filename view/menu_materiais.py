import os
import time
from constants.materiais import materiais_info
from shared.shared_service import set_material_selecionado
from view.header import exibe_header
from view.lixeira import exibe_lixeira
from view.menu_decomposicao import exibe_menu_decomposicao


def exibe_itens():
    """
    OBJETIVO: dividir menu em duas colunas.
    PASSOS: 
    pega a metade do array pela divisão inteira do len para dividir a lista em duas.
    até a metade da lista, valida para não lançar IndexError. Se o index for menor, exibe as duas colunas. Senão, o item será exibido sozinho à esquerda.
    """
    meio = (len(materiais_info) + 1) // 2 
    col_esquerda =  materiais_info[:meio]
    col_direita = materiais_info[meio:]
    
    
    for i in range(meio):
        nome_item_esquerda = col_esquerda[i]['nome']
        posicao_item_esquerda = i + 1
        
        if i < len(col_direita):
            nome_item_direita = col_direita[i]['nome']
            posicao_item_direita = meio + i + 1
            
            print(f'{posicao_item_esquerda} - {nome_item_esquerda:30} {posicao_item_direita} - {nome_item_direita}')
        else:
            print(f'{posicao_item_esquerda} - {nome_item_esquerda}')


def exibe_menu_materiais():
    os.system('clear')
    
    exibe_header("BEM-VINDO AO SIMULADOR DE DEGRADAÇÃO DE LIXO")
    print("\n" * 3)
    exibe_itens()
    exibe_lixeira()
    

            
    opcao_selecionada = input("Digite a opção: ")

    while True:
        try:
            indice = int(opcao_selecionada) - 1
            if 0 <= indice < len(materiais_info):
                break
            else:
                print("Opção inválida. Favor digite uma opção enumerada acima.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

        opcao_selecionada = input("Digite a opção: ")

    selecionado = materiais_info[indice]

    set_material_selecionado(selecionado)
    
    while True:
        continua = exibe_menu_decomposicao()
        if not continua: 
            break
        else:
            exibe_menu_materiais()

    time.sleep(2)







