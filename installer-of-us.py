import requests
import os
import shutil
import zipfile
from colorama import init, Fore, Style
init()

print(f"\
{Fore.YELLOW}=====================\n\
Town of Us Instalator\n\
====================={Style.RESET_ALL}\n\
Wybierz wersje gry:\n\
1. 2021.5.10s\n\
2. 2021.4.14s\n\
3. 2021.4.12s\n\
4. 2021.3.31.3s\n\
5. 2021.3.5s\n\
")

while True: # do ..
    version = int(input("Wersja gry: ")) - 1
    if 0 < version < 5: # .. while
        break
    else:
        print(f"{Fore.RED}Niepoprawna wersja: {str(version + 1)}{Style.RESET_ALL}")
while True:
    susdir = input("Folder gry: ")
    if os.path.isfile(f"{susdir}\\Among Us.exe"):
        break
    else:
        print(f"{Fore.RED}Folder nie zawiera Among Us: {susdir}{Style.RESET_ALL}")

modver = ["2.0.4", "2.0.2", "2.0.2", "2.0.0", "1.2.0"]
link = "https://github.com/slushiegoose/Town-Of-Us/releases/download/v{0}/TownOfUs-v{0}.zip".format(modver[version])
print()

print(f"{Fore.GREEN}Pobieranie z: {link}{Style.RESET_ALL}")
r = requests.get(link, allow_redirects=True)
open('townofsus.zip', 'wb').write(r.content)

moddir = f"{susdir}\\..\\Town of Us"
print(f"{Fore.GREEN}Tworzenie folderu: {moddir}{Style.RESET_ALL}")
shutil.copytree(susdir, moddir)

print(f"{Fore.GREEN}Instalacja modu w folderze..{Style.RESET_ALL}")
with zipfile.ZipFile("townofsus.zip", 'r') as suszip:
    suszip.extractall(moddir)

os.remove("townofsus.zip")
print()
print(f"{Fore.YELLOW}Zainstalowano Town of Us w folderze: {moddir}!{Style.RESET_ALL}")
input("Nacisnij Enter, aby otworzyc gre..")
os.startfile(f"{moddir}\\Among Us.exe")