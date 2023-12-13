def divide(x,y):
    try:
        res=x/y
        print("Result =",res)                                           #Arithmetic Opeation Eroro
    except ZeroDivisionError:
        print("Division by zero is not allowed")
    finally:
        print("Exception handled")

divide(5,4)

def open_file(filename):
    try:                                                                    
        file=open(filename,"r")                                            #FileNotFoundError
        contents=file.read()
        print("File contenets:")
        print(contents)
        file.close()
    except FileNotFoundError:
        print("Error File not found")

filename=input("Enter a file name:")
open_file(filename)

try:
    value=(int(input("Enter an integer:")))
    print("Success")
except ValueError:
    print("Invalid value")


def test_index(data,index):
    try:
        res=data[index]
        print("Result= ",res)                   #index out of range
    except IndexError:
        print("Errror,indeex out of range....")

n=[1,2,3,4,5,5,5]
index=int(input("Enter index:"))
test_index(n,index)

def test_list_operations(n):
    try:
        r=len(n)
        print("lenght of the list:",r)
    except AttributeError:
        print("Error: The list does not have a 'length' attribute.")

n=[1,2,3,4]
test_list_operations(n)

n1=10;n2=0
try:
    res=n1/n2
    print("Result",res)
except ZeroDivisionError:
    print("Error occured")

try:
    x=int(input('Enter integer'))
except:
    print('Error occur enter integer')

def test_list(n):
    try:
        r=len(n)
        print('lenght of the list:',r)
    except AttributeError:
        print('Error:The list does not have a length attribute')

n=[1,2,2,4,45,5]
test_list(n)
"""
                           #Custom Exceptions
class InvalidMonthError(Exception):
    pass
def display_month(month_no):
    months=['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept',"Oct",'Nov','Dec']
    if 1<=month_no<=12:
        print(f"The month corresponding to the number {month_no} is: {months[month_no - 1]}")
    else:
        raise InvalidMonthError('Invalid month number.Pls enter a proper month')
def main():
    try:
        month_no:print('Enter a valid month number')
    except ValueError:
        print('Invalid month number')
    except InvalidMonthError as e:
        print(f'Errro: {e}') 

if __name__=='__main__' :
    main()

# define Python user-defined exceptions
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass

number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
        
except InvalidAgeException:
    print("Exception occurred: Invalid Age")

class SalNotInRange(Exception):
   def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

sal=int(input('Enter amount:'))
if not 5000 < 15000:
    raise SalNotInRange(sal)
"""