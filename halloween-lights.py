from random import randint
from time import sleep

lightStatus = input("Light on/off: ")

if lightStatus == "off":
  status = False
  quit()
elif lightStatus == "on":
  status = True
else:
  status = False
  print("Invalid input!")
  quit()

while status == True:
  lightStatus = "off"
  print("Lights off")
  sleep(randint(1, 2))
  lightStatus = "on"
  print("Lights on")
  sleep(randint(1, 2))