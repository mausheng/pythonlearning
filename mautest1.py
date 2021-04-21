class Person:   

    def __init__(self,name,weight,hp,ap):
        self.name=name
        self.weight=weight
        self.hp=hp
        self.ap=ap

    def eat(self):
        self.weight=self.weight+1

    def eat(self,volume):
        self.weight=self.weight+volume

    def exercise(self):
        self.weight=self.weight-1

    def underattack(self,who):
        self.hp=self.hp-who.ap

    def attack(self,who):
        who.hp=who.hp-self.ap
        

mausheng=Person("mausheng_chen",76,2000,100)
print(mausheng.weight)

mausheng.eat(10)
mausheng.exercise()
mausheng.exercise()
print(mausheng)
print(mausheng.name)
print(mausheng.weight)


susie=Person("susie_Su",60,1000,50)
print(susie)
print(susie.name)
print(susie.weight)
susie.exercise()
print(susie.weight)


print(mausheng.hp)
mausheng.underattack(susie)
print(mausheng.hp)


print(susie.hp)
susie.attack(mausheng)
print(mausheng)
print(susie.hp)

print(mausheng.hp)
mausheng.attack(susie)
print(susie.hp)
print(mausheng.hp)