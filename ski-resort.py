from time import sleep

class CustomerProfile:
  def __init__(self, id, email, name, age, hours, SkiLevel, SkiMove):
    self.__id = id
    self.__email = email
    self.__name = name
    self.__age = age
    self.__hours = hours
    self.__SkiLevel = SkiLevel
    self.__SkiMove = SkiMove

  def GetInfo(self):
    return """
--== ID: {} ==--
Customer Info:
  Email: {}
  Name: {}
  Age: {}
Skiing Info:
  Hours: {}
  Level: {}
  Specialised In: {}""".format(self.__id, self.__email, self.__name, self.__age, self.__hours, self.__SkiLevel, self.__SkiMove)

  def LastVisited(self, lastVisitedInDays):
    self.__lastVisitedInDays = lastVisitedInDays



# Data
per1 = CustomerProfile(1, "email1@gmail.com", "Josh", 17, 103, "Medium", "Gliding")
per2 = CustomerProfile(2, "email2@gmail.com", "John", 22, 56, "Low", "Jumping")
per3 = CustomerProfile(3, "email3@gmail.com", "Jack", 43, 789, "High", "Everything")

# Final output
print("""-------------------------
--- Customer Profiles ---
-------------------------""")
print(per1.GetInfo())
print(per2.GetInfo())
print(per3.GetInfo())



ansTesting = input("\nDo you want to enter testing grounds? y/n\n").lower()

if ansTesting == "y":
  print("""\n************************
Entered Testing Grounds!
************************\n""")
else:
  print("\nBye bye...")
  sleep(1/2)
  quit()

class Person(object): 
  # Constructor
  def __init__(self, name):
    self.name = name

  # Get name
  def GetName(self):
    return self.name
  
  # To check if this person is an employee
  def IsEmployee(self):
    return False

# Inherited or Subclass
class Employee(Person):
  def IsEmployee(self):
    return True

emp = Person("Name: Josh\n") # Object of Person
print(emp.GetName(), emp.IsEmployee())

emp = Employee("Name: James\n") # Object of Employee
print(emp.GetName(), emp.IsEmployee())