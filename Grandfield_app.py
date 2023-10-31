import Grandfield_functions as gf # I changed the abbreviation from db to gf cause I lookes better

#need to make functions that input data into the databse functions

def user_addMachine():
    location =input("Enter it's location: ")
    status = input("Enter it's status: ")
    machine = gf.addMachine(location, status)
    print(f' ------ Machine {machineKey} has been added.------')

def user_addSoftware():
    softwareName = input("Enter the softare name: ")
    licenseKey = input("Enter the licenseKey of the software")
    licenseStartDate= input("Enter the date when the license starts (YYYY-MM-DD): ")
    licenseEndDate= input("Enter the date when the license will End (YYYY-MM-DD): ")
    price = input("Enter the price: ")
    pricingUnit = input("Enter the pricing unit: ")
    availabilitystatus = input("Enter whether software is available or not: ")
    software = gf.addSoftware(softwareName, licenseKey ,licenseStartDate ,licenseEndDate ,price , pricingUnit , availabilitystatus)
    print(f'-------- Software {softwareName} has been added. ----------')

def user_addMachineSoftware():
    machineKey = input = ('Enter the machine Key: ')
    softwareKey = input("Enter the software Key: ")
    dateInstalled = input("Enter the date the software was installed (YYYY-MM-DD hh:mm:ss): ")
    dateUninstalled = input("Enter the date the software was unistalled (YYYY-MM-DD hh:mm:ss) Leave empty if not known: ")
    machinesoftware = gf.addMachineSoftware(machineKey,softwareKey, dateInstalled, dateUnistalled)
    print(f'----------A machine software {machineKey} and software {softwareKey} has been added. ---------')


def user_addSoftwareRequest():
    requestdate = input('Enter the request date: ')
#     print("Date will be automatically inserted when request is made")
    softwareName = input('Enter the software name: ')
    reason = input ('Enter the reason: ')

    if requestdate and softwareName and reason:
        softwarerequest = gf.addSoftwareRequest(requestdate,softwareName,reason,USERKEY)
        print(f'-----------software request {softwareName} has been added.----------')
    else:
        print("This did not work!")

def user_addUser():
    userName = input('Enter your userName: ')
    email = input('Enter your email address: ')
    password = input('Enter your password: ')
    userID = gf.addUser(userName,email , password)
    print(f'-------------User {userName} has been added. User ID is {userID}-----------')
def user_addUserAccess():
    userKey= input('Enter the user Key:  ')
    print("List of Access \n Access Types: \n 1)Instructor access \n 2)Adminstrative access \n 3)IT staff access \n 4)software management access \n 5)legal advisor access \n")
    accessKey = input('Enter the access Key: ')
    UserAccess = gf.addUserAccess(userKey,accessKey)
    print(f'-----------User access {userKey} has been added.------------')
def user_addMachineAccess():
# machine key duplicate?
    machinekey= input('Enter machine Key: ')
    accessKey = input('Enter the access key: ')
    machineaccess = gf.addMachineAccess(machinekey,accessKey)
    print(f'-------------Machine access {accessKey} has been added-------------')

def user_updateUserAccess():
    accessKey = input('Enter updated access Key : ')
    userKey = input('Enter updated user key: ')
    updateduseraccess = gf.updateUserAccess(accessKey, userKey)
    print(f'------------Updated user acess {accessKey} has been added.-----------------')
def user_updateMachineAccess():
    machineKey = input('Enter the updated machine Key: ')
    accessKey = input('Enter the updated access Key: ')
    updatedmachineaccess = gf.updateMachineAccess (machineKey, accessKey)
    print(f'-----------Updated user access {accessKey} has been added.-------------')
def user_updateUser():
    email= input('Enter the updated user email: ')
    password = input('Enter the update user password: ')
    updateduser = gf.updateUser(email, password)
    print(f'----------Updated User email {email} and {password} has been added.------------')
    
def user_updateSoftwareRequest():
    requestKey = int(input("Enter the request Key you want to respond to: "))
    response = input("Enter your response to the request here: ")
    responseDate = input("Date (yyyy-mm-dd hh:mm:ss): ")
    status = input("Enter status (approved, pending, rejected): ")
    if status.lower() =="approved" or status.lower() == "pending" or status.lower() == "rejected":
        updatedrequest = gf.updateSoftwareRequest(requestKey, response, responseDate, status)
    else:
        return
    print(f'------------Updated Software Request with status {status}. ---------')
    

def user_viewSoftware():
    viewing = gf.viewSoftware()
    print(f'--------You can view software.---------')

def user_viewMachine():
    machineview = gf.viewMachine()
    print(f'-------you can view machine.----------')
def user_viewSoftwareRequest():
    viewingsoftwaerrequest = gf.viewSoftwareRequest()
    print(f'---------You can view Software Request.--------------')
def user_viewUser():
    Viewinguser = gf.viewUser()
    print(f'----------You can View user-----------')
def user_viewLicenseType():
    viewingLT = gf.viewLicenseType()
    print(f'---------------You can view License Type.----------------------')
def user_viewUserAccess():
    viewingUserAccess = gf.viewUserAccess()
    print(f'---------------You can view User access.----------------')
def user_viewMachineSoftware():
    viewingMachineSoftware = gf.viewMachineSoftware()
    print(f'--------------You can view machine software--------------')

