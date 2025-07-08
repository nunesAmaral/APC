import os
import time
from constants.materiais import materiais_info
from shared.shared_service import set_material_selecionado
from view.header import exibe_header
from view.lixeira import exibe_lixeira
from view.menu_decomposicao import exibe_menu_decomposicao


def exibe_menu_materiais():
    os.system('clear')

    exibe_header("BEM-VINDO AO SIMULADOR DE DEGRADAÇÃO DE LIXO")
    exibe_lixeira()

    for idx, mtrl in enumerate(materiais_info):
        print(f'{idx+1} - {mtrl["nome"]}')  
        
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
    print(selecionado)
    set_material_selecionado(selecionado)
    
    while True:
        continua = exibe_menu_decomposicao()
        if not continua: 
            break
        else:
            exibe_menu_materiais()

    time.sleep(2)







