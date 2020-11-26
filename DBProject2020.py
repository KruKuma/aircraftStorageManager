#   DBProject2020.py
#   Author:         Naphatsakorn Khotsombat
#   Description:    This program will be used to access Database from MySQL Database created for plane storage.

import mysql.connector

#   Creating MySQLConnection object
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="aircraftStorage"
)

#   Creating MySQLCursor object
mycursor = mydb.cursor()

#   Using cursor object to execute the query to create the database and table if not exists
mycursor.execute("CREATE DATABASE IF NOT EXISTS aircraftStorage")
mycursor.execute("CREATE TABLE IF NOT EXISTS aircraft (reg VARCHAR(10) NOT NULL, maker VARCHAR(25), "
                 "series VARCHAR(25), price INTEGER(20), PRIMARY KEY (reg))")


def write_line():
    """
    Function for printing out lines
    :return:
    """
    print("-" * 35)  # Print out a line


def check_for_num(prompt):
    """
    Using a value as a prompt from one of the option to verified if its an int or not
    :parameter prompt (int)
    :returns (int)
    """
    while True:
        try:
            number = int(input(prompt))  # Prompt for input and check if it is an int
            break
        except ValueError:
            print("\nMust be numeric...\n")  # If it is not an int print out error

    return number


def main_menu():
    """
    Print out the option for the user in the main menu so that the user can choose if they want
    the manage the system or view the current aircraft in storage.
    :return:
    """
    write_line()
    print("\nMain Menu of Plane Storage System - Input an option")

    res = 0     # Initialise res

    while True:
        userInput = check_for_num("\n1. Manage the storage system"        # Print out main menu and prompt for input
                                  "\n2. View Storage"
                                  "\n3. Quit"
                                  "\n>>")

        if 0 < userInput <= 3:                                          # If input is between 0 and 3 break out of loop
            break
        else:
            print("\nInvalid input! Must be a number between 1 to 3\n")

    if userInput == 1:      # If input equal to 1 res is equal to 1
        res = 1

    if userInput == 2:      # If input equal to 2 res is equal to 2
        res = 2

    if userInput == 3:      # If input equal to 3 exit the program
        exit()

    return res


def login_option():
    """
    Print out the option for the user in the login menu giving the user the option to login
    or register an account.
    :return:
    """
    write_line()
    print("\nPlease login or register an account")
    while True:
        userOption = check_for_num("\n1. Login - existing account"    # Print out login option and prompt for input
                                   "\n2. Register - new account"
                                   "\n3. Go back"
                                   "\n>>")

        if userOption == 1:             # If input equal 1 will display login menu
            login_menu()

        elif userOption == 2:           # If input equal 2 will display registration menu
            user_reg_menu()

        elif userOption == 3:           # If input equal 3 will go back to main menu
            main_menu()

        else:
            print("\nNot an option!\n")     # If input not between 1 and 3 print out error


def login_menu():
    """
    Print out the login screen for the user to input name and password to verified if the name or password
    is in the database or not
    """

    write_line()
    print("\nWelcome to our Aircraft Storage System"      # Print out message asking for user input
          "\nPlease enter your user information")

    userData = open('loginData.txt', 'r')               # Creating data from an file for reading from it
    userName = []                                       # Creating list that will contain username
    userPass = []                                       # Creating list that will contain password

    while True:
        name = input("\nUsername: ")                    # Prompt to input username
        password = input("Password: ")                  # Prompt to input password

        while True:
            data = userData.readline().strip()          # Write from the line and remove and spacing
            if data == "":
                break
            lineData = data.split(',')                  # Split each string into a list using comma as a separator
            userName.append(lineData[0])                # First string is the username
            userPass.append(lineData[1])                # Second string is the password

        if name in userName and password in userPass:   # If username and password input is in username and password
            print("\nWelcome " + name)                  # list then it may continue to the management menu
            manage_menu()
            exit()

        else:
            print("\nLogin Failed\n")                   # Print out error if input is not in username and password list


def user_reg_menu():
    """
    Print out the menu asking the user to input the username and password they want to register in the the database
    :return:
    """
    write_line()
    print("\nPlease enter the username and "              # Print out message asking for user input
          "password you want to register")
    username = input("Username:")                       # Prompt to input username
    password = input("Password:")                       # Prompt to input password

    userData = open('loginData.txt', 'a')               # Creating data from an file to add to
    print(f"{username},{password}", file=userData)      # Adds username and password into the file
    print("\nUser have been register! Please login!\n")

    userData.close()


