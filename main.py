import os
from getpass import getpass

userprofile_path = os.environ["USERPROFILE"]
passwords_path = userprofile_path + "//.barankrky//passwordManager"
passwords_file_path = passwords_path + "//passwords"

if os.path.exists(passwords_path) == True:
    pass
else:
    os.makedirs(userprofile_path + "//.barankrky//passwordManager")

def add_password():
    passwords_file = open(passwords_file_path, "a")
    password_input = getpass("Please enter a password : ")
    passwords_file.write(password_input + "\n")
    passwords_file.close()
    ask_more = input("Do you want to add more password ? (Y/n)")
    if ask_more == "y":
        add_password()
    if ask_more == "n":
        menu()



def view_passwords():
    passwords_file = open(passwords_file_path, "r+")
    for i in passwords_file.readlines():
        print(i)
    input("\nPress ENTER to continue...")
    menu()


def menu():
    os.system("cls")
    print(" Password Manager ".center(50, "*"))
    print(" 1- Add Password\n"
          " 2- View Passwords\n"
          " e- exit\n")

    menu_input = input(">> ")

    if menu_input == "1":
        add_password()
    if menu_input == "2":
        view_passwords()
    if menu_input == "e":
        exit()

if __name__ == '__main__':
    menu()


