class Building:
  # def = constructor - create attributes for an object in the class
  def __init__(self, ID, numFloors, width, height): # (passing parameters)
    self.ID = ID
    self.numFloors = numFloors # Public attributes, to make private self.__name
    self.width = width
    self.height = height

  # Method
  def GetNumFloors(self): # Only self no parameter in a method
    return self.numFloors

# Office class
class Office(Building):
  def __init__(self, ID, numFloors, width, height, numDesks, numCompanies): # Constructor - pass ALL the attributes and create NEW parameters here
    # Super allows all the methods and attributes to be inherited
    super().__init__(ID, numFloors, width, height) # Pass ONLY existing attributes NOT new parameters
    self.numDesks = numDesks # Define new attributes here after super()
    self.numCompanies = numCompanies

# House class
class House(Building):
  def __init__(self, ID, numFloors, width, height, bedrooms, bathrooms):
    super().__init__(ID, numFloors, width, height)
    self.bedrooms = bedrooms
    self.bathrooms = bathrooms
    
  def GetBedrooms(self):
    return self.bedrooms

  def GetBathrooms(self):
    return self.bathrooms

  def SetBedrooms(self, n):
    self.bedrooms = n

  def SetBathrooms(self, n):
    self.bathrooms = n

  def Structure(self):
    return print("\nID:", self.ID, "\nFloors:", self.numFloors, "\nWidth:", self.width, "\nHeight:", self.height , "\nBedrooms:", self.bedrooms, "\nBathrooms:", self.bathrooms)



buildingOne = Building("01", 4, 100, 100) # Declare an object
print(buildingOne.GetNumFloors())

officeOne = Office("02", 4, 100, 100, 40, 6) # Declare an object
print("Office companies:", officeOne.numCompanies, "\nOffice desks:", officeOne.numDesks)
print(officeOne.GetNumFloors())

houseOne = House("03", 3, 40, 40, 4, 2)
houseOne.Structure()