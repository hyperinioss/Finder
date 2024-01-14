print("""
 ██▓ ██▓███       █████▒██▓ ███▄    █ ▓█████▄ ▓█████  ██▀███  
▓██▒▓██░  ██▒   ▓██   ▒▓██▒ ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
▒██▒▓██░ ██▓▒   ▒████ ░▒██▒▓██  ▀█ ██▒░██   █▌▒███   ▓██ ░▄█ ▒
░██░▒██▄█▓▒ ▒   ░▓█▒  ░░██░▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
░██░▒██▒ ░  ░   ░▒█░   ░██░▒██░   ▓██░░▒████▓ ░▒████▒░██▓ ▒██▒
░▓  ▒▓▒░ ░  ░    ▒ ░   ░▓  ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░░▒ ░         ░      ▒ ░░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
 ▒ ░░░           ░ ░    ▒ ░   ░   ░ ░  ░ ░  ░    ░     ░░   ░ 
 ░                      ░           ░    ░       ░  ░   ░     
                                       ░                      


""")


print("""Copyright By Hyperinios
      
      İnstagram: hyperinioss
      Telegram: byhyperinios
      
      """)




import socket

def ip_bulucu():
    hedef_url = input("Hedef URL'yi girin: ")
    ip_adresi = socket.gethostbyname(hedef_url)
    print("Hedefin IP adresi:", ip_adresi)

ip_bulucu()