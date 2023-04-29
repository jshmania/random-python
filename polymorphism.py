class John():
  def name(self):
    print("Name: John")

  def age(self):
    print("Age: 17")

  def height(self):
    print("Height: 5'9")
    
  def StudentPremium(self):
    studentPremium = True
    
    if studentPremium == True:
      print("Student Premium: True")
    else:
      print("Student Premium: False")

class Luke():
  def name(self):
    print("Name: Luke")

  def age(self):
    print("Age: 20")

  def height(self):
    print("Height: 6'1")

  def StudentPremium(self):
    studentPremium = False

    if studentPremium == True:
      print("Student Premium: True")
    else:
      print("Student Premium: False")

class Josh():
  def name(self):
    print("Name: Josh")

  def age(self):
    print("Age: 18")

  def height(self):
    print("Height: 5'11")

  def StudentPremium(self):
    studentPremium = False

    if studentPremium == True:
      print("Student Premium: True")
    else:
      print("Student Premium: False")



per1 = John()
per2 = Luke()
per3 = Josh()

for type in (per1, per2, per3):
  print("---------------------")
  type.name()
  type.age()
  type.height()
  type.StudentPremium()