def main():
    """
    Access Types:
    1)Instructor access
    2)Adminstrative access
    3)IT staff access
    4)software management access
    5)legal advisor access
   """


    email = input("Enter your email/username, please! -------- ")

    password = input("Enter your password,  please! --------- ")
    access = ''
    if not gf.determineAccess(email,password):
        print("Invalid user details")
        return
    else:
        access = gf.determineAccess(email,password)[0][0]

        global USERKEY
        USERKEY = gf.determineAccess(email,password)[0][1]

        global EMAIL
        EMAIL = email

        global PASSWORD
        PASSWORD = password

    # Tables in database
    # Access               Software             UserSoftwareRequest
    # Machine              SoftwareRequest      licenseType
    # MachineAccess        User                 MachineSoftware
    # UserAccess
    if access == 2: # Instructor access
        #take input of which table they want to see
        #select
        print("This user can only select from specific tables in the database")
        print("Tables to View \n -----------------------")
        tablechoice = input("""Enter which table you want to view?
        1) Machine
        2) Software
        3) User
        4) License Type
        5) Machine Software relation
        6) User Access
        7) Machine Access
        8) Access Types
        9) Software Requests
        : """)
        userOption(tablechoice, 2)

    elif access == 1: # Instructor access
        # take input of whether they want to request software or look at the softwares available table 
        # call the addSoftwareRequest function
        choice = input("""Enter your choice:
        1) if you would like to view the available softwares table 
        2) if you would like to make a request for a new software not available currently
        """)
        if int(choice) == 1:
             displayData(gf.viewSoftware(access))
        else:
            user_addSoftwareRequest()

    elif access == 3: # IT staff access
        # ask what action they want to perform with the database 
        # call functions (addUser, addUserAccess, addMachine, addMachineAccess, addMachineStatus, updateUser, updateUserAccess) based on their choice
        choice = input("""Enter the task you want to complete: 
        1) view table
        2) Add a user
        3) Add an access type for a user
        4) Add Access types for a machine
        5) Add Machine status 
        6) Update User information
        7) Update User Access
        """) 
        choice = int(choice)
        # do we also need an update function for the machine status? yes
        if choice == 1:
            tablechoice = input("""Enter the table you want to view: 
        1) Machine
        2) Software
        3) User
        4) License Type
        5) Machine Software relation
        6) User Access
        7) Machine Access
        8) Access Types
        : """)
            userOption(tablechoice, access)
        elif choice == 2:
            user_addUser()
        elif choice == 3:
            user_addUserAccess()
        elif choice == 4:
            user_addMachineAccess()
        elif choice == 5:
            user_addMachineStatus()
        elif choice == 6:
            user_updateUser()
        elif choice == 7:
            user_updateUserAccess()
        else: 
            print("Please Try again with the correct input.")
            

    elif access == 4: # Software Management Access
        #ask what action they want to perform with the database 
        #call functions addSoftwareRequest, addSoftware,addMachineSoftware based on their choice
        choice = input("""Enter your choice of tasks to complete? 
        1) view a table
        2) Respond to a software request
        3) Add a software information to the software data
        4) Add a Software that is installed in a machine
        """)
        choice = int(choice)

        if choice == 1:
            tablechoice = input("""Enter the table you want to view: 
         1) Machine
        2) Software
        3) User
        4) License Type
        5) Machine Software relation
        6) User Access
        7) Machine Access
        8) Access Types
        9) Software Requests
        : """)
            userOption(tablechoice, access)
        elif choice == 2:
            print("Here are the requests with no response yet: ")
            displayData(gf.getNullResponse())
            user_updateSoftwareRequest()
        elif choice == 3: 
            user_addSoftware()
        elif choice ==4: 
            user_addMachineSoftware()
        else: 
            print("Try again with a correct input.")



    elif access == 5: # Legal advisor access
        #select software table only for viewing. 
        choice = input("""Which table would you like to view:
        1) Software
        2) License Type
        """)
        choice = int(choice)
        if choice ==1: 
            displayData(gf.viewSoftware(access))
        elif choice == 2:
            displayData(gf.viewLicenseType())
        else: 
            print("Try again with a correct input")

    else:
        print("Invalid email/password!!!!!!")

def userOption(tablechoice,access): # This function makes the user select the table to select.
    tablechoice = int(tablechoice)
    if access == 2 or access == 4 :
        if tablechoice == 1:
            displayData(gf.viewMachine())
        elif tablechoice ==2:
            displayData(gf.viewSoftware(access))
        elif tablechoice ==3:
            displayData(gf.viewUser())
        elif tablechoice==4:
            displayData(gf.viewLicenseType())
        elif tablechoice ==5:
            displayData(gf.viewMachineSoftware())
        elif tablechoice ==6:
            displayData(gf.viewUserAccess())
        elif tablechoice == 7:
            displayData(gf.viewMachineAccess())
        elif tablechoice == 8:
            displayData(gf.viewAccessTypes())
        elif tablechoice == 9:
            displayData(gf.viewSoftwareRequest())
        else:
            print("Try again with a correct input! Can't access table")


    elif  access == 3:
        if tablechoice == 1:
            displayData(gf.viewMachine())
        elif tablechoice ==2:
            displayData(gf.viewSoftware(access))
        elif tablechoice ==3:
            displayData(gf.viewUser())
        elif tablechoice==4:
            displayData(gf.viewLicenseType())
        elif tablechoice ==5:
            displayData(gf.viewMachineSoftware())
        elif tablechoice ==6:
            displayData(gf.viewUserAccess())
        elif tablechoice == 7:
            displayData(gf.viewMachineAccess())
        elif tablechoice == 8:
            displayData(gf.viewAccessTypes())
        else:
            print("Try again with a correct input! Can't access table")
            
    else:
        print("We apologize. It seems like you don't have access to this part of the database.")

def displayData(result):
    for item in result:
        row = "{:<30}" *len(item)
        if None in item:
            print(item)
        else:
            print(row.format(*item))
main()


