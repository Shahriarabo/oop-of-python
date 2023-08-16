class cons:
   def __init__(self,name, age):
      self.name = name
      self.age = age

   def rclass(self):
      print(f"My Name is  {self.name}")
      print(f"My Name is  {self.age}")
      print("\n")

   @classmethod
   def mclass(cls):
       print("Hi Abdullah ")
   @staticmethod
   def staticm():
       print("This staticmethod")

f1 = cons("Abdullah",20)
f2 = cons("Abdullah",20)
f3 = cons("Abdullah",20)
f4 = cons("Abdullah",20)
f5 = cons("Abdullah",20)
f6 = cons("Abdullah",20)

f1.rclass()
f2.rclass()
f3.rclass()
f4.rclass()
f5.rclass()
f6.rclass()

f2.mclass()
f2.staticm()
cons.staticm()
cons.mclass()
class Employee:
    @staticmethod
    def sample(x):
        print('Inside static method', x)

# call static method
Employee.sample(10)

# can be called using object
emp = Employee()
emp.sample(10)