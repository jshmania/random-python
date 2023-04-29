temp = float(input("Enter the temperature: "))
humidity = float(input("Enter the humidity: "))
window = str(input("Is your window open? y/n: ")).lower()

# Order of operation
if temp > 25 or humidity > 50 and window == "n":
  print("Open the window.")
elif temp < 10 and humidity < 50 and window == "y":
  print("Close the window.")
else:
  print("You found a bug in the code!")