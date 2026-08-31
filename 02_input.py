# 消费满100元打9折
# 客户输入消费多少元
# 判断是否满足打折条件，并输出最后价格


op=Original_price=float(input("请输入原价:"))
sp=Special_price=op*0.9

if op>=100:
    print("实际付价：",sp)
else :
    print("实际付价：",op)
