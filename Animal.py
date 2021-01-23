# _*_ coding: utf-8 _*_
# @Time : 2021/1/23 0023 下午 16:55
# @Author : jiangyiyi

# 比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
# 创建子类【猫】，继承【动物类】，
# 重写父类的__init__方法，继承父类的属性，
# 添加一个新的属性，毛发 = 短毛，
# 添加一个新的方法， 会捉老鼠，
# 重写父类的【会叫】的方法，改成【喵喵叫】

class Animal:
    # 属性
    name = 'Alice'
    colour = 'orange'
    age = 3
    gender = 'female'

    def __init__(self):
        self.leg = '小短腿'

    # 方法
    def call(self):
        print('我会叫')

    def run(self):
        print('我会跑')

class Cat(Animal):
    def __init__(self):
        self.hair = '短毛'

    def catch(self):
        print('会捉老鼠')

    def call(self):
        # Animal().call()  # 调用父类
        super(Cat, self).call()
        print('喵喵叫')

if __name__ == '__main__':
    cat_animal = Animal()
    # Cat_Animal = Cat()
    # cat_animal.call()
    # cat_animal.run()
    print('我的名字：',cat_animal.name)
    print('我的年龄：',cat_animal.age)
    print('我喜欢的颜色：',cat_animal.colour)
    print('我的性别：',cat_animal.gender)
    # Cat_Animal.catch()
    # Cat_Animal.call()