def manage_menu():
    """
    Print out option for the user to choose how they want to manage the aircraft storage system. They can display,
    add, remove and update the aircraft storage system. It will they take them to another function that they
    want or to exit from the menu
    :return:
    """
    write_line()
    print("\nPlease select from the option below")
    while True:
        userInput = check_for_num("\n1. Display Aircraft"       # Print out login option and prompt for input
                                  "\n2. Add Aircraft"
                                  "\n3. Remove Aircraft"
                                  "\n4. Update Aircraft"
                                  "\n5. Logout"
                                  "\n>>")

        if userInput == 1:                                      # If input equal 1 display aircraft in storage
            display_aircraft()

        elif userInput == 2:                                    # If input equal 2 shows add menu
            add_aircraft()

        elif userInput == 3:                                    # If input equal 3 shows remove menu
            remove_aircraft()

        elif userInput == 4:                                    # If input equal 4 shows update menu
            update_aircraft()

        elif userInput == 5:                                    # If input equal 5 go back to login option
            login_option()

        else:
            print("\nNot an option!\n")                             # If input not between 1 and 5 output error


def display_aircraft():
    """
    Print out the list of aircraft currently in storage in the database
    :return:
    """
    write_line()
    mycursor.execute("SELECT * FROM aircraft")      # Cursor object execute query to take all information from the
                                                    # aircraft table

    result = mycursor.fetchall()                    # Take all the rows of the query result set and returns a list

    print("\nThese are the current aircraft in the database\n")
    for row in result:                              # Print out each row of the list
        print(row)


def add_aircraft():
    """
    Print out a menu asking for the user to input information about the aircraft they want to add.
    It will ask the user to input the registration number, maker, series and price of the aircraft.
    Then it will update it into the database.
    :return:
    """
    write_line()
    print("\nPlease enter the information of the aircraft")           # Print out message asking for user input
    sqlFormula = "INSERT INTO aircraft VALUES (%s, %s, %s, %s)"     # Initialising the query for inserting an aircraft

    # Prompt for the aircraft information
    reg = input("\nRegistration No.:")
    maker = input("Maker:")
    series = input("Series:")
    price = input("Price:")

    # Inserting information
    aircraft = (reg, maker, series, price)
    mycursor.execute(sqlFormula, aircraft)

    # Make sure data is committed to the database
    mydb.commit()

    print("\nAircraft Successfully Added!\n")


def remove_aircraft():
    """
    Print out the menu asking for the registration number of the aircraft the user want to remove.
    Then it will update it into the database.
    :return:
    """
    write_line()
    print("\nPlease enter the registration number of the aircraft you want to remove")

    # Prompt for registration number
    reg = input("\nRegistration No.:")

    # Initialising the query for inserting an aircraft
    sql = "DELETE FROM aircraft WHERE reg= %s"

    # Removing aircraft
    remove = (reg,)
    mycursor.execute(sql, remove)

    # Make sure data is committed to the database
    mydb.commit()

    print("\nAircraft Removal Successful\n")


def update_aircraft():
    """
    Print out the menu asking what the user want to update in the about the aircraft and it will ask
    for the registration number of the aircraft. Then it will update it into the database.
    :return:
    """
    write_line()
    while True:
        # Print out updating menu and prompt for input
        print("\nSelect what you want to update")
        userInput = check_for_num("\n1. Maker"
                                  "\n2. Series"
                                  "\n3. Price"
                                  "\n4. Exit"
                                  "\n>>")
        print("Please enter the registration number of the aircraft you want to update")

        # Prompt for registration number
        reg = input("Registration No.:")

        if userInput == 1:
            # Prompt for Maker
            maker = input("New Maker:")

            # Initialising the query for updating the maker using registration number
            sql = "UPDATE aircraft SET maker= %s WHERE reg= %s"

            # Update information
            update = (maker, reg)
            mycursor.execute(sql, update)

            # Make sure data is committed to the database
            mydb.commit()

            print("\nAircraft Successfully Updated!\n")

        elif userInput == 2:
            # Prompt for Series
            series = input("New Series:")

            # Initialising the query for updating the series using registration number
            sql = "UPDATE aircraft SET series= %s WHERE reg= %s"

            # Update information
            update = (series, reg)
            mycursor.execute(sql, update)

            # Make sure data is committed to the database
            mydb.commit()

            print("\nAircraft Successfully Updated!\n")

        elif userInput == 3:
            # Prompt for price
            price = check_for_num("New Price:")

            # Initialising the query for updating the price using registration number
            sql = "UPDATE aircraft SET price =%s WHERE reg =%s"

            # Update information
            update = (price, reg)
            mycursor.execute(sql, update)

            # Make sure data is committed to the database
            mydb.commit()

            print("\nAircraft Successfully Updated!\n")

        elif userInput == 4:
            exit()

        else:
            print("\nNot an option!\n")


def main():
    while True:
        # Prompt for result in the main menu
        mainMenuInput = main_menu()

        # If result is 1 show login menu
        if mainMenuInput == 1:
            login_option()

        # If result is 2 display aircraft in the database
        elif mainMenuInput == 2:
            display_aircraft()

        else:
            print("\nNot an option!\n")


main()

# Make sure to close cursor object
mycursor.close()
