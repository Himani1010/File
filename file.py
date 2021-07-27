f=open("file.txt","w")
p=f.write("I am from Bangalore \n now I am doing Python .\n After that I will try for job.")
f.close()

f1=open("file.txt","a")
p2=f1.write("I am from Nainital , I am so lucky .")
f1.close()

new1=open("file.txt","r")
p3=new1.read()
print(p3)
c=0
for i in p3:
    if i=="\n":
        c=c+1
print(c+1)