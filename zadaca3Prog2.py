import re

regex1 = "^t"
regex2 = "p$"
regex3 = "[0-5]"
regex4 = "\s"

unos = input("Unos:")

prvo = re.findall(regex1, unos)
if not prvo:
    print("Niste unijeli prvo slovo točno")

zadnje = re.findall(regex2, unos)
if not zadnje:
    print("Niste unijeli zadnje slovo točno")

broj = re.findall(regex3, unos)
if not broj:
    print("Niste unijeli broj od 1 do 5.")

razmak = re.findall(regex4, unos)
if not razmak:
    print("Niste unijeli razmak.")

if prvo and zadnje and broj and razmak:
    print("Ispravan unos.")

