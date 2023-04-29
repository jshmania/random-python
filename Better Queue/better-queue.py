import json

with open('data.json') as json_file:
  queue = json.load(json_file)
maxSize = 6
option = 0

def IsEmpty(queue):
  return not len(queue)

def IsFull(queue,maxSize):
  return len(queue) == maxSize

def EnQueue(newItem):
  if IsFull(queue, maxSize):
    print("Queue is full!")
  else:
    queue.append(newItem)
  return

def DeQueue(slot):
  if IsEmpty(queue):
    print("Queue is empty!")
  else:
    queue.pop(slot)
  return



print("List: " + str(queue))
print("Max Size: " + str(maxSize))
print("")
print("Empty: " + str(IsEmpty(queue)))
print("Full: " + str(IsFull(queue, maxSize)))

while True:
  try:
    option = int(input("\n1. Add\n2. Remove\n3. Exit\n\n"))
  except ValueError as e:
    print("")
  
  if option == 1:
    numOrTxt = input("NUM or TXT?\n").lower()
    if numOrTxt.lower() == "num":
      newItem = int(input("Enter new item: "))
      EnQueue(newItem)
    elif numOrTxt.lower() == "txt":
      newItem = input("Enter new item: ")
      EnQueue(newItem)
    else:
      print("!! Invalid Input !!")

  elif option == 2:
    try:
      slot = int(input("Select a slot to remove: ")) - 1
      slotInt = type(slot) == int
      if slotInt == True:
        DeQueue(slot)
      else:
        pass
    except ValueError as e:
      print("")
      print("!! Invalid Input !!")
    
  elif option == 3:
    with open('data.json', 'w') as json_file:
      json.dump(queue, json_file)
    quit()
    
  else:
    print("!! Invalid Input !!")
  print("List: " + str(queue))