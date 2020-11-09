#   DBProject2020.py
#   Author:         Naphatsakorn Khotsombat
#   Description:    This program will be used to access Database from MySQL Database created for plane storage.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
)

print(mydb)
