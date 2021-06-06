import os
try:
    import requests
    from colorama import Fore
    from colorama import init
    init(autoreset=True)
except:
    os.system("pip install requests")
    os.system("pip install colorama")
    os.system("main.py")


os.system("title [+] Shalby V2 - 0x37U [+]")
try:
    os.system("cls")
except:
    os.system("clear")
def banner():
    
    print(Fore.RED+"\t\t ██████╗ ██╗  ██╗██████╗ ███████╗██╗   ██╗")
    print(Fore.RED+"\t\t██╔═████╗╚██╗██╔╝╚════██╗╚════██║██║   ██║")
    print("\t\t██║██╔██║ ╚███╔╝  █████╔╝    ██╔╝██║   ██║")
    print("\t\t████╔╝██║ ██╔██╗  ╚═══██╗   ██╔╝ ██║   ██║")
    print(Fore.GREEN+"\t\t╚██████╔╝██╔╝ ██╗██████╔╝   ██║  ╚██████╔╝")
    print(Fore.GREEN+"\t\t ╚═════╝ ╚═╝  ╚═╝╚═════╝    ╚═╝   ╚═════╝ ")

    print(f"\n\t\tGitHub : github.com/{Fore.LIGHTCYAN_EX}0x37U")
banner()

choice = """
[1] Domain To iP
[2] Sites Grabber (Not Public)
[3] SSL Checker
[4] info Grabber
[5] Delete Duplicate With Sort
[6] Bin Checker
"""

print(choice)
Scripts = input("\tTool > ").strip()

if Scripts == "1":
    os.system("Tools\\reverser\domaintoip.py")
elif Scripts == "2":
    os.system("Tools\grab\grab.py")
elif Scripts == "3":
    os.system("Tools\SSL_Checker\SSL.py")
elif Scripts == "4":
    os.system("Tools\info\info.py")
elif Scripts == "5":
    os.system("Tools\Duplicate\dup.py")
elif Scripts == "6":
    os.system("Tools\Bin\\bin.py")
else:
    print("Tool Number Not Found")