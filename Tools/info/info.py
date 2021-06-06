import requests

num =  int(input("How Many Data You Want ? ").strip())

gender = input("Enter Female or Male or Enter > ").strip().lower()

Url = f"https://randomuser.me/api?results={num}&gender={gender}&password=upper,lower,12&exc=register,picture,id&nat=US"

accc = open("Results\data.txt","a")
    

def Getinfo():

    global accc
    global Url
    global num
    req = requests.get(Url).json()
    data = req["results"]
    for i in data:
            gender = i["gender"]
            frist = i["name"]['first']
            last = i["name"]['last']
            country = i["location"]["country"]
            city = i["location"]["city"]
            number = i["location"]["street"]["number"]
            street = i["location"]["street"]["name"]
            postcode = i["location"]["postcode"]
            print(f"Gender : {gender.capitalize()}")
            print(f"Name : {frist+last}")
            print(f"Email : {frist+last}@yahoo.com".lower())
            print(f"Country : {country}\nCity : {city}\nStreet : {number} {street}\nPostalcode : {postcode}")
            print("="*25)
            accc.write(f"Gender : {gender.capitalize()}\nName : {frist} {last}\nEmail : {frist.lower()}.{last.lower()}@yahoo.com\nCountry : {country}\nCity : {city}\nStreet : {number} {street}\nPostalcode : {postcode}\n================\n")
    print("<======= Check \"Results\Data.txt\" File =======>")
Getinfo()
accc.close()