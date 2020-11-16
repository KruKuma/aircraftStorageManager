#   DBProject2020.py
#   Author:         Naphatsakorn Khotsombat
#   Description:    This program will be used to access Database from MySQL Database created for plane storage.

import mysql.connector


def initDatabase():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root"
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

    while True:
        userInput = checkForNum("1. Manage the storage system"
                                "\n2. View Storage"
                                "\n3. Quit")

        if 0 < userInput <= 3:
            break
        else:
            print("Invalid input! Must be a number between 1 to 3")

    if userInput == 1:
        userInput = 1
    if userInput == 2:
        userInput = 2
    if userInput == 3:
        exit()

    return userInput


def main():
    initDatabase()

    while True:
        mainMenuInput = mainMenu()

        if mainMenuInput == 1:
            print()

        if mainMenuInput == 2:
            print()


main()
