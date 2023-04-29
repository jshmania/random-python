from time import sleep

list = []
invalidInput = 0
invalidInputMax = 5

def RemoveItem():
  list.pop(int(input("Item to be removed: ")) - 1)

def AddItem():
  list.append(input("Enter item: "))



# While statement to run until it's given the quit function
while invalidInput < invalidInputMax:
  # Show list
  print("\nList: " + str(list))
  
  # Show menu
  option = input("""Options:
【+ add + 】
【- remove - 】
【🚪 exit 🚪】
""")

  # Add an item
  if option == "+" or option == "add":
    AddItem()

  # Remove an item
  elif option == "-" or option == "remove":
    RemoveItem()

  # Quit program
  elif option.lower() == "q" or option == "quit" or option == "exit":
    print("Closing Program...")
    sleep(1/2)
    quit()

  else:
    print("--------------\nInvalid Input!\n--------------")
    invalidInput = invalidInput + 1
    print("Tries:" + str(invalidInput) + "/" + str(invalidInputMax))



print("Too many invalid inputs!")
print("Closing Program...")
sleep(1/2)
quit()