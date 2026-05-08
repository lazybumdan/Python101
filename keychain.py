username = []
password = []

def login():
    global username
    global password
    user = input("Please enter your username: ")
    passwords = input("Please enter your password: ")
    username.append(user)
    password.append(passwords)

def keychain():
    global username
    global password
    print(f"Your usernames are {username} and the passwords are {password}")

def main():
    login()
    keychain()

main()
