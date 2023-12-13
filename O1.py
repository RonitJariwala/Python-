"""
class Person():
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.id,self.name)

class Man(Person):
    def displ(self):
        print("shugsd")

m=Man("hjds",1)
m.display()
m.displ()

class Mother:
    mothername = ""
    def mother():
        print(mothername)
 
class Father:
    fathername = ""
    def father():
        print(fathername)
 
class Son(Mother, Father):
    def parents(self):
        print("Father :",self.fathername)
        print("Mother :",self.mothername)
  
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()
"""
"""
class Vehicle:
    color="white"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    
class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

b=Bus("School bus",120,12)
print(b.color, b.name, "Speed:", b.max_speed, "Mileage:", b.mileage)

c=Car("Mercedes",220,18)
print(c.color, c.name, "Speed:", c.max_speed, "Mileage:", c.mileage)

class Shape:
    pass
class Circle(Shape):
    def __init__(self,radius):
        area=3.14*radius**2
        print("Area of circle:",area)
class Rectangle(Shape):
    def __init__(self,l,b):
        area=l*b
        print("Area of rectangle:",area)

c=Circle(4.3)
r=Rectangle(5,4)

class BankAccount:
    bal=int(input("Enter balance of account:"))
    def __init__(self,acc_no):
        self.acc_no=acc_no
    def deposit(self,amt):
        self.bal += amt
        print("Balance after deposit:",self.bal)
    def withdraw(self,amt):
        self.bal -= amt
        print("Balance after withdrawl:",self.bal)
class SavingsAccount(BankAccount):
    def withdraw(self,amt):
        if self.bal - amt < 100:
            print("Withdrawel not possible")
        else:
            self.bal -= amt
    
b=BankAccount(1)
b.deposit(200)
b.withdraw(100)

class Faculty:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def details(self):
        print(f"Name is: {self.name}")
        print(f"Salary is: {self.salary}")

class PartTime(Faculty):
    def __init__(self, name, salary,hrs):
        super().__init__(name, salary)
        self.hrs=hrs
    def details(self):
        super().details()
        print(f"Hours: {self.hrs}")

class FullTime(Faculty):
    def __init__(self, name, salary,dur):
        super().__init__(name, salary)
        self.dur=dur
    def details(self):
        super().details()
        print(f"Durations: {self.dur}")

fal1=PartTime("Manan",8930,3)
fal1.details()
fal2=FullTime("Raj",2823,"5 years")
fal2.details()
"""
"""
class GeommetryObject:
    def calculateArea():
        pass
class Square(GeommetryObject):
    def calculateArea(self,s):
         self.side=s
         area=s**2
         print("Area of square is:",area)
class Circle(GeommetryObject):
    def calculateArea(self,r):
        self.r=r
        area=3.14*r**2
        print("Area of circle is:",area)

s=Square()
side=int(input("Enter side of square:"))
s.calculateArea(side)
c=Circle()
radius=int(input("Enter radius:"))
c.calculateArea(radius)

class Book:
    pass
class Tech(Book):
    def details(self,name,a_name):
        self.n=name
        self.a=a_name
        print(f"Name of book {self.n} and author {self.a}")
class NonTech(Book):
    def details(self,name,a_name):
        self.n=name
        self.a=a_name
        print(f"Name of book {self.n} and author {self.a}")
t=Tech()
name=input("Enter name of book")
a_name=input("Enter author name")
t.details(name,a_name)
nt=NonTech()
name=input("Enter name of book")
a_name=input("Enter author name")
nt.details(name,a_name)

class Project:
    pass
class InHouse(Project):
    def __init__(self,name,t_size):
        self.name=name
        self.t_size=t_size
        print(f"Team name is {self.name} and size is {self.t_size}")
class OutHouse(Project):
    def __init__(self,name,t_size):
        self.name=name
        self.t_size=t_size
        print(f"Team name is {self.name} and size is {self.t_size}")
i=InHouse("harsh",892)
o=OutHouse("sgh",217)

class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def info(self):
        print(f"Vehicle: {self.make} {self.model} {self.year}")
class Car(Vehicle):
    def __init__(self, make, model, year,nod):
        super().__init__(make, model, year)
        self.nod=nod
    def drive(self):
        print(f"Driving my {self.make} {self.model}!")
class MotorCycle(Vehicle):
    def __init__(self, make, model, year,eng_size):
        super().__init__(make, model, year) 
        self.eng_size=eng_size
    def wheelie(self):
        print(f"Popping a wheelie on my {self.make} {self.model}!")
c=Car("Ford","Mustang",1961,4)
c.info()
c.drive()
m=MotorCycle("Harley","718921",289,250)
m.info()
m.wheelie()
"""
class Employee:
    def __init__(self,emp_name,emp_id,sal):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.sal=sal
        print(f"Employee name:{self.emp_name},employee id:{self.emp_id},salary:{self.sal}")
    def display():
        pass
class Manager(Employee):
    def __init__(self, emp_name, emp_id, sal,age):
        super().__init__(emp_name, emp_id, sal)
        self.age=age
    def display():
        pass
class Engineer(Employee):
    def __init__(self, emp_name, emp_id, sal,exp):
        super().__init__(emp_name, emp_id, sal)
        self.exp=exp
        print(f"Employee name:{self.emp_name},employee id:{self.emp_id},salary:{self.sal}")
    def display():
        pass
m=Manager("Jash",1,9022,12)
e=Engineer("Harsh",2,8393,45)

class Employee:
    def work():
        print("Employee is working")
    def getSalary(self,sal):
        self.sal=sal
        print("Salary is :",sal)
class HRManager(Employee):
    def work(self):
        print("Working???")
    def addEmployee(self,emp):
        self.emp=emp
        print("Enter employee:",emp)
h=HRManager()
h.work()
h.addEmployee(12)

class Member:
    def __init__(self,name,age,phone_number,add,sal):
        self.name=name
        self.age=age
        self.phone_number=phone_number
        self.add=add
        self.sal=sal
    def printSalary(self):
        print("Salary:",self.sal)
class Employee(Member):
        def __init__(self, name, age, phone_number, add, sal,spec):
            super().__init__(name, age, phone_number, add, sal)
            self.spec=spec
class Manager(Member):
    def __init__(self, name, age, phone_number, add, sal,dep):
        super().__init__(name, age, phone_number, add, sal)
        self.dep=dep
    
emp=Employee("Ra",10,2883933,"Has",90000.0,"IT")
m=Manager("d",20,289228,"muimbai",2300.,"CS")
emp.printSalary()
m.printSalary()


