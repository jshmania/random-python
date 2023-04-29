# Asking the user their name
name = str(input("Enter a name: ")).lower()

# Blocked characters in the letters category
# Blocked: 'space' , . / < > ? 0 1 2 3 4 5 6 7 8 9
lettersOfName = int(len(name.replace(" ", "").replace(",", "").replace(".", "").replace("/", "").replace("<", "").replace(">", "").replace("?", "").replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "")))

# Blocked characters in the numbers category
# Blocked: 'space' , . / < > ? a b c d e f g h i j k l m n o p q r s t u v w x y z
numbersOfName = int(len(name.replace(" ", "").replace(",", "").replace(".", "").replace("/", "").replace("<", "").replace(">", "").replace("?", "").replace("a", "").replace("b", "").replace("c", "").replace("d", "").replace("e", "").replace("f", "").replace("g", "").replace("h", "").replace("i", "").replace("j", "").replace("k", "").replace("l", "").replace("m", "").replace("n", "").replace("o", "").replace("p", "").replace("q", "").replace("r", "").replace("s", "").replace("t", "").replace("u", "").replace("v", "").replace("w", "").replace("x", "").replace("y", "").replace("z", "")))

# Blocked characters in the numbers category
# Blocked: 'space' 0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z
otherOfName = int(len(name.replace(" ", "").replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace("a", "").replace("b", "").replace("c", "").replace("d", "").replace("e", "").replace("f", "").replace("g", "").replace("h", "").replace("i", "").replace("j", "").replace("k", "").replace("l", "").replace("m", "").replace("n", "").replace("o", "").replace("p", "").replace("q", "").replace("r", "").replace("s", "").replace("t", "").replace("u", "").replace("v", "").replace("w", "").replace("x", "").replace("y", "").replace("z", "")))

# If there are no letters then output N/A
if lettersOfName < 1:
  lettersOfName = "N/A"

# If there are no numbers then output N/A
if numbersOfName < 1:
  numbersOfName = "N/A"

# If there are no others then output N/A
if otherOfName < 1:
  otherOfName = "N/A"

# Final output
print("--====+STATS+====--\n" + "Letters:", str(lettersOfName) + "\nNumbers:", str(numbersOfName) + "\nOthers:", str(otherOfName) + "\n--====+STATS+====--")