# Sorting with integers
def BubbleSort(arr):
	n = len(arr)
	swapped = False
	for i in range(n-1):
		for j in range(0, n-i-1):

			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		if not swapped:
			return

arr = [12, 11, 13, 5, 6, 7, 65, 83, 23, 55, 10, 33, 33, 33, 65, 87, 58, 78, 87, 99, 22, 102, 55, 1, 4, 3, 2, 100, 99, 98, 97,96, 55, 64, 46, 34, 867, 78, 12436745, 678, 325, 967856, 6, 8, 9, 4, 2, 7, 89, 54, 35, 56854, 2653, 4673, 3463, 26536, 3463, 783456, 7426, 786573, 7864, 8925, 835, 854, 937, 838, 8, 3, 893457, 83, 835, 835, 784, 7357, 85, 78357, 7345, 3423, 79724, 72467, 246, 754, 9, 8, 7, 5, 4, 3, 2, 22, 87, 246, 2346536346346346536, 475345, 245, 567457, 246246, 75475, 3835423, 846356, 35734]

BubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("% d" % arr[i], end=" ")



# Sorting with strings
items = ["Sophie", "Lily", "Jessica", "Isabella", "Ava", "Poppy", "Emily", "Isla", "Olivia", "Amelia"]

n = len(items)
swapped = True

while n > 0 and swapped == True:
  swapped = False
  n -= 1
  for index in range(0, n):
    if items[index] > items[index+1]:
      temp = items[index]
      items[index] = items[index+1]
      items[index+1] = temp
      swapped = True
  print("\n" + str(items))

print("\n\n" + str(items))