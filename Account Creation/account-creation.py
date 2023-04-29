import sqlite3

# Create username
def AskUsername():
  username = input("Enter a username: ")
  usernameLength = len(username)
  usernameLower = username.lower()
  # Need to sort out the banned words check! #
  bannedUsernames = ["fuck", "cunt", "faggot", "bitch", "slag"]
  bannedUsernamesListLength = len(bannedUsernames)
  bannedUsernamesCheck = 0

  # Password checks
  while bannedUsernamesListLength != 0:
    if username != bannedUsernames[bannedUsernamesCheck]:
      bannedUsernamesCheck += 1
      bannedUsernamesListLength -= 1
    else:
      bannedUsernamesListLength = 0
      print("Username not allowed!")
      AskUsername()
      
  if usernameLength < 3 or usernameLength > 18:
    print("Invalid username length! Must be between 3 and 18 characters long.")
    AskUsername()
  else:
    return username
  
  #if usernameLower == "fuck":
  #  print("Username not allowed!")
  #  AskUsername()
  #else:
  #  return username

# Create password
def AskPassword():
  password = input("Enter a password: ")
  
  passwordLength = len(password)

  # Password checks
  if passwordLength < 8 or passwordLength > 32:
    print("Invalid password length! Must be between 8 and 32 characters long.")
    AskPassword()
  else:
    return password



username = str(AskUsername())
password = str(AskPassword())

print("Username: " + username)
print("Password: " + password)

con = sqlite3.connect('users.db')
cur = con.cursor()

# Creating a database
#cur.execute('''CREATE TABLE stocks
#               (id integer, user text, pass text)''')

# Insert data into database
#cur.execute("INSERT INTO stocks VALUES (2, 'username', 'password')")

# Printing the entire database
for row in cur.execute('SELECT * FROM stocks ORDER BY id'):
  print(row)

con.commit()
con.close()