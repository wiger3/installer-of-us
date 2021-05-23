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
Town of Us Installer\n\
====================={Style.RESET_ALL}\n\
Select game version:")

gamever = ["2021.5.10s", "2021.4.14s", "2021.4.12s", "2021.3.31.3s", "2021.3.5s"]
for i in range(0, len(gamever)):
    print(f"{i + 1}. {gamever[i]}")

modver = ["2.0.4", "2.0.2", "2.0.2", "2.0.0", "1.2.0"]
while True: # do ..
    try: version = int(input("Game version: ")) - 1
    except: pass
    if 0 <= version < len(modver): # .. while
        break
    else:
        print(f"{Fore.RED}Invalid version: {str(version + 1)}{Style.RESET_ALL}")
while True:
    susdir = os.path.abspath(input("Game directory: ").replace('"', ''))
    if os.path.isfile(f"{susdir}\\Among Us.exe"):
        break
    else:
        print(f"{Fore.RED}Directory doesn't contain Among Us: {susdir}{Style.RESET_ALL}")

link = "https://github.com/slushiegoose/Town-Of-Us/releases/download/v{0}/TownOfUs-v{0}.zip".format(modver[version])
print()

print(f"{Fore.GREEN}Downloading from: {link}{Style.RESET_ALL}")
try:
    r = requests.get(link, allow_redirects=True)
    if not r:
        print(f"{Fore.RED}HTTP Error occured: {r.status_code} ({responses[r.status_code]}).{Style.RESET_ALL}")
        raise requests.HTTPError
except:
    print(f"{Fore.RED}Couldn't download file. Please check internet connection{Style.RESET_ALL}")
    input()
    sys.exit(2)
try: open('townofsus.zip', 'wb').write(r.content)
except:
    print(f"{Fore.RED}Couldn't download file. Please run as administrator{Style.RESET_ALL}")
    input()
    sys.exit(1)

moddir = os.path.abspath(f"{susdir}\\..\\Town of Us")
print(f"{Fore.GREEN}Creating directory: {moddir}{Style.RESET_ALL}")
try: shutil.copytree(susdir, moddir)
except FileExistsError:
    shutil.rmtree(moddir)
    shutil.copytree(susdir, moddir)
except:
    print(f"{Fore.RED}Couldn't create directory. Please run as administrator{Style.RESET_ALL}")
    input()
    sys.exit(1)

print(f"{Fore.GREEN}Installing mod in directory..{Style.RESET_ALL}")
with zipfile.ZipFile("townofsus.zip", 'r') as suszip:
    try: suszip.extractall(moddir)
    except:
        print(f"{Fore.RED}Couldn't install mod. Please run as administrator.{Style.RESET_ALL}")
        input()
        sys.exit(1)

try: os.remove("townofsus.zip")
except: pass
print()
print(f"{Fore.YELLOW}Town of Us installed in folder: {moddir}!{Style.RESET_ALL}")
print(f"{Fore.YELLOW}Press Enter, to open the game..{Style.RESET_ALL}")
input()
os.startfile(f"{moddir}\\Among Us.exe")