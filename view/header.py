import shutil

# Calcula largura do terminal com a lib de utilitários do shell.
largura = shutil.get_terminal_size().columns   

def exibe_header(texto):
    # largura do menu.
    decoracao = "*"*91
    print(decoracao.center(largura))
    print(texto.center(largura))
    print(decoracao.center(largura))
    
    
def exibe_titulo():

  titulo = """
   /$$$$$$$                                                                            /$$                              
| $$__  $$                                                                          |__/                              
| $$  \ $$  /$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$   /$$$$$$   /$$$$$$$ /$$  /$$$$$$$  /$$$$$$   /$$$$$$ 
| $$  | $$ /$$__  $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$ /$$__  $$ /$$_____/| $$ /$$_____/ |____  $$ /$$__  $$
| $$  | $$| $$$$$$$$| $$      | $$  \ $$| $$ \ $$ \ $$| $$  \ $$| $$  \ $$|  $$$$$$ | $$| $$        /$$$$$$$| $$  \ $$
| $$  | $$| $$_____/| $$      | $$  | $$| $$ | $$ | $$| $$  | $$| $$  | $$ \____  $$| $$| $$       /$$__  $$| $$  | $$
| $$$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$/ /$$$$$$$/| $$|  $$$$$$$|  $$$$$$$|  $$$$$$/
|_______/  \_______/ \_______/ \______/ |__/ |__/ |__/| $$____/  \______/ |_______/ |__/ \_______/ \_______/ \______/ 
                                                      | $$                                                            
                                                      | $$                                                            
                                                      |__/  
  
  """ 
  
  # forma para centralizar a ASCII Art no terminal sem bagaçar tudo.
  for linha in titulo.splitlines():
    print(linha.center(largura))
   
  # Centraliza texto conforme largura do terminal.
  texto = "PRESSIONE ENTER PARA INICIAR!!".center(largura)     
  input(texto)


                                                                                                                                           

                                                                                                                                           
