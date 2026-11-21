#creating a file
# x=open("file.txt","x")
# x.write("hello")
# x.close()
#write mode-overwrites the previous content
f=open("test_file.txt","w")
f.write("how are you\n")
f.close()
#append mode-helps to add content to file
f=open("test_file.txt","a")
f.write("hi\n")
f.write("how are you\n")
f.close()
# read mode-to read from the file
f=open("test_file.txt","r")
content=f.read()
f.close()
print(content)
#with statement
with open("test_file.txt","r") as f:
    print(f.read())
