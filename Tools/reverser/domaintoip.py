import socket,os

from colorama import Fore
from colorama import init
init()
def Ips(site):
    global text

    text = open("Results\\result.txt","a")
    
    try:

        if site in "http://" or "https://":

            url = site.replace("http://","").replace("https://","").replace('/', '')

        elif "/" in site:

            url = site.replace('/', '')

        _0x37U = socket.gethostbyname(url)
        text.write(_0x37U+"\n")
        print(Fore.GREEN+"[REVERSED]"+(Fore.LIGHTWHITE_EX+" >> ")+_0x37U)

    except:
        pass

Input = input("Enter Your Sites List > ").strip()  

LIST = open(Input,"r").read().rsplit("\n")

for sites in LIST:
    Ips(sites.strip())
print("<======= Check \"Results\\result.txt\" File =======>")
text.close()