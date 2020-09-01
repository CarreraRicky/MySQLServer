import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database = "NBA"
)
# Allows to user to use MySQL commands
db_Cursor = db.cursor()

# Creating the database
# db_Cursor.execute("CREATE DATABASE NBA")

# Create tables to add to the Database
# db_Cursor.execute("CREATE TABLE Players (jerseynumber int PRIMARY KEY, firstname VARCHAR(25), lastname VARCHAR(25))")
# db_Cursor.execute("CREATE TABLE PlayerStats (number int PRIMARY KEY, FOREIGN KEY(number) REFERENCES Players(jerseynumber), PPG int, FT int)")

def select_all():
    query = "SELECT * FROM PlayerStats"
    db_Cursor.execute(query)
    for x in db_Cursor:
        print(x)

def insert_many(pList = [], sList = []):
    Q1 = "INSERT INTO Players (jerseynumber, firstname,lastname) VALUES (%s,%s,%s)"
    Q2 = "INSERT INTO PlayerStats (number, PPG, FT) VALUES (%s,%s,%s)"
    db_Cursor.executemany(Q1, pList)
    db_Cursor.executemany(Q2, sList)

def insert_many_players(pList = []):
    Q1 = "INSERT INTO Players (jerseynumber, firstname,lastname) VALUES (%s,%s,%s)"
    db_Cursor.executemany(Q1, pList)

def insert_many_stats(sList = []):
    Q2 = "INSERT INTO PlayerStats (number, PPG, FT) VALUES (%s,%s,%s)"
    db_Cursor.executemany(Q2, sList)

def insert_single(player):
    Q1 = "INSERT INTO Players (jerseynumber, firstname, lastname) VALUES (%s,%s,%s)"
    db_Cursor.execute(Q1, player)

def insert_single_stat(stat):
    Q1 = "INSERT INTO PlayerStats (number, PPG, FT) VALUES (%s,%s,%s)"
    db_Cursor.execute(Q1,stat)

def inner_join():
    Q1 = "SELECT Players.firstname as playerfirst, PlayerStats.PPG as gamestat FROM Players INNER JOIN PlayerStats ON Players.jerseynumber = PlayerStats.number"
    db_Cursor.execute(Q1)
    results = db_Cursor.fetchall()
    for x in results:
        print(x)

def left_join():
    Q1 = "SELECT Players.firstname as playerfirst, stats.PPG as gamestat FROM player LEFT JOIN stats ON Players.jerseynumber = PlayerStats.number"
    db_Cursor.execute(Q1)
    results = db_Cursor.fetchall()
    for x in results:
        print(x)

def right_join():
    Q1 = "SELECT Players.firstname as playerfirst, PlayerStats.PPG as gamestat FROM Players RIGHT JOIN PlayerStats ON Players.jerseynumber = PlayerStats.number"
    db_Cursor.execute(Q1)
    results = db_Cursor.fetchall()
    for x in results:
        print(x)

# Delete rows and columns from a table
def delete_from_stats_table():
    db_Cursor.execute("DELETE FROM PlayerStats")

def delete_from_player_table():
    db_Cursor.execute("DELETE FROM Players")

# remove the table from the database
def remove_stats_table():
    db_Cursor.execute("DROP TABLE PlayerStats")

def remove_player_table():
    db_Cursor.execute("DROP TABLE Players")