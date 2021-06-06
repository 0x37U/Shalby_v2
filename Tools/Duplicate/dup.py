Input = input("Enter Your list > ").strip()

InputText= open(f"{Input}","r").read().split("\n")

SET = sorted(set(InputText))

OUT = input("Enter Your Save list > ").strip()

OutText = open(f"Results\{OUT}","w")

for _Out in SET:

    OutText.write(_Out+"\n")
    
    print(_Out)
print(f"<======= Check \"Results\{OUT}\" File =======>")
OutText.close()