# get the number of chunks unlocked from the user
initialChunks = int(input("Chunks: "))

# calculate the cost of unlocking the next chunk
nextChunk = round(600 * (1.25 ** initialChunks))

# display the cost of unlocking the next chunk
print("It will cost ${:,.0f} to unlock the next chunk.".format(nextChunk))