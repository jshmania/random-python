# Class is a blueprint for creating objects
class AdultMonster:
  # def = Constructor - create attributes for an object in the class
  def __init__(self, name, eyes, furColour, size, ears, weight): # Passing parameters
    self.name = name # Public attributes, to make private self.__name
    self.eyes = eyes
    self.furColour = furColour
    self.size = size
    self.ears = ears
    self.weight = weight

  # Method
  def MonsterPrint(self): # Only self no parameter in a method
    return 'Monster name: {} \nMonster eyes colour: {}\n'.format(self.name, self.eyes)

adultMonsterOne = AdultMonster("Jacob", "Red", "Pink", "Tiny", "Floppy", 33) # Declare an object
print(adultMonsterOne.MonsterPrint()) # Object then method to print attributes show in above method for MonsterPrint

# New subclass will inherit attributes and methods from the base/parent class
class BabyMonster(AdultMonster): # To inherit pass the class as a parameter DO NOT PASS methods this will happen automatically
  def __init__(self, name, eyes, furColour, size, ears, weight, school): # Constructor - pass ALL the attributes and create NEW parameters here
    # Super allows all the methods and attributes to be inherited
    super().__init__(name, eyes, furColour, size, ears, weight) # Pass ONLY existing attributes NOT new parameters
    self.school = school # Define new attributes here after super()

babyMonsterOne = BabyMonster("Alba", "Deep Red", "Red", "Red", "Red", 5, "Monster Inc Junior School") # Declare an object
print("Baby Monster's eye colour: ", babyMonsterOne.eyes, "\nBaby Monster attends: ", babyMonsterOne.school)
print(babyMonsterOne.MonsterPrint()) # Can use method from class AdultMonster is class BabyMonster