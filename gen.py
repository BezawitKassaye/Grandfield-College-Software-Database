import sqlite3

arr=["UserAccess","MachineAccess","SoftwareRequest","UserSoftwareRequest"]

def getData(tableName):
    # Add new Machihe

    # Create a connection to the database
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object
    cur = conn.cursor()

    # Turn on foreign_key constraints
    cur.execute("PRAGMA foreign_keys = ON;")

    # insert the new machine into the database:
    cur.execute(f"SELECT * FROM {tableName} ;")

    # Commit (i.e. save) the changes
    conn.commit()

    result = cur.fetchall()

    # Close the connection
    conn.close()

    return result



def insertIntoFile():
    f = open("data.txt","a")
    for table in arr:
        data = getData(table)
        for d in data:
            f.write(str(d).strip("()"))
            f.write("\n")
        f.write("\n")
    f.close()

insertIntoFile()