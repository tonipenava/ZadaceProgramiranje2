import re

regex= r"^(\w|\.|\_|\-|[0-9])+[@][fpmoz.sum.ba]+\Z$"
fpmoz="fpmoz.sum.ba"
email=input("Unesite mail: ")

if (re.search(regex, email)):
    print("Valid Email")

else:
    print("Invalid Email")

regex2=r"^(\w|\.|\_|\-|[0-9])+[@][sum.ba]+\Z$"
eduid = input("Unesi eduid:")
if (re.search(regex2, eduid)):
    print("Valid Eduid")
else:
    print("Invalid Eduid")