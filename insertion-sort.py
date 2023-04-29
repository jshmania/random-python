def InsertionSort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key


arr = [98, 12, 13, 5, 6, 4, 9, 99, 10, 11, 44, 65, 76, 45, 89, 77]
InsertionSort(arr)
print("-- Sorted List --")
for i in range(len(arr)):
  print (arr[i])