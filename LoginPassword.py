import re

pattern1 = "^(?![-._])(?!.*[_.-]{2})[\w.-]{6,30}(?<![-._])$"
pattern2 = "[A-Za-z0-9@#$%^&+=_+-]{8,}"


def login_password(username=None, password=None):
    print("Administrator login Panel ")
    print("\t1.New user Entry\n"
          "\t2.Change Credentials\n"
          "\t3.Show all accounts")

    option = int(input("Enter your choise:"))
    if option == 1:
        enroll_login()
        return username, password
    elif option == 2:
        u, p = change_credentials(username, password)
        return u, p
    elif option == 3:
        show_users(username, password)
        return username, password
    else:
        print("You enter wrong input plz try again")
        login_password(username, password)


def enroll_login():
    with open("accounts.txt", "a") as f:
        username, password = getInput()
        account = "" + username + "\t" + password + "\n"
        f.write(account)
    return username, password


def change_credentials(username=None, password=None):
    with open("accounts.txt", "r") as f:
        lines = f.readlines()
    with open("accounts.txt", "w") as f:
        for line in lines:
            data = line.split("\t")
            if not (data[0] == username and data[1] == password):
                f.write(line)
    u, p = enroll_login()
    return u, p


def show_users(username, password):
    p = input("First enter password to verify: ")
    with open("accounts.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            data = line.split('\t')
            if data[0] == username and data[1].split("\n")[0] == p:
                print("-----Entries ----\n"
                      "Username\tPassword\n" +
                      ''.join(lines))
                return

        print("Sorry you enter worng credentials ")


def getInput():
    print("\t\t\t\tWelcome!\n"
          "Note For username :\n"
          "\t1. Username must be 6-30 characters long\n"
          "\t2. Username may not begin with: special character\n"
          "Note for Password\n"
          "\t1. Your Password contains At least 8 characters\n"
          "\t2. Must be restricted to, though does not specifically require any of:\n"
          "\t\ta.uppercase letters: A-Z\n"
          "\t\tb.lowercase letters: a-z\n"
          "\t\tc.numbers: 0-9\n"
          "\t\td.any of the special charactersspace excluded: @#$%^&+=\n"
          )

    username = input("Enter username =")
    result = re.findall(pattern1, username)
    while not result:
        username = input("You enter invalid username, kindly enter correct username:")
        result = re.findall(pattern1, username)

    password = input("Enter password =")
    result = re.findall(pattern2, password)
    while not result:
        password = input("You enter invalid password, kindly enter correct password:")
        result = re.findall(pattern2, password)

    return username, password


if __name__ == "__main__":
    with open("accounts.txt", "r") as f:
        line = f.readline()
        data = line.split("\t")
        login_password(data[0], data[1])
