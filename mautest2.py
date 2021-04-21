class Head:
    def __init__(self,size):
        self.size=size

class Body:
    def __init__(self,capacity):
        self.capacity=capacity

class Hand:
    def __init__(self,length):
        self.length=length

class Leg:
    def __init__(self,width):
        self.width=width

class People:
    def __init__(self):
        self.head=None
        self.body=None
        self.right_hand=None
        self.left_hand=None
        self.right_leg=None
        self.left_leg=None

mausheng=People()
mausheng.head=Head(30)
mausheng.body=Body(3000)
mausheng.right_hand=Hand(30)
mausheng.left_hand=Hand(30)
mausheng.right_leg=Leg(100)
mausheng.left_leg=Leg(100)

print(mausheng.head.size)
print(mausheng.body.capacity)
print(mausheng.right_hand.length)
print(mausheng.left_hand.length)
print(mausheng.right_leg.width)
print(mausheng.left_leg.width)


susie=People()
susie.head=Head(20)
susie.body=Body(2000)
susie.right_hand=Hand(20)
susie.left_hand=Hand(20)
susie.right_leg=Leg(50)
susie.left_leg=Leg(50)


print(susie.head.size)
print(susie.body.capacity)
print(susie.right_hand.length)
print(susie.left_hand.length)
print(susie.right_leg.width)
print(susie.left_leg.width)

swap =mausheng
mausheng=susie
susie=swap

print(mausheng.head.size)
print(mausheng.body.capacity)
print(mausheng.right_hand.length)
print(mausheng.left_hand.length)
print(mausheng.right_leg.width)
print(mausheng.left_leg.width)

print(susie.head.size)
print(susie.body.capacity)
print(susie.right_hand.length)
print(susie.left_hand.length)
print(susie.right_leg.width)
print(susie.left_leg.width)
    