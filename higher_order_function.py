#现在有个产品的价格列表[1,2,3,4,5,6,7]
# 现在需要把价格列表中的每个元素都增加10元
# 计算价格表的总价格
# 筛选过滤低于15的元素
from functools import reduce

price = [1,2,3,4,5,6,7]
new_price=list(map(lambda i:i+10,price))#  高阶内置函数 map(普通函数,可迭代对象)
print(new_price)


def add_price(num1,num2):
    return num1+num2
## total_price=sum(new_price)
#sum内置函数
total_price=reduce(add_price,new_price)#  高阶内置函数 reduce(二元函数,迭代对象,初始值) #初始值默认为0
# total_price = reduce(lambda x,y:x+y,new_price)
print(total_price)

def real(x):
    return x >=15
real_new_price=filter (real,new_price )#  高阶内置函数 filter(普通函数,可迭代对象) #保留为Ture的元素
# real_new_price = list(filter(lambda i: i>=15,new_price ))
print(list(real_new_price ))
