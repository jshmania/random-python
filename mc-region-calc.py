def CalcChunkX(regionX):
  chunkX = int(regionX * 32)
  return chunkX

def CalcChunkY(regionY):
  chunkY = int(regionY * 32)
  return chunkY

def CalcRegionX(chunkX):
  regionX = int(chunkX / 32)
  return regionX

def CalcRegionY(chunkY):
  regionY = int(chunkY / 32)
  return regionY



# Option select
option = input("Calc chunk or region: ")

if option == "chunk":
  regionX = int(input("X pos region: "))
  regionY = int(input("Y pos region: "))
  print("Chunk: (" + str(CalcChunkY(regionX)) + ", " + str(CalcChunkX(regionY)) + ")")

elif option == "region":
  chunkX = int(input("X pos chunk: "))
  chunkY = int(input("Y pos chunk: "))
  print("Region: (" + str(CalcRegionY(chunkX)) + ", " + str(CalcRegionX(chunkY)) + ")")