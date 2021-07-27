# my_file=open("new.txt","r")
# i=0
# while i<(my_file):
#     my_file.write(my_file[i])
#     my_file.write("\n")
#     i=i+1
# my_file.close()

banks_list=open("new.txt","r")
for i in banks_list:
    print(i)
banks_list.close()