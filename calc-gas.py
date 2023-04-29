# Miles information
milesLastFilled = float(input("What was the mileage of the car the last time you filled it?\n"))

milesNow = float(input("What is the car mileage now?\n"))
milesDriven = milesNow - milesLastFilled

# Tank information
totalLitresToFillTank = float(input("What is the fuel tank limit (in litres)?\n"))

litresAfterDriven = float(input("How much is in the tank now (in litres)?\n"))
litresUsed = totalLitresToFillTank - litresAfterDriven

# Gallons information
gallonsUsed = litresUsed / 4.546
gallonsPerMile = gallonsUsed / milesDriven

print("\nYou've driven", milesDriven, "miles and used", litresUsed, "litres of fuel.\nThe car is currently using", round(gallonsPerMile, 3), "gallons per mile.")

# 0.22 gallons = litre
# 4.546 litres = gallon