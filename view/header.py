import shutil

def exibe_header(texto):
    print("***********************************************".center(20))
    print(texto.center(20))
    print("***********************************************".center(20))
    
    
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
  
  # Calcula largura do terminal com a lib de utilitários do shell.
  largura = shutil.get_terminal_size().columns    
  
  # forma para centralizar a ASCII Art no terminal sem bagunçar a bagaça toda
  for linha in titulo.splitlines():
    print(linha.center(largura))

   
  
  # Centraliza texto conforme largura do terminal.
  texto = "PRESSIONE ENTER PARA INICIAR!!".center(largura)     
  input(texto)


                                                                                                                                           

                                                                                                                                           
