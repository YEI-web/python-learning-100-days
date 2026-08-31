#打开并读取test文件夹下面的demo文档

with open(r".\test\demo","r",encoding="utf-8") as file:
    print(file.read())
