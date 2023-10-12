# fw=open("text3.txt","w")
# fw.write("first line")
# fw.close()


# fr=open("text3.txt","r")
# print(fr.read())
# fr.close()


with open("text4","w") as fw:
    fw.write("this line is from with operation")


with open("text4","r") as fr:
    print(fr.read())
