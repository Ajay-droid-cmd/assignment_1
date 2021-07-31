x= input("Enter a String : ")
d= {"Uppercase":0,"Lowercase":0}
for i in x:
    if i.isupper():
        d["Uppercase"]+=1
    elif i.islower():
         d["Lowercase"]+=1
    else:
        pass

print ("NO OF UPPERCASE IS :", d["Uppercase"])
print ("NO OF LOWERCASE IS :", d["Lowercase"])