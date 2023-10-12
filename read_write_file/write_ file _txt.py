# save file in specific folder
# fw=open("D:\\Testfile\\text1.file","w")
# fw.write("this is file ")
# fw.close()


# fw=open("D:\\Testfile\\text2.file","w")
# l=[10,20,30,40,50,500,600,700]
# for text in l:
#     fw.write(str(text)+'\n')
# fw.close()


fw=open("D:\\Testfile\\text2.file","a")
l=[10,20,30,40,50,500,600,700]
for text in l:
    fw.write(str(text)+'\n')
fw.close()

