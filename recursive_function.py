#写一个递归函数计算阶乘
#什么是阶乘
#A!=A*(A-1)*(A-2)*...*1

def recursive(x):
   if x==1:
       return 1
   return x*recursive(x-1)

if __name__=="__main__":
    print(recursive(5))