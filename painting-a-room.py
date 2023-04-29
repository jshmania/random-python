def WallMeasurements():
  totalArea = 0
  measurement = int(input("Input how many walls your room has: "))
  for count in range(measurement):
    height = float(input("\nHeight of a wall: "))
    width = float(input("Width of a wall: "))
    area = height * width
    totalArea = area + totalArea
    print("Overall total area:", totalArea)
  return totalArea

def UnpaintableMeasurements():
  totalUnpaintableArea  = 0
  measurement = int(input("\nInput how many un-paintable areas there are: "))
  for count in range(measurement):
    height = float(input("\nHeight of un-paintable area (cm): "))
    width = float(input("Width of un-paintable area (cm): "))
    area = height * width
    totalUnpaintableArea = area + totalUnpaintableArea
    print("Overall total un-paintable area:", totalUnpaintableArea)
  return totalUnpaintableArea



# Basic greeting
print("Welcome to the Paint My Room Program! Answer with 'yes', 'no' or a number that represents a measurement!\n")

# Asking for wall mesurements
totalArea = 0
totalArea = WallMeasurements()
# Asking for window mesurements
totalUnpaintableArea = 0
totalUnpaintableArea = UnpaintableMeasurements()

paintedArea = totalArea - totalUnpaintableArea
print("\n\nTotal area:", totalArea - totalUnpaintableArea)

# 1 bucket = 11 square metres
buckets = paintedArea / 11
extraBucket = paintedArea % 11
if extraBucket > 0:
  buckets = buckets // 1
  buckets = buckets + 1
plural = "buckets"
if buckets == 1:
  plural = "bucket"

# Conclusion
print(buckets, plural, "buckets of paint is required to completely paint your room.\n\nThanks for using the Paint My Room Program.\n<3")