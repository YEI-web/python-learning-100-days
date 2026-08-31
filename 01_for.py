#X=1-1/3-1/5-1/7-1/9......
n = int(input("输入一个正整数:"))
m=2
for i in range(1,n+1):
    m-=1/(2*i-1)
print("%.2f"%m)
