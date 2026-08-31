#判断润年
#润年规则：
#能被4整除但不能被100整除
#或者能被400整除
#

n=int(input("输入年份判断是否为闰年："))
if n%4==0 and n%100!=0 or n%400==0:
    print("yes")
else:
    print("no")