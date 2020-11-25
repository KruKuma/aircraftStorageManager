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
    print("Main Menu of Plane Storage System - Input an option")

    res = 0

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

    elif userInput == 2:
        res = 2

    elif userInput == 3:
        exit()

    else:
        print("Not an option!")

    return res


def loginOption():
    while True:
        userOption = checkForNum("1. Login - existing account"
                                 "\n2. Register - new account"
                                 "\n>>")

        if userOption == 1:
            loginMenu()

        elif userOption == 2:
            userRegMenu()

        else:
            print("Not an option!")


def loginMenu():
    """
    Print out the login screen for the user to input name and password to verified if the name or password
    is in the database or not
    """
    isUser = False

    print("Welcome to our Aircraft Storage System"
          "Please enter your user information")

    while True:
        name = input("Username: ")
        password = input("Password: ")

        userData = open('loginData.txt', 'r')
        userName = []
        userPass = []

        while True:
            data = userData.readline().strip()
            if data == "":
                break
            lineData = data.split(',')
            userName.append(lineData[0])
            userPass.append(lineData[1])

        print(data, userName, userPass)

        if name in userName and password in userPass:
            print("Welcome " + name)
            manageMenu()
            exit()

        else:
            print("Login Failed")



def userRegMenu():
    username = input("Username:")
    password = input("Password:")

    userData = open('loginData.txt', 'w')
    print(f"{username},{password}", file=userData)
    print("User have been register! Please login!")


def manageMenu():

    while True:
        userInput = checkForNum("1. Display Aircraft"
                                "\n2. Add Aircraft"
                                "\n3. Remove Aircraft"
                                "\n4. Update Aircraft"
                                "\n5. Quit"
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
            break

        else:
            print("Not an option!")


def displayAircraft():
    mycursor.execute("SELECT * FROM aircraft")

    result = mycursor.fetchall()

    for row in result:
        print(row)


def addAircraft():
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
    print("Please enter the registration number of the aircraft you want to remove")
    reg = input("Registration No.:")
    sql = "DELETE FROM aircraft WHERE reg= %s"
    mycursor.execute(sql, reg)

    mydb.commit()


def updateAircraft():
    print("Please enter the registration number of the aircraft you want to remove")

    while True:
        reg = input("Registration No.:")
        print("Select what you want to update")
        userInput = checkForNum("1. Maker"
                                "2. Series"
                                "3. Price"
                                "4. Exit")

        if userInput == 1:
            maker = input("New Maker:")
            sql = "UPDATE student SET maker = %s WHERE reg = %s"
            mycursor.execute(sql, maker, reg)
            mydb.commit()

        elif userInput == 2:
            series = input("New Series:")
            sql = "UPDATE student SET series = %s WHERE reg = %s"
            mycursor.execute(sql, series, reg)
            mydb.commit()

        elif userInput == 3:
            price = input("New Price:")
            sql = "UPDATE student SET price = %s WHERE reg = %s"
            mycursor.execute(sql, price, reg)
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
