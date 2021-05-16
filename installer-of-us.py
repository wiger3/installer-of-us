import requests
import os
import shutil
import zipfile
from colorama import init, Fore, Style
init()

print(f"\
{Fore.YELLOW}=====================\n\
Town of Us Installator\n\
====================={Style.RESET_ALL}\n\
Select game version:\n\
1. 2021.5.10s\n\
2. 2021.4.14s\n\
3. 2021.4.12s\n\
4. 2021.3.31.3s\n\
5. 2021.3.5s\n\
")

while True: # do ..
    version = int(input("Game version: ")) - 1
    if 0 < version < 5: # .. while
        break
    else:
        print(f"{Fore.RED}Invalid version: {str(version + 1)}{Style.RESET_ALL}")
while True:
    susdir = input("Folder gry: ")
    if os.path.isfile(f"{susdir}\\Among Us.exe"):
        break
    else:
        print(f"{Fore.RED}Directory doesn't contain Among Us: {susdir}{Style.RESET_ALL}")

modver = ["2.0.4", "2.0.2", "2.0.2", "2.0.0", "1.2.0"]
link = "https://github.com/slushiegoose/Town-Of-Us/releases/download/v{0}/TownOfUs-v{0}.zip".format(modver[version])
print()

print(f"{Fore.GREEN}Downloading from: {link}{Style.RESET_ALL}")
r = requests.get(link, allow_redirects=True)
open('townofsus.zip', 'wb').write(r.content)

moddir = f"{susdir}\\..\\Town of Us"
print(f"{Fore.GREEN}Creating directory: {moddir}{Style.RESET_ALL}")
shutil.copytree(susdir, moddir)

print(f"{Fore.GREEN}Installing mod in directory..{Style.RESET_ALL}")
with zipfile.ZipFile("townofsus.zip", 'r') as suszip:
    suszip.extractall(moddir)

os.remove("townofsus.zip")
print()
print(f"{Fore.YELLOW}Town of Us installed in folder: {moddir}!{Style.RESET_ALL}")
input(f"{Fore.YELLOW}Press Enter, to open the game..{Style.RESET_ALL}")
os.startfile(f"{moddir}\\Among Us.exe")