import os 
from view.menu_materiais import exibe_menu_materiais
from view.header import exibe_titulo

# limpa prompt (linux apenass)
os.system('clear')

exibe_titulo()
exibe_menu_materiais()


