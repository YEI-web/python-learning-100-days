#对除法运算的代码进行异常处理
try:
    num1=float (input("请输入一个被除数："))
    num2=float (input("请输入一个除数"))
    result=num1/num2
except ZeroDivisionError:
    print("除数不能为0")
except ValueError:
    print("输入的不是数字")
except Exception as e:
    print("发生了未知错误:",e)
else:
    print("结果为:",result)
finally:
    print("程序结束")
