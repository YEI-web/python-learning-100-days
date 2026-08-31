# 定义1个狗类:
# 1.每个狗对象有独立,品种(style),年龄(age),颜色(color)
#2.每个狗对象都有独立的方法:
#             1.打印当前狗对象的品种(get_style())
#             2.打印当前狗对象的年龄(get_age())
#             3.打印当前狗对象的颜色(get_color())
# 1.实例化一条‘拉布拉多’2岁 黄色的狗,调用所有实例方法


class Dog:
    def __init__(self,style,age,color):
        self.style = style
        self.age = age
        self.color = color
    def get_style(self):
        print(f"当前狗的品种为{self.style}")
    def get_age(self):
        print(f"当前狗的年龄为{self.age}")
    def get_color(self):
        print("当前狗的颜色为%s"%self.color)
dog1=Dog("拉布拉多","2岁","黄色")
dog2=Dog("金毛","3岁","黄色")
dog1.get_style()
dog1.get_color()
dog1.get_age()
dog2.get_style()
dog2.get_color()
dog2.get_age()
