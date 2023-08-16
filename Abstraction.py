from abc import ABC,abstractclassmethod

class Parent(ABC):

    @abstractclassmethod
    def pqr(self):
        pass

class Child(Parent):

    def pqr(self):
        print("Abdullah al shahriar")

obj = Child()
obj.pqr()