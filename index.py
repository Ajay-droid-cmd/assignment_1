print("hello world!")
msg =("It works!")
print(msg)
#Write a Python program that accepts a word from the user and reverse it
x=input('Enter a String:')
y=x[::-1] #splice operator reverses the string (-1) so reverse it
print(y)
#Generate a Fibonacci Series for 20 numbers.
print("Fibonacci series for 20 numbers")
num = 20;
n1, n2 = 0 ,1
count = 0;
while  (count < num):
 print(n1)
 count += 1
 temp = n1+n2   
 n1=n2
 n2=temp  
# Write a Python program to construct the following pattern, using a nested loop number
print ("pattern")
num =5
for i in range(num+1):
    for j in range(i):
        print(i,end = " ")

    print (" ")    