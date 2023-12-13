"""
class parent:
    def p(self):
        print("This is parent class")
class child(parent):
    def c(self):
        print("This is child class")

pi=child()
pi.c();  pi.p()

class Car:
    def accelerate(self):
        pass
    def brake(self):
        pass

class Mercedes(Car):
    def accelerate(self):
        print("Unique acceleration smooth and powerful")
    def brake(self):
        print("Advanced braking system")

class BMW(Car):
    def accelerate(self):
        print("Dynamic acceleration fast and powerful")
    def brake(self):
        print('High performance braking')
m=Mercedes()
b=BMW()
print("\nStats of mercedes")
m.accelerate(); m.brake();
print("\nStats of BMW")
b.accelerate(); b.brake();

class SuperClass:
    def some(self):
        print('SuperClass Method')
class SubClass(SuperClass):
    def some1(self):
        super().some()
        print("SubClass Method")
o=SubClass()
o.some1();

class Employee:
    def __init__(self):
        self.salary=50000
    def increment_salary(self,perc):
        self.salary += self.salary *(perc/100)
    def display(self):
        print(f'Employee Salary: Rs {self.salary}')
class FullTimeEmployee(Employee):
    def increment_salary(self):
        super().increment_salary(50)
class InternEmployee(Employee):
    def increment_salary(self):
        super().increment_salary(25)
f=FullTimeEmployee()
i=InternEmployee()
print('\nBefore increment')
f.display(); i.display();
f.increment_salary()
i.increment_salary()
print('\nAfter increment')
f.display(); i.display();

class Base:
    def __init__(self):
        print("This is base class")
class der1(Base):
    def __init__(self):
        super().__init__()
        print("this is derived class 1")
class der2(Base):
    def __init__(self):
        super().__init__()
        print('This is derived class 2')
d1=Base()
d2=Base()

import math
class GeometryObject:
    def calculate_area(self):
        pass
class Circle(GeometryObject):
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        return math.pi*self.radius**2
class Square(GeometryObject):
    def __init__(self,side):
        self.side=side
    def calculate_area(self):
        return self.side**2
def main():
    shape_type=input("Enter the shape circle or square").lower()
    if shape_type=='circle':
        radius=float(input('Enter radius of circle:'))
        c=Circle(radius)
        area=c.calculate_area()
        print(f'Area of the circle: {area}')
    elif shape_type=='square':
        side=float(input('Enter side of circle'))
        s=Square(side)
        area=s.calculate_area()
        print(f'Area of square is: {area}')
    else:
        print('Invalid choice')


class Animal:
    def makeSound(self):
        pass
    def move(self):
        pass
    def sleep(self):
        print("Animal is sleeping")
class Cat(Animal):
    def makeSound(self):
        print('Meow')
    def move(self):
        print('Cat is moving')
class Dog(Animal):
    def makeSound(self):
        print('Woof')
    def move(self):
        print('Dog is moving')
c=Cat()
d=Dog()
c.makeSound(); c.move(); c.sleep();
d.makeSound(); d.move(); d.sleep();

class Employee:
    pass
class Manager(Employee):
    def __init__(self,name,eid,sal):
        self.name=name
        self.eid=eid
        self.sal=sal
        print(f'Name = {self.name} \nEmployee ID = {self.eid} \nSalary = {self.sal}')
class Salesperson(Employee):
    def __init__(self,name,eid,sal):
        self.name=name
        self.eid=eid
        self.sal=sal
        print(f'Name = {self.name} \nEmployee ID = {self.eid} \nSalary = {self.sal}')
class Engineer(Employee):
    def __init__(self,name,eid,sal):
        self.name=name
        self.eid=eid
        self.sal=sal
        print(f'Name = {self.name} \nEmployee ID = {self.eid} \nSalary = {self.sal}')
m=Manager('kk',1,45000)
s=Salesperson('om',2,56000)
e=Engineer('raj',3,80000)

"""
"""
class Bank:
    def getBalanace():
        pass
class BankA(Bank):
    def getBalanace(self):
        print('$100 is deposited')
class BankB(Bank):
    def getBalanace(self):
        print("$150 is deposited")
class BankC(Bank):
    def getBalanace(self):
        print('$100 is deposited')

a=BankA(); a.getBalanace();
b=BankB(); b.getBalanace();
c=BankC(); c.getBalanace();

import math
class MyMath:
    def calculate():
        pass
class Sq(MyMath):
    def calculate(self,s):
        self.side=s
        area=self.side**2
        print("Square of number is:",area)
class Cone(MyMath):
    def calculate(self,r,h):
        vol=(1/3)*math.pi*r**2*h
        print("Volume of cone=",vol)
class Triangle(MyMath):
    def calculate(self,h,b):
        area=(1/2)*b*h
        print('Area of triangle=',area)
s=Sq(); s.calculate(4)
c=Cone(); c.calculate(5,7) 
t=Triangle(); t.calculate(5,4)

class Project:
    pass
class InHouse(Project):
    def met(self):
        name=input('Enter name of project:')
        size=5
        print(f'Name of project and size is: {name},{size}')
class OutHouse(Project):
    def met(self):
        name=input('Enter name of project:')
        size=5
        print(f'Name of project and size is: {name},{size}')
        
i=InHouse(); i.met();
o=OutHouse(); o.met();

import gc

class MemoryManager:
    def __init__(self, size):
        self.memory = [0] * size
        print(f"Memory allocated for object {id(self)}.")

    def __del__(self):
        print(f"Memory released for object {id(self)}.")

# Demonstrate the garbage collector in action
def create_and_discard_objects():
    # Create a few MemoryManager objects
    obj1 = MemoryManager(1000000)
    obj2 = MemoryManager(500000)
    obj3 = MemoryManager(800000)

    # Discard references to the objects
    obj1 = obj2 = obj3 = None

    # Manually run the garbage collector
    gc.collect()

# Test the MemoryManager class
create_and_discard_objects()

import math

class Shape:
    def __init__(self, color):
        self.color = color

    def calculate_area(self):
        pass  # Abstract method to be overridden in derived classes

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

# Demonstrate polymorphism by creating objects of different shapes
rectangle1 = Rectangle("Blue", 4, 6)
circle1 = Circle("Red", 3)

# Call the area calculation method for different shapes
print(f"Area of the rectangle: {rectangle1.calculate_area():.2f} square units")
print(f"Area of the circle: {circle1.calculate_area():.2f} square units")

class Student:
    def __init__(self,sapid,name,rno):
        self.sapid=sapid
        self.name=name
        self.roll_no=rno
        print(f"Sapid of student is {self.sapid},name is {self.name} and roll no is {self.roll_no}")
class Science(Student):
    def __init__(self, sapid, name, rno):
        super().__init__(sapid, name, rno)
    def readMarks(self):
        p=int(input('Enter marks of physics: '))
        c=int(input('Enter marks of chem: '))
        m=int(input(('Enter marks of maths: ')))
        self.total=p+c+m
    def display(self):
        print('Total is:',self.total)
s=Science(1,'Raj',12)
s.readMarks(); s.display();

class Commerce(Student):
    def __init__(self, sapid, name, rno):
        super().__init__(sapid, name, rno)
    def readMarks(self):
        a=int(input('Enter marks of accounts: '))
        e=int(input('Enter marks of eco: '))
        m=int(input(('Enter marks of maths: ')))
        self.total=a+e+m
    def display(self):
        print('Total is:',self.total)
s=Commerce(2,'Raju',123)
s.readMarks(); s.display();

class Arts(Student):
    def __init__(self, sapid, name, rno):
        super().__init__(sapid, name, rno)
    def readMarks(self):
        h=int(input('Enter marks for history: '))
        g=int(input('Enter marks for geagragphy: '))
        c=int(input('Enter marks for civics: '))
        self.total=h+c+g
    def display(self):
        print('Total is: ',self.total)
a=Arts(3,'Heet',125)
a.readMarks(); a.display();



class Car:
    def speed(self):
        x=int(input('Enter the speed of car:'))
        print("Speed is:",x)
class Maruti(Car):
    def speed(self):
        return super().speed()
class Alto(Car):
    def speed(self):
        return super().speed()
class Breeza(Car):
    def speed(self):
        return super().speed()
m=Maruti(); m.speed();
a=Alto(); a.speed();
b=Breeza(); b.speed();

class DJSCE:
    def __init__(self,sapid,div):
        self.sapid=sapid
        self.div=div
        print(f'Sap id is {sapid} and div is {div}')
    def getStudentInfo():
        pass
class Dep(DJSCE):
    def __init__(self, sapid, div):
        super().__init__(sapid, div)
    def getStudentInfo(self):
        self.name=input('Enter name:')
        self.rno=int(input("Enter roll number:"))
        self.clss=input('Enter class:')
        self.ptr=int(input('Enter pointer'))
class Students(Dep):
        def __init__(self, sapid, div):
            super().__init__(sapid, div)
        def displayStudentInfo(self):
            print(f'Name is {self.name},roll no is {self.rno},class is {self.clss} and pointer is {self.ptr}')

s=Students(190,"A")
s.getStudentInfo()
s.displayStudentInfo()

class Hospital():
    def __init__(self,patid,wno):
        self.patid=patid
        self.wno=wno
        print(f'Patient id is {patid} and ward no is {wno}')
    def getPatientInfo():
        pass
class AdminDept(Hospital):
    def __init__(self, patid, wno):
        super().__init__(patid, wno)
    def getPatientInfo(self):
        self.name=input('Enter name of patient')
        self.bno=int(input('Enter bed no:'))
        self.tbill=int(input('Emter total bill'))
class Patient(AdminDept):
    def __init__(self, patid, wno):
        super().__init__(patid, wno)
    def displayPatientInfo(self):
        print(f'Name of patient is {self.name},bed no is {self.bno} and total bill to pay is {self.tbill}.')
p=Patient(1,109)
p.getPatientInfo(); p.displayPatientInfo();

# Base class Grandfather
class Grandfather:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money

    def print_money(self):
        print(f"{self.name} wealth - Rs {self.money:.2f}")


# Derived class Father
class Father(Grandfather):
    def __init__(self, name, age, money):
        super().__init__(name, age, money)

    def get_child_wealth(self):
        return self.money * 0.5


# Derived class Child
class Child(Father):
    def __init__(self, name, age, money):
        super().__init__(name, age, money)
        self.money = self.get_child_wealth()


def main():
    # Taking input for grandfather's wealth
    grandfather_wealth = float(input("Enter Grandfather's wealth: Rs "))

    # Creating objects for each class
    grandfather = Grandfather("Thomas", 70, grandfather_wealth)
    father = Father("Brandon", 45, grandfather.money)
    child = Child("Alex", 10, father.get_child_wealth())

    # Printing wealth for each family member
    grandfather.print_money()
    father.print_money()
    child.print_money()


if __name__ == "__main__":
    main()

"""
class College:
    COLLEGE_NAME = "Your College Name"
    COLLEGE_ADDRESS = "College Address, City, Country"
    def header(self):
        print(f"Welcome to {self.COLLEGE_NAME}")
        print(f"Address: {self.COLLEGE_ADDRESS}")
        print("=" * 30)
class Department(College):
    def admission_form(self):
        self.header()
        print("Admission Form for Department:")
def main():
    computerScienceDept = Department()
    computerScienceDept.admission_form()


if __name__ == "__main__":
    main()

class Tree:
    def __init__(self,t_id,t_name,hgt):
        self.t_id=t_id
        self.t_name=t_name
        self.hgt=hgt
    def print_info(self):
        print(f"{self.t_id} is a {self.t_name} tree. The height of the tree is {self.hgt}ft.")
class Fruit(Tree):
    def __init__(self, t_id, t_name, hgt,clr,n_seeds,taste):
        super().__init__(t_id, t_name, hgt)
        self.color=clr
        self.taste=taste
        self.num_seeds=n_seeds
    def print_info(self):
        super().print_info()
        print(f"It bears fruits of {self.color} color with {self.num_seeds} seeds and tastes {self.taste}.")
class Flower(Tree):
    def __init__(self, t_id, t_name, hgt,clr,n_petals,frag):
        super().__init__(t_id, t_name, hgt)
        self.color=clr
        self.num_petals=n_petals
        self.fragrance=frag
    def print_info(self):
        super().print_info()
        print(f"It bears flowers of {self.color} color with {self.num_petals} petals. It has a {self.fragrance} fragrance.")
def main():
    a=Fruit(21,'Apple',70,'Red',20,'Sweet')
    f=Flower(22,'Cheery',90,'Red',4,'Good')
    a.print_info(); f.print_info();
if __name__=='__main__':
    main()