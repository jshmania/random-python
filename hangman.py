import random
from random import randint

# Create a session ID for the user
def CreateSessionID():
  sessionIDLength = 24
  sessionID = ""

  for i in range(sessionIDLength):
    x = randint(0, 9)
    sessionID = sessionID + str(x)

  return sessionID



wordList = ["cat", "dog", "wall"]
guessingList = []

sessionID = CreateSessionID()

word = random.choice(wordList)
wordList = []

for i in range(1):
  word = word.rstrip()
  wordList.append(word[0])
  wordList.append(word[1])
  wordList.append(word[2])

# Check will always have 1 added to it
check = 6
while check != 0:
  if wordList != guessingList:
    print("Word: " + str(guessingList))
    print("Tries: " + str(check))
    guess = input("Letter: ")

    if guess == wordList[0]:
      print("\nCorrect!\n")
      guessingList.append(wordList[0])
    elif guess == wordList[1]:
      print("\nCorrect!\n")
      guessingList.append(wordList[1])
    elif guess == wordList[2]:
      print("\nCorrect!\n")
      guessingList.append(wordList[2])
    else:
      check = check - 1
      print("\nWrong!\n")
  else:
    check = 0

if guessingList == wordList:
  print("Word: " + str(guessingList))
  print("--------\nYou won!\n--------")
else:
  print("---------\nYou lost!\n---------")