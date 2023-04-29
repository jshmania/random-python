def AnswerYOrN(answer):
  answer = str(input("y/n\n")).lower()

  if answer == "y":
    answer = "y"
  elif answer == "n":
    answer = "n"
  else:
    print("Please enter a valid answer!")
    answer = "y"
    AnswerYOrN(answer)
  return answer

answer = "y"
answer = AnswerYOrN(answer)
print("Your answer is", answer)