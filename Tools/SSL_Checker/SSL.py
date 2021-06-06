import requests

from colorama import Fore

from colorama import init

print("\t\t You must put http:// or https:// To Sites")
init(autoreset=True)
Input = input("Enter Your Sites list > ").strip()

urls = open(Input,"r").read().split("\n")

a = open("Results\SSL.txt","a")

def SSL(links):

    global a

    global urls

    try:

        rep = links.replace("https://","http://")

        req = requests.get(rep)

        a.write(req.url+"\n")

        print(Fore.GREEN + f"[GOOD] {req.url}")
        
    except:
        print(Fore.RED + f"[BAD] {links}")
    
for i in urls:
    SSL(i)
print("<======= Check \"Results\SSL.txt\" File =======>")
a.close()