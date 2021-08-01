'''
Write 4 lines of text into the file 
Read the contents from text file line by line
Append one more line in the text file.'''

print ("File menuplation")
#create and read file 
f=open("newfile.txt","w")
f.close()
# open to create a new files
# w to edit the files

# 2- to append to the text files
f=open("newfile.txt","a")
f.write("placeholder txt")
f.close()