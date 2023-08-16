'''class Employees(): 
   def __init__(self, Name, Salary): 
       self.Name = Name
       self.Salary = Salary
 
   def details(self):
       
    print("Employee Name : ", self.Name)
    print("Employee Salary: ", self.Salary)
    print("\n")
 
first = Employees("Abdullah", 10000) 
second = Employees("RaseL", 20000)
third = Employees("Shahriar", 10000)
fourth = Employees("Setu", 30000)
fifth = Employees("Esha", 50000)
 
first.details() 
second.details() 
third.details()
fourth.details()
fifth.details()'''

'''class mainclass:
   def chclass(self, name, age):
      print(f"My name is {name}, My Age is {age}")


a= mainclass()

a.chclass("RaseL",20)
a.chclass("RaseL",20)
a.chclass("RaseL",20)
a.chclass("RaseL",20)
a.chclass("RaseL",20)'''


class cons:
   def __init__(self,name, age):
      self.name = name
      self.age = age

   def rclass(self):
      print(f"My Name is  {self.name}")
      print(f"My Name is  {self.age}")
      print("\n")

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
