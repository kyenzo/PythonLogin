from random import randint
users = {'user1': '123', 'user2': '234'}


def user_choice(arg):
    switcher = {
        1: '1',
        2: '2'
    }
    return switcher.get(arg, "Invalid input")


def login(auth):
    username = input("Please type in your username! ")
    if username in users.keys():
        print("username match")
    password = input("Please type in your password! ")
    if password == users[username]:
        auth = randint(1000, 9999)
        print("success login")
    return auth


def register():
    new_user = input("Please type in your new username: ")
    new_password = input("Please type in your password: ")
    users[new_user] = new_password


def login_flow(users_di):
    auth, session = 0, 0
    u_choice = input("Choose the required action with numeric input: \n"
                     "1 - Login\n2 - Register\n-> ")

    while auth == 0:
        if u_choice == '1':
            auth = login(auth)
        elif u_choice == '2':
            register()
        else:
            print("This is not a valid input! ")
        print(users_di)
        print(auth)


login_flow(users)
