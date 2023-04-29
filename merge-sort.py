def MergeSort(arr):
  if len(arr) > 1:
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    MergeSort(L)
    MergeSort(R)
    leftIndex = rightIndex = newListIndex = 0
    while leftIndex < len(L) and rightIndex < len(R):
      if L[leftIndex] < R[rightIndex]:
        arr[newListIndex] = L[leftIndex]
        leftIndex += 1
      else:
        arr[newListIndex] = R[rightIndex]
        rightIndex += 1
      newListIndex += 1
    while leftIndex < len(L):
      arr[newListIndex] = L[leftIndex]
      leftIndex += 1
      newListIndex += 1
    while rightIndex < len(R):
      arr[newListIndex] = R[rightIndex]
      rightIndex += 1
      newListIndex += 1



arr = [12, 11, 13, 5, 6, 7]
MergeSort(arr)
print(arr)