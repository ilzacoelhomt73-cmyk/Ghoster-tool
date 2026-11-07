import sys
import time
import os
import subprocess

RESET = "\033[0m"

PRETO = "\033[30m"
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
ROXO = "\033[35m"
CIANO = "\033[36m"
BRANCO = "\033[37m"

PRETO_B = "\033[90m"
VERMELHO_B = "\033[91m"
VERDE_B = "\033[92m"
AMARELO_B = "\033[93m"
AZUL_B = "\033[94m"
ROXO_B = "\033[95m"
CIANO_B = "\033[96m"
BRANCO_B = "\033[97m"


comando_kahoot_termux = (
    "pkg update -y && "
    "pkg upgrade -y && "
    "pkg install -y git python python-pip nodejs npm && "
    "python -m pip install pystyle colorama && "
    "git clone https://github.com/CPScript/Kitty-Tools && "
    "cd Kitty-Tools && "
    "python main.py"
)


comando_kahoot_debian = (
    "sudo apt update -y && "
    "sudo apt upgrade -y && "
    "sudo apt install -y git python3-pip nodejs npm && "
    "python3 -m pip install --break-system-packages pystyle colorama && "
    "git clone https://github.com/CPScript/Kitty-Tools && "
    "cd Kitty-Tools && python3 main.py"
)


def banner():
    print(VERDE + fr"""

   ________               __                ______            __
  / ____/ /_  ____  _____/ /____  _____    /_  __/___  ____  / /
 / / __/ __ \/ __ \/ ___/ __/ _ \/ ___/_____/ / / __ \/ __ \/ /
/ /_/ / / / / /_/ (__  ) /_/  __/ /  /_____/ / / /_/ / /_/ / /
\____/_/ /_/\____/____/\__/\___/_/        /_/  \____/\____/_/

              {RESET}[ + ] CRIADO POR ARTHUR [ + ]{RESET}

          """ + RESET)


def escrever(texto, limite=0.02):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(limite)


def clear():
    os.system("clear")

# o script foi feito pra suportar apenas termux e debian


def get_system():
    if "com.termux" in os.environ.get("PREFIX", ""):
        return "termux"

    else:
        return "debian"


def menu():

    sistema = get_system()

    escrever(f"[ 1 ] {VERDE}FERRAMENTAS PARA KAHOOT{RESET}\n")
    escrever(f"[ 2 ] {VERDE}FERRAMENTAS DDOS{RESET}\n")

    escolha = input(f"\n[ + ] {VERDE}Escolha uma opção{RESET} : ")

    if escolha == "1":
        clear()
        banner()
        escrever(f"[ 1 ] {VERDE}Kitty Tools{RESET}\n", 0.01)
        escrever(f"[ 2 ] {VERDE}Buscar Quizid{RESET}\n", 0.01)
        escrever(f"[ 3 ] {VERDE}Pegar Respostas{RESET}\n", 0.01)
        escrever(f"[ 4 ] {VERDE}Adiconar Bots{RESET}\n", 0.01)

        escolha_kahoot = input(f"\n[ + ]{VERDE} Escolha uma opção{RESET} : ")

        if escolha_kahoot == "1" and sistema == "termux":
            escrever("[ + ] Instalando Kitty-Tools Para Termux\n")
            subprocess.run(comando_kahoot_termux, shell=True)

        elif escolha_kahoot == "1" and sistema == "debian":
            escrever("[ + ] Instalando Kitty-Tools Para Debian\n")
            subprocess.run(comando_kahoot_debian, shell=True)

        elif escolha_kahoot == "2":
            subprocess.run(
                [sys.executable, "scripts/buscar_uuid.py"])

        elif escolha_kahoot == "3":
            escrever("[ + ] Abrindo site de respostas\n")
            subprocess.run([
                "xdg-open",
                "https://quizonator.com/en/platforms/kahoot#answers"
            ])

        elif escolha_kahoot == "4":
            escrever("[ + ] Abrindo site de bots\n")
            subprocess.run([
                "xdg-open",
                "https://quizflood.xyz/"
            ]) 

        else:
            escrever("[ - ] opção invalida\n", 0.01)

    
    elif escolha == "2":
        clear()
        banner()
        escrever(f"[ 1 ] {VERDE}DDoS Ripper{RESET}\n")
        escrever(f"[ 2 ] {VERDE}Gamkers-DDos{RESET}\n")

        
        
        escolha_ddos = input(f"\n[ + ]{VERDE} Escolha uma opção{RESET} : ")

        if escolha_ddos == "1":
            escrever("[ + ] Instalando DDos ripper\n")
            subprocess.run(["git", "clone", "https://github.com/palahsu/DDoS-Ripper.git"])
            
            subprocess.run([sys.executable, "DRipper.py"], cwd="DDoS-Ripper", check=True)

        elif escolha_ddos == "2":
            escrever("[ + ] Instalando Gamkers-DDos\n")
            subprocess.run(["git", "clone", "https://github.com/gamkers/GAMKERS-DDOS.git"])

            subprocess.run(["python2", "GAMKERS-DDOS.py"], cwd="GAMKERS-DDOS", check=True)



    else:
        escrever("[ - ] opção invalida\n", 0.01)


clear()
banner()
menu()
