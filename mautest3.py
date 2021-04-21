class Engine:
    def __init__(self,cc):
        self.cc=cc

class Wheel:
    def __init__(self,size):
        self.size =size


class Car:
    def __init__(self,name,cc,size):
        self.name=name
        self.engine=Engine(cc)
        self.right_Front=Wheel(size)
        self.left_Front=Wheel(size)
        self.right_back=Wheel(size)
        self.left_back=Wheel(size)


mycar=Car("toyota",2400,70)
print(mycar.name)
print(mycar.engine.cc)
print(mycar.right_Front.size)
print(mycar.left_Front.size)
print(mycar.right_back.size)  
print(mycar.left_back.size)

