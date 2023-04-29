testOneTotal = 0
testTwoTotal = 0
testThreeTotal = 0
totalStudents = int(input("Number of students: "))

for i in range(10):
  testOne = int(input("Enter score: "))
  testOneTotal = testOneTotal + testOne
  testOneAverage = testOneTotal / totalStudents

print("\nTotal marks:", str(testOneTotal))
print("Average mark:", str(testOneAverage))