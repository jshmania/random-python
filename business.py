arr = [10000,8000,12000,13000,9000,11000,14000,16000,12000,13000,17000,19000]
fourArr = []
eightArr = []
fourAvg = []

for x in range(len(arr)-3):
  fourArr.append((arr[x]+arr[x+1]+arr[x+2]+arr[x+3]))

for x in range(len(fourArr)-1):
  eightArr.append((fourArr[x]+fourArr[x+1]))
  
for x in range(len(eightArr)):
  fourAvg.append((eightArr[x]/8))

print(fourArr)
print(eightArr)
print(fourAvg)