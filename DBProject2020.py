#   DBProject2020.py
#   Author:         Naphatsakorn Khotsombat
#   Description:    This program will be used to access Database from MySQL Database created for plane storage.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="aircraftStorage"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS aircraftStorage")
mycursor.execute("CREATE TABLE IF NOT EXISTS aircraft (reg VARCHAR(10) NOT NULL, maker VARCHAR(25), "
                 "series VARCHAR(25), price INTEGER(20), PRIMARY KEY (reg))")


def writeLine():
    """
    Function for printing out lines
    :return:
    """
    print("-" * 35)


def checkForNum(prompt):
    """
    Using a value as a prompt from one of the option to verified if its an int or not
    :parameter prompt (int)
    :returns (int)
    """
    while True:
        try:
            number = int(input(prompt))
            break
        except ValueError:
            print("Must be numeric...")

    return number


def mainMenu():
    """
    Print out the option for the user in the main menu so that the user can choose if they want
    the manage the system or view the current aircraft in storage.
    :return:
    """
    writeLine()
    print("Main Menu of Plane Storage System - Input an option")

    while True:
        userInput = checkForNum("1. Manage the storage system"
                                "\n2. View Storage"
                                "\n3. Quit"
                                "\n>>")

        if 0 < userInput <= 3:
            break
        else:
            print("Invalid input! Must be a number between 1 to 3")

    if userInput == 1:
        res = 1

    if userInput == 2:
        res = 2

    if userInput == 3:
        exit()

    return res


def loginOption():
    """
    Print out the option for the user in the login menu giving the user the option to login
    or register an account.
    :return:
    """
    writeLine()
    print("Please login or register an account")
    while True:
        userOption = checkForNum("1. Login - existing account"
                                 "\n2. Register - new account"
                                 "\n3. Go back"
                                 "\n>>")

        if userOption == 1:
            loginMenu()

        elif userOption == 2:
            userRegMenu()

        elif userOption == 3:
            mainMenu()

        else:
            print("Not an option!")


def loginMenu():
    """
    Print out the login screen for the user to input name and password to verified if the name or password
    is in the database or not
    """

    writeLine()
    print("Welcome to our Aircraft Storage System"
          "\nPlease enter your user information")

    userData = open('loginData.txt', 'r')
    userName = []
    userPass = []

    while True:
        name = input("Username: ")
        password = input("Password: ")

        while True:
            data = userData.readline().strip()
            if data == "":
                break
            lineData = data.split(',')
            userName.append(lineData[0])
            userPass.append(lineData[1])

        if name in userName and password in userPass:
            print("Welcome " + name)
            manageMenu()
            exit()

        else:
            print("Login Failed")



def userRegMenu():
    """
    Print out the menu asking the user to input the username and password they want to register in the the database
    :return:
    """
    writeLine()
    print("Please enter the username and password you want to register")
    username = input("Username:")
    password = input("Password:")

    userData = open('loginData.txt', 'a')
    print(f"{username},{password}", file=userData)
    print("User have been register! Please login!")

    userData.close()


def manageMenu():
    """
    Print out option for the user to choose how they want to manage the aircraft storage system. They can display,
    add, remove and ypdate the aircraft storage system. It will they take them to another function that they
    want or to exit from the menu
    :return:
    """
    writeLine()
    print("Please select from the option below")
    while True:
        userInput = checkForNum("1. Display Aircraft"
                                "\n2. Add Aircraft"
                                "\n3. Remove Aircraft"
                                "\n4. Update Aircraft"
                                "\n5. Logout"
                                "\n>>")

        if userInput == 1:
            displayAircraft()

        elif userInput == 2:
            addAircraft()

        elif userInput == 3:
            removeAircraft()

        elif userInput == 4:
            updateAircraft()

        elif userInput == 5:
            loginOption()

        else:
            print("Not an option!")


def displayAircraft():
    """
    Print out the list of aircraft currently in storage in the database
    :return:
    """
    writeLine()
    mycursor.execute("SELECT * FROM aircraft")

    result = mycursor.fetchall()

    for row in result:
        print(row)


def addAircraft():
    """
    Print out a menu asking for the user to input information about the aircraft they want to add.
    It will ask the user to input the registration number, maker, series and price of the aircraft.
    Then it will update it into the database.
    :return:
    """
    writeLine()
    print("Please enter the information of the aircraft")
    sqlFormula = "INSERT INTO aircraft VALUES (%s, %s, %s, %s)"

    reg = input("Registration No.:")
    maker = input("Maker:")
    series = input("Series:")
    price = input("Price:")

    aircraft = (reg, maker, series, price)

    mycursor.execute(sqlFormula, aircraft)

    mydb.commit()


def removeAircraft():
    """
    Print out the menu asking for the registration number of the aircraft the user want to remove.
    Then it will update it into the database.
    :return:
    """
    writeLine()
    print("Please enter the registration number of the aircraft you want to remove")
    reg = input("Registration No.:")
    sql = "DELETE FROM aircraft WHERE reg= %s"
    remove = (reg,)
    mycursor.execute(sql, remove)

    mydb.commit()

    print("Aircraft Removal Successful")


def updateAircraft():
    """
    Print out the menu asking what the user want to update in the about the aircraft and it will ask
    for the registration number of the aircraft. Then it will update it into the database.
    :return:
    """
    writeLine()
    while True:
        print("Select what you want to update")
        userInput = checkForNum("1. Maker"
                                "\n2. Series"
                                "\n3. Price"
                                "\n4. Exit"
                                "\n>>")
        print("Please enter the registration number of the aircraft you want to update")
        reg = input("Registration No.:")

        if userInput == 1:
            maker = input("New Maker:")
            sql = "UPDATE aircraft SET maker= %s WHERE reg= %s"
            update = (maker, reg)
            mycursor.execute(sql, update)
            mydb.commit()

        elif userInput == 2:
            series = input("New Series:")
            sql = "UPDATE aircraft SET series= %s WHERE reg= %s"
            update = (series, reg)
            mycursor.execute(sql, update)
            mydb.commit()

        elif userInput == 3:
            price = checkForNum("New Price:")
            sql = "UPDATE aircraft SET price =%s WHERE reg =%s"
            update = (price, reg)
            mycursor.execute(sql, update)
            mydb.commit()

        elif userInput == 4:
            exit()

        else:
            print("Not an option!")


def main():
    while True:
        mainMenuInput = mainMenu()

        if mainMenuInput == 1:
            loginOption()

        elif mainMenuInput == 2:
            displayAircraft()

        else:
            print("Not an option!")


main()
