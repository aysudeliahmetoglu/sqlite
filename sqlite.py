import sqlite3 as sql

# vt=sql.connect('deneme.sqlite')     #-If there is no database named deneme.sqlite in the directory where you gave this command, a database with this name is created.
                                    #If you already have a database file with this name, sqlite3 will connect to that database.
# vt = sqlite3.connect(':memory:')    #-create a SQLite database file on the hard disk-
# vt = sqlite3.connect(':memory:')   #-Creating a temporary database with sqlite3-
# vt = sqlite3.connect('')           #-Creating temporary databases on disk, not on RAM-


vt = sql.connect('veritabani.sqlite')
im = vt.cursor()
# sql=im.execute("""CREATE TABLE 'users'
# ('id', 'first name', last name)""")
# im.execute(sql)

# CREATE TABLE IF NOT EXISTS.  - conditional table creation method-
# sql = """CREATE TABLE IF NOT EXISTS admins
# (id, name, age)"""


create_table = """CREATE TABLE IF NOT EXISTS users
(id,firstname,lastname)"""

insert_value = """INSERT INTO users VALUES ('123','Aysu', 'Deliahmetoglu')"""

# im.execute(create_table)
im.execute(insert_value)
vt.commit()              #In order to process the data we entered into the database
              #closing the database