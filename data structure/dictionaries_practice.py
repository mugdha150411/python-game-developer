#Count the occurrence of each vowel in the sentence given as input by the user.
d={"a":0,"e":0,"i":0,"o":0,"u":0}
s=input("enter a sentence: ").lower()
for i in s:
    if i in d:
        d[i]+=1
print(d)
#Count the occurrence of each alphabet that occurs in the sentence given as input by the user.
d={}
s=input("enter a sentence: ")
for i in s:
    if i.isalpha():
        if i in d:
            d[i]+=1
        else:
            d[i]=1
print(d)
/Users/mugdhagoel/Desktop/mugdha jet learn projects/python game developer/data_structure