#Creating A Table:
import sqlite3

# To use the module you must create an object that represents the database
con = sqlite3.connect('example.db')

# Now a cursor can be created to perfrom SQL commands
cur = con.cursor()

# Creating a table
cur.execute('''CREATE TABLE sopranos 
                (first_name, last_name, position)''')

#Insert a row of data 
cur.execute("INSERT INTO sopranos VALUES('Tony', 'Soprano','Boss')")
cur.execute("INSERT INTO sopranos VALUES('Sylvia', 'Dante','Conslierge')")
cur.execute("INSERT INTO sopranos VALUES('Chris', 'Moltisante','Soldier')")



# Save & commit changes
con.commit()


for row in cur.execute('SELECT * FROM sopranos'): 
    print(row)

# When finished calling, modifying or working with the Database
con.close()
