numberOfStudents = int(input("How many students are there?\n"))
numberOfBooks = int(input("How many books are there?\n"))

# Calculate the number of books each student will get
perStudentBook = numberOfBooks // numberOfStudents
perStudentBookRemainder = numberOfBooks % numberOfStudents

# Plural or not
booksPlural = "books"
if perStudentBook < 2:
  booksPlural = "book"

# Final statement to calculate how many book(s) each student will get
print("Each student will recieve", perStudentBook, booksPlural, "with", perStudentBookRemainder, "left over.")