import sqlite3

####################
# Tables in database
####################
# Access               Software             UserSoftwareRequest
# Machine              SoftwareRequest      licenseType
# MachineAccess        User                 MachineSoftware
# UserAccess

##############################
# Add data to Tables Functions
##############################

def addMachine(location, status):
    # Add new Machihe

    # Create a connection to the database
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object
    cur = conn.cursor()

    # Turn on foreign_key constraints
    cur.execute("PRAGMA foreign_keys = ON;")

    # insert the new machine into the database:
    cur.execute("INSERT INTO Machine VALUES (? ,?);", (location, status))

    # Commit (i.e. save) the changes
    conn.commit()

    # Close the connection
    conn.close()

def addSoftware(softwareName, licenseKey ,licenseStartDate ,licenseEndDate ,price , pricingUnit , availability):
    # Add new Software
    
    # Create a connection to the database
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object
    cur = conn.cursor()
    
    # Turn on foreign_key constraints
    cur.execute("PRAGMA foreign_keys = ON;")

    # Insert the new software into the database:
    cur.execute("INSERT INTO Software (softwareName, licenseKey ,licenseStartDate ,licenseEndDate ,price , pricingUnit , availability) VALUES ( ?, ?, ?, ?,?,?,?);",(
  softwareName ,
  licenseKey ,
  licenseStartDate ,
  licenseEndDate ,
  price ,
  pricingUnit ,
  availability))

    # Commit (i.e. save) the changes
    conn.commit()

    # Close the connection
    conn.close()#CORRECT

def addMachineSoftware(machineKey, softwareKey, dateInstalled ,dateUninstalled):
    # Add link between Machine and Software
    
    # Create a connection to the database
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object
    cur = conn.cursor()
    
    # Turn on foreign_key constraints
    cur.execute("PRAGMA foreign_keys = ON;")

    # insert the new link between Machine and Software into the database:
    cur.execute("INSERT INTO Software VALUES (?,?,?,?);",(
  machineKey,
  softwareKey,
  dateInstalled ,
  dateUninstalled ))

    # Commit (i.e. save) the changes
    conn.commit()

    # Close the connection
    conn.close()#CORRECT

def addSoftwareRequest(requestdate,softwareName,reason,userKey):
    # Add software request

    # Create a connection to the database
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object
    cur = conn.cursor()
    
    # Turn on foreign_key constraints
    cur.execute("PRAGMA foreign_keys = ON;")

    # insert the new link between Request and Software into the database:
    cur.execute("INSERT INTO SoftwareRequest (requestdate,  softwareName , reason) VALUES (?, ?, ?);",(
  requestdate,
  softwareName,
  reason
  ))

    # Commit (i.e. save) the changes
    conn.commit()

    # Close the connection
    conn.close()
    
    #get last row id 
    reqKey = cur.lastrowid
    
    #Add usersoftwarerequest table
    addUserSoftwareRequest(userKey,reqKey)

def addUser(userName,email , password):
    # Add New users

    # Create a connection to the database
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object
    cur = conn.cursor()

    # Turn on foreign_key constraints
    cur.execute("PRAGMA foreign_keys = ON;")

    # Insert the user:
    cur.execute("INSERT INTO User ('userName','email','password') VALUES (?, ?, ?);",(userName,
  email ,
  password ))

    # Commit (i.e. save) the changes
    conn.commit()

    # Close the connection
    conn.close()
    
    result = cur.lastrowid
    
    return result

def addUserAccess(userKey,accessKey):
    # Add user access by IT Admin
    
    # Create a connection to the database
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object
    cur = conn.cursor()
    
    # Turn on foreign_key constraints
    cur.execute("PRAGMA foreign_keys = ON;")

    # Insert the new User Access:
    cur.execute("INSERT INTO UserAccess VALUES (?, ?);",(
 userKey,
  accessKey))

    # Commit (i.e. save) the changes
    conn.commit()

    # Close the connection
    conn.close()

def addMachineAccess(machinekey,accessKey):
    # Add machine access
    
    # Create a connection to the database
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object
    cur = conn.cursor()
    
    # Turn on foreign_key constraints
    cur.execute("PRAGMA foreign_keys = ON;")

    # insert the new Machine Access:
    cur.execute("INSERT INTO MachineAccess VALUES (?, ? );",(
 machinekey,
  accessKey))

    # Commit (i.e. save) the changes
    conn.commit()

    # Close the connection
    conn.close()

def addUserSoftwareRequest(userKey,requestKey):
    # Add new Link between User and softwareRequest
    # UserSoftwareRequest
    
    # Create a connection to the database
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object
    cur = conn.cursor()
    
    # Turn on foreign_key constraints
    cur.execute("PRAGMA foreign_keys = ON;")

    # insert the new link between user and softwareRequest:
    cur.execute("INSERT INTO UserSoftwareRequest VALUES (?, ? );",(
 userKey,
  requestKey))

    # Commit (i.e. save) the changes
    conn.commit()

    # Close the connection
    conn.close()

########################################
# Get Specific data from table Functions
########################################

def getRequestKey(requestdate, softwareName ,  reason ,  response, responseDate,  status):
    # Get the request key will be used in linking user to softwareRequest
    
    # Create a connection to the database
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object
    cur = conn.cursor()

    # Turn on foreign_key constraints
    cur.execute("PRAGMA foreign_keys = ON;")

    # Select the new software request made by User from SoftwareRequest in the database:
    cur.execute("SELECT softwareKey FROM SoftwareRequest WHERE requestdate = ? and softwareName = ? and softwareName = ? and reason = ? and response = ? responseDate = ? and status = ?;",(
  requestdate,
  softwareName ,
  reason ,
  response,
  responseDate,
  status))

    #get results in variable result
    result = cur.fetchall()
    
    # Commit (i.e. save) the changes
    conn.commit()

    # Close the connection
    conn.close()
    
    return result

def getUserKey(email,password):
    # Get user key
    
    # Create a connection to the database
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object
    cur = conn.cursor()
    # Turn on foreign_key constraints
    cur.execute("PRAGMA foreign_keys = ON;")

    # Select userkey from the database:
    cur.execute("SELECT userkey FROM User WHERE email = ? and password = ?;",(
  email,
  password))

    #get results in variable result
    result = cur.fetchall()
    # Commit (i.e. save) the changes
    conn.commit()

    # Close the connection
    conn.close()

    return result

def getNullResponse():
    # Get software request with null response
    
    # Create a connection to the database
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object
    cur = conn.cursor()
    # Turn on foreign_key constraints
    cur.execute("PRAGMA foreign_keys = ON;")

    # Select userkey from the database:
    cur.execute("SELECT * FROM SoftwareRequest WHERE response IS NULL ;") #OR responseDate IS NULL OR status IS NULL

    #get results in variable result
    result = cur.fetchall()
    # Commit (i.e. save) the changes
    conn.commit()

    # Close the connection
    conn.close()

    return result

#########################
# Tables Functions
#########################
    
def updateUserAccess(accessKey, userKey):
    # Update the user access by IT admin
    
    # Create a connecti on to the database
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object
    cur = conn.cursor()
    
    # Turn on foreign_key constraints
    cur.execute("PRAGMA foreign_keys = ON;")

    # Update the User Access into the database:
    cur.execute("UPDATE userAccess SET accessKey= ? WHERE userKey = ?;",(
  accessKey ,
  userKey))

    # Commit (i.e. save) the changes
    conn.commit()

    # Close the connection
    conn.close()

def updateMachineAccess (machineKey, accessKey):
    '''Update Machine Access by IT admin'''

    # Create a connection to the database
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object
    cur = conn.cursor()
    
    # Turn on foreign_key constraints
    cur.execute("PRAGMA foreign_keys = ON;")

    # insert the new link between Machine and Software into the database:
    cur.execute("UPDATE userAccess SET accessKey= ? WHERE machineKey = ?;",(
 machineKey,
  accessKey))

    # Commit (i.e. save) the changes
    conn.commit()

    # Close the connection
    conn.close()
        
def updateUser(email, password):
    # Update users information

    # Create a connection to the database
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object
    cur = conn.cursor()

    # Turn on foreign_key constraints
    cur.execute("PRAGMA foreign_keys = ON;")

    # Update the user data:
    cur.execute("UPDATE User SET password = ? WHERE email = ? ;",(
 password,
  email ))

    # Commit (i.e. save) the changes
    conn.commit()

    # Close the connection
    conn.close()

def determineAccess(email, password):
    # Determine the user access
    
    # Create a connection to the database
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object
    cur = conn.cursor()

    # Turn on foreign_key constraints
    cur.execute("PRAGMA foreign_keys = ON;")
    
    # select accesskey from the User Access table in database:
    cur.execute("SELECT accessKey,userKey FROM UserAccess WHERE userKey = (SELECT userKey FROM User WHERE (email = ? or userName = ?) and password = ? );",(email,email ,  password ))

    # results
    result = cur.fetchall()

    # Commit (i.e. save) the changes
    conn.commit()

    # Close the connection
    conn.close()

    return result

def updateSoftwareRequest(requestKey,response,responseDate,status):
    # Update Software Request
    
    # Create a connection to the database
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object
    cur = conn.cursor()

    # Turn on foreign_key constraints
    cur.execute("PRAGMA foreign_keys = ON;")
    
    # UPDATE SOFTWARE REQUEST :
    cur.execute("UPDATE SoftwareRequest set response = ? , responseDate=?, status=? WHERE requestKey =  ? ;",(response, responseDate ,  status,requestKey ))

    # Commit (i.e. save) the changes
    conn.commit()

    # Close the connection
    conn.close()


#######################
# View tables Functions
#######################

def viewSoftware(access):
    # View software

    # Create a connection to the database
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object
    cur = conn.cursor()

    # Turn on foreign_key constraints
    cur.execute("PRAGMA foreign_keys = ON;")

    # insert the software:
    if access == 1 or access == 5:
        cur.execute("SELECT softwareKey, softwareName FROM Software;")
    else:
        cur.execute("SELECT * FROM Software;")

    # Commit (i.e. save) the changes
    conn.commit()
    
    # results
    result = cur.fetchall()

    # Close the connection
    conn.close()
    
    return result

def viewMachine():
    # View software

    # Create a connection to the database
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object
    cur = conn.cursor()

    # Turn on foreign_key constraints
    cur.execute("PRAGMA foreign_keys = ON;")

    # insert the user:
    cur.execute("SELECT * FROM Software;")

    # Commit (i.e. save) the changes
    conn.commit()
    
    # results
    result = cur.fetchall()
    

    # Close the connection
    conn.close()
    
    return result

def viewSoftwareRequest():
    # View software

    # Create a connection to the database
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object
    cur = conn.cursor()

    # Turn on foreign_key constraints
    cur.execute("PRAGMA foreign_keys = ON;")

    # insert the user:
    cur.execute("SELECT * FROM SoftwareRequest;")

    # Commit (i.e. save) the changes
    conn.commit()
    
    # results
    result = cur.fetchall()
    

    # Close the connection
    conn.close()
    
    return result

def viewUser():
    # View User Function

    # Create a connection to the database:
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object:
    cur = conn.cursor()

    # Turn on foreign_key constraints:
    cur.execute("PRAGMA foreign_keys = ON;")

    # Get all the users:
    cur.execute("SELECT * FROM User;")

    # Commit (i.e. save) the changes
    conn.commit()
    
    #results
    result = cur.fetchall()
    

    # Close the connection
    conn.close()
    
    return result

def viewLicenseType():
    # View License Type

    # Create a connection to the database:
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object:
    cur = conn.cursor()

    # Turn on foreign_key constraints:
    cur.execute("PRAGMA foreign_keys = ON;")

    # Get all the license types avaliable:
    cur.execute("SELECT * FROM licenseType;")

    # Commit (i.e. save) the changes
    conn.commit()
    
    #results
    result = cur.fetchall()
    

    # Close the connection
    conn.close()
    
    return result

def viewUserAccess():
    # View User Access

    # Create a connection to the database:
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object:
    cur = conn.cursor()

    # Turn on foreign_key constraints:
    cur.execute("PRAGMA foreign_keys = ON;")

    # Get all the license types avaliable:
    cur.execute("SELECT U.userName, A.accessType FROM User AS U JOIN UserAccess AS UA ON u.userKey = UA.userKey JOIN Access AS A ON A.accessKey = UA.accessKey;")
    
    # Commit (i.e. save) the changes
    conn.commit()
    
    #results
    result = cur.fetchall()

    # Close the connection
    conn.close()
    
    return result

def viewMachineSoftware():
    # View Machine Software

    # Create a connection to the database:
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object:
    cur = conn.cursor()

    # Turn on foreign_key constraints:
    cur.execute("PRAGMA foreign_keys = ON;")

    # Get all the license types avaliable:
    cur.execute("SELECT M.machineKey, MS.softwareKey FROM Machine AS M JOIN MachineSoftware AS MS ON MS.machineKey = M.machineKey JOIN Software AS S ON S.softwareKey = MS.softwareKey;")
    
    # Commit (i.e. save) the changes
    conn.commit()
    
    # results
    result = cur.fetchall()

    # Close the connection
    conn.close()
    
    return result

def viewAccessTypes():
    # View Access Types

    # Create a connection to the database:
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object:
    cur = conn.cursor()

    # Turn on foreign_key constraints:
    cur.execute("PRAGMA foreign_keys = ON;")

    # Get all the access types avaliable:
    cur.execute("SELECT * FROM Access;")
    
    # Commit (i.e. save) the changes
    conn.commit()
    
    # results
    result = cur.fetchall()

    # Close the connection
    conn.close()
    
    return result

def viewMachineAccess():
    # View machine Access

    # Create a connection to the database:
    conn = sqlite3.connect('Grandfield.db')

    # Create a cursor object:
    cur = conn.cursor()

    # Turn on foreign_key constraints:
    cur.execute("PRAGMA foreign_keys = ON;")

    # Get all the machine and access:
    cur.execute("SELECT U.userName, A.accessType FROM Machine AS M JOIN UserAccess AS UA ON u.userKey = UA.userKey JOIN Access AS A ON A.accessKey = UA.accessKey;")
    
    # Commit (i.e. save) the changes
    conn.commit()
    
    #results
    result = cur.fetchall()

    # Close the connection
    conn.close()
    
    return result

