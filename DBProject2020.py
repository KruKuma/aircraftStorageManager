#   DBProject2020.py
#   Author:         Naphatsakorn Khotsombat
#   Description:    This program will be used to access Database from MySQL Database created for plane storage.

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS aircraftStorage")
mycursor.execute("CREATE TABLE IF NOT EXISTS aircraft (reg VARCHAR(10) NOT NULL, maker VARCHAR(25), "
                 "series VARCHAR(25), price INTEGER(20), PRIMARY KEY (reg))")
