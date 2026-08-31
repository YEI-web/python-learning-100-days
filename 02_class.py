#定义一个父类:Flower
#在flower类中的属性有 花的名字
#flower中的方法有 开花(bloom)和凋谢(wither)
#定义一个子类:Sunflower
#在Sunflower类中的属性有 花的名字 和颜色 和 朝哪个方向(direction)开花
#sunflower中的方法有 向日葵向哪边开(bloom_towards_sun)

class Flower:
    def __init__(self,name):
        self.name = name
    def bloom(self):
        print(f"{self.name}开花了")
    def wither(self):
        print(f"{self.name}凋谢了")


class SunFlower(Flower):
    def __init__(self,name,color,direction):
        super().__init__(name)
        self.color = color
        self.direction = direction
    def bloom_towards_sun(self):
        print("向日葵向{}开花".format(self.direction))

if __name__ == "__main__":
    little_sun=SunFlower("little_sun",'yellow','southeast')
    little_sun.bloom_towards_sun()
