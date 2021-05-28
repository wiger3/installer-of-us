import requests
from http.client import responses
import os
import sys
import shutil
import zipfile
from colorama import init, Fore, Style
init()

print(f"\
{Fore.YELLOW}=====================\n\
Town of Us Instalator\n\
====================={Style.RESET_ALL}\n\
Wybierz wersje gry:")

gamever = ["2021.5.25e (Epic Games)", "2021.5.10s", "2021.4.14s", "2021.4.12s", "2021.3.31.3s", "2021.3.5s"]
for i in range(0, len(gamever)):
    print(f"{i + 1}. {gamever[i]}")

modver = ["2.0.5", "2.0.4", "2.0.2", "2.0.2", "2.0.0", "1.2.0"]
epic = False
while True: # do ..
    try: version = int(input("Wersja gry: ")) - 1
    except: pass
    if 0 <= version < len(modver): # .. while
        break
    else:
        print(f"{Fore.RED}Niepoprawna wersja: {str(version + 1)}{Style.RESET_ALL}")
if version == 0:
    print(f"{Fore.CYAN}Eksperymentalny tryb Epic Games Launcher wlaczony!{Style.RESET_ALL}")
    epic = True
while True:
    susdir = os.path.abspath(input("Folder gry: ").replace('"', ''))
    if os.path.isfile(f"{susdir}\\Among Us.exe"):
        break
    else:
        print(f"{Fore.RED}Folder nie zawiera Among Us: {susdir}{Style.RESET_ALL}")

if epic:
    link = "https://github.com/wiger3/installer-of-us/raw/epic/TownOfUs-v2.0.4-EPIC.zip"
else:
    link = "https://github.com/slushiegoose/Town-Of-Us/releases/download/v{0}/TownOfUs-v{0}.zip".format(modver[version])
print()

print(f"{Fore.GREEN}Pobieranie z: {link}{Style.RESET_ALL}")
try:
    r = requests.get(link, allow_redirects=True)
    if not r:
        print(f"{Fore.RED}Wystapil blad HTTP: {r.status_code} ({responses[r.status_code]}).{Style.RESET_ALL}")
        raise requests.HTTPError
except:
    print(f"{Fore.RED}Nie mozna pobrac pliku. Sprawdz polaczenie sieciowe{Style.RESET_ALL}")
    input()
    sys.exit(2)
try: open('townofsus.zip', 'wb').write(r.content)
except:
    print(f"{Fore.RED}Nie mozna pobrac pliku. Uruchom jako administrator{Style.RESET_ALL}")
    input()
    sys.exit(1)

if epic:
    moddir = susdir
else:
    moddir = os.path.abspath(f"{susdir}\\..\\Town of Us")
    print(f"{Fore.GREEN}Tworzenie folderu: {moddir}{Style.RESET_ALL}")
    try: shutil.copytree(susdir, moddir)
    except FileExistsError:
        shutil.rmtree(moddir)
        shutil.copytree(susdir, moddir)
    except:
        print(f"{Fore.RED}Nie mozna utworzyc folderu. Uruchom jako administrator{Style.RESET_ALL}")
        input()
        sys.exit(1)

print(f"{Fore.GREEN}Instalowanie moda w folderze..{Style.RESET_ALL}")
with zipfile.ZipFile("townofsus.zip", 'r') as suszip:
    try: suszip.extractall(moddir)
    except:
        print(f"{Fore.RED}Nie mozna zainstalowac moda. Uruchom jako administrator{Style.RESET_ALL}")
        input()
        sys.exit(1)

try: os.remove("townofsus.zip")
except: pass
print()
print(f"{Fore.YELLOW}Zainstalowano Town of Us w folderze: {moddir}!{Style.RESET_ALL}")
print(f"{Fore.YELLOW}Nacisnij Enter, aby uruchomic gre..{Style.RESET_ALL}")
input()
if epic:
    os.startfile("com.epicgames.launcher://apps/963137e4c29d4c79a81323b8fab03a40?action=launch&silent=true")
else:
    os.startfile(f"{moddir}\\Among Us.exe")