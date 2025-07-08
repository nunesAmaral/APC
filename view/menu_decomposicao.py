import os
import time
from shared.shared_service import get_material_selecionado
from view.header import exibe_header

def exibe_menu_decomposicao():
    os.system('clear')

    material = get_material_selecionado()
    exibe_header(f"DECOMPOSIÇÃO — {material['nome'].upper()}")
    print(f"\n Informação: {material['descricao']}")
    print(f"\n Tempo de decomposição: {material['tempo']}")
    
    tempo_em_anos = int(input("\n Digite o tempo em anos: "))
            
    if  material['tempo_anos'][0]  > tempo_em_anos:
        print(f'Em {tempo_em_anos} anos, a decomposição nem iniciou.')
    
    for i in range(tempo_em_anos + 1):
        print(f'Anos: {i}   ', end='\r')
        time.sleep(0.01)

    if material['tempo_anos'][0] <= tempo_em_anos < material['tempo_anos'][1]:
        print(f'{material["nome"]} ainda estará em decomposição!!!')

        
    if  material['tempo_anos'][1] <= tempo_em_anos:
        print(f"{material['nome']} se tornou um só com a natureza.")
        
    continuar_execucao = input('Deseja consultar outro material? (S/N) ').upper() == 'S'
    
    return continuar_execucao
            



        
    
    
    
    
    