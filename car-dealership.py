from time import sleep

class Car:
  def __init__(self, itemID, itemModel, itemPrice, carType, age, itemWarranty):
    self.itemID = itemID
    self.itemModel = itemModel
    self.itemPrice = itemPrice
    self.carType = carType
    self.age = age
    self.itemWarranty = itemWarranty

  def __str__(self):
    return f"""ID: {self.itemID}
Model: {self.itemModel}
Price: {self.itemPrice}
Type: {self.carType}
Age: {self.age}
Warranty: {self.itemWarranty}"""

def AskOptions():
  ans = input("""
   --== + ==--
  "See options"  1
     "Exit"      2
  """)
  return ans



# List of cars
cars = [
  Car("01", "Volkswagen", "£20,995", "Manual", "New", "3 years"),
  Car("02", "BMW M3", "£73,950", "Manual", "New", "3 years"),
  Car("03", "Tesla Model X", "£57,450", "Automatic", "Used", "N/A"),
  Car("04", "N/A", "N/A", "N/A", "N/A", "N/A"),
  Car("05", "N/A", "N/A", "N/A", "N/A", "N/A"),
]

ans = AskOptions()

if ans == "1":
  print("-- Options --")
  for car in cars:
    print("---------------------")
    sleep(1/18)
    print(car)
  print("\n:<><><><>:  ENDED  :<><><><>:\n")
else:
  quit()

ansTesting = input("Enter testing grounds? y/n\n").lower()

if ansTesting == "y":
  print("""\n------------------------
Entered Testing Grounds!
------------------------\n""")
else:
  print("Bye bye...")
  sleep(1/4)
  quit()

# Example usage of the Car class
car1 = Car("01", "Volkswagen", "£23,000", "Manual", "New", "3 years")

print(car1.itemID)
print(car1.itemPrice)