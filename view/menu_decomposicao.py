import os
from shared.shared_service import get_material_selecionado
from view.header import exibe_header

def exibe_menu_decomposicao():
    os.system('clear')

    material = get_material_selecionado()
    exibe_header(f"DECOMPOSIÇÃO — {material['nome'].upper()}")
    print(f"\n Informação: {material['descricao']}")
    print(f"\n Tempo de decomposição: {material['tempo']}")

    tempo_em_anos = input("\n Digite o tempo em anos: ")
    
    
    
    
    
    