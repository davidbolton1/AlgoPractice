#Classes and Objects
#Inheritance
#Encapsulation
#Polymorphism
#Abstraction

#Inheritance in OOP means that a class takes over characteristics from it's parents





#Encapsulation is a process in which we enclose our values, gathering all data and methods in one place
#Encapsulation bundles a bunch of things inside a class
class Empoyee: 
    def __init__(self, name, project):
        self.name = name
        self.project = project
    
    def work(self):
        print(self.name, 'is working on', self.project)

class Employee:
    # constructor
    def __init__(self, name, salary, project):
        # data members
        self.name = name
        self.salary = salary
        self.project = project

    # method
    # to display employee's details
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

    # method
    def work(self):
        print(self.name, 'is working on', self.project)

# creating object of a class
emp = Employee('Jessa', 8000, 'NLP')

# calling public method of the class
emp.show()
emp.work()

#Polymorphism is a process that defines multiple ways to perform a single action(Run time and compile-time)
#Abstraction is when we hide system details or complexities from end users. When we abstract class, it can't have any objects. This class just provides functions for other classes to inherit. 



#