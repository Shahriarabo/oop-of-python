class Employee:
    # constructor
    def __init__(self, name, salary, project):
        # data members
        self._name = name
        self._salary = salary
        self.__project = project

    # method
    # to display employee's details
    def show(self):
        # accessing public data member
        print("Name: ", self._name, 'Salary:', self._salary)

    # method
    def work(self):
        print(self._name, 'is working on', self.__project)

# creating object of a class
emp = Employee('Jessa', 8000, 'NLP')

# calling public method of the class
emp.show()
emp.work()



class enca:
    def __init__(self , name , age):
        self.__name = name
        self.__age = age
        print(self.__name,self.__age)

a = enca("Eash", 17)

#print(a.__name, a.__age)