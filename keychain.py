usernames = []
passwords = []
platforms = []
def login():
    global username
    global password
    global platforms

def login_data():
    while True:
       user = input("Please enter your username: ")
       password = input("Please enter your password: ")
       platform = input("Please enter your platform: ")
       usernames.append(user)
       passwords.append(password)
       decision = input("Would you like to continue? (y/n): ")
       if decision == "y" or decision == "Y":
           continue
       elif decision == "n" or decision == "N":
           break
       else:
           print("Sorry, I didn't understand that.")
           continue

def keychain():
    global usernames
    global passwords
    global platforms
    for user in usernames:
        print(f"Your username is {user}")
    for password in passwords:
        print(f"Your password is {password}")
    for platform in platforms:
        print(f"Your platform is {platform}")


def main():
    login()
    login_data()
    keychain()

main()
