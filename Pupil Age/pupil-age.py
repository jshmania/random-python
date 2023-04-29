import time

name = str(input("What is your first name?\n")).replace(" ", "").replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").lower()

age = 0

def AskAge(age):
  age = int(input("What is your age?\n"))

  if age < 18:
    print("Invalid age")
    AskAge(age)
  else:
    age = age

  return age



age = AskAge(age)

with open('database.txt', 'w') as f:
    f.write("-")
    f.write(str(name))
    f.write(":")
    f.write(str(age))
    f.write("-")

print("\n---------------\nAccess granted!\n---------------")
print("Loading assests...\n")
time.sleep(3)
print("Loaded files.")
time.sleep(2)
print("Loaded database.")
time.sleep(1)
print("\nWelcome back", name.capitalize() + "!")