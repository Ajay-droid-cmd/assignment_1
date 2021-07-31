#Write a Python program to create the multiplication table (from 1 to  10) of a number
print ("TABLES from 1 to 10")
num=10;
for i in range(1,11):
    print ("\n\n Multiplication Table For %d\n"%(i))
    for j in range (1,11):
        print ("%5d  X  %5d = %5d"%(i,j,i*j))


                 