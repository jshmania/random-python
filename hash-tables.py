def MidSquareHash(value, slots):
  print(f"--- {value} ---")
  value **= 2
  print(f"sqd: {value}")
  length = len(str(value))
  if length > 1:
    mid1 = str(value)[(length // 2) - 1]
    mid2 = str(value)[(length // 2)]
    value = int(mid1 + mid2)
    print(f"mid: {value}")
  return value % slots

keys = [456, 37, 3, 12, 5875]
hashSlots = 11
for key in keys:
  print(f"pos: {MidSquareHash(key, hashSlots)}\n")