import requests


bin = input("Enter Bin : ").strip()

if len(bin) >= 6:
    replaces = bin.replace("x","")
    url = f"https://lookup.binlist.net/{replaces}"
else:
    print("Try Anthor Bin")
    pass


try:
    Data = requests.get(url).json()
    Scheme = Data["scheme"]
    country = Data["country"]["name"]
    Type = Data["type"]
    brand = Data["brand"]
    bank = Data["bank"]["name"]

    print(f"Bin : {bin}")
    if "scheme" not in Data:
        pass
    else:
        print(f"SCHEME / NETWORK : {Scheme.capitalize()}")
    if "type" not in Data:
        pass
    else:
        print(f"TYPE : {Type}")
    if "brand" not in Data:
        pass
    else:
        print(f"Brand : {brand}")
    if "name" not in Data:
        pass
    else:
        print(f"County : {country}")
    if "name" not in Data:
        pass
    else:
        print(f"Bank : {bank}")

except:
    pass