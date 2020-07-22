from tkinter import *
import os #operating system

#this is the function for the register page button
def registerUser():

    #returns the value of the item with the specified key.
    usernameInfo = username.get()
    passwordInfo = password.get()
    
    #opens file for writing, creates file if non-existant
    file = open(usernameInfo+".txt", "w")
    file.write(usernameInfo+"\n")
    file.write(passwordInfo+"\n")
    file.close()

    #clears the field after user completes registry
    userInp.delete(0, END)
    passInp.delete(0, END)

    # signal that the registration is complete
    regCompl = Label(regScreen, text = "registration complete", fg = "green", font = ("calibri", 11))
    regCompl.pack()
 
#this is the function for the opening screen "REGISTER" button   
def register():
    global regScreen
    regScreen = Tk()
    regScreen.title("REGISTER")
    regScreen.geometry("400x350")

    #allows variables to be used outside the function
    global username
    global password
    
    # Holds a string; the default value is an empty string
    username = StringVar()
    password = StringVar()

    # text for instructions
    userRegInstruct = Label(regScreen, text = 'Please enter details below', font = ("calibri", 11))
    userRegInstruct.pack(pady=10)

    #this is where the user inputs data to register
    usernameLB = Label(regScreen, text = 'Username *', font = ("calibri", 9))
    usernameLB.pack()
    global userInp
    userInp = Entry(regScreen, textvariable = username) # provides a place to accept a value from user (grabs info from StringVar()
    userInp.pack()
    
    passwordLB = Label(regScreen, text = 'Password *', font = ("calibri", 9))
    passwordLB.pack()
    global passInp
    passInp = Entry(regScreen, textvariable = password)
    passInp.pack()

    #this button will submit the provided information
    regButton = Button(regScreen, text = "REGISTER", bg = "lightgray", width = 10, height = 1, font = ("calibri", 9), command = registerUser)
    regButton.pack(ipady=2, ipadx = 2, pady=15)

# function for login page button
def verifyLogin():
    # to verify whether the username is in the system
    usernameVerify = username2.get()
    passwordVerify = password2.get()

    #clears the field after user completes login
    usernameLogEntry.delete(0, END)
    passwordLogEntry.delete(0, END)

    # lists all files (aka the usernames and passwords) in the current directory as a list
    listOfFiles = os.listdir()
    if username2 in listOfFiles:
        loginFile = open(username2, "r") # string will be read
        verify = loginFile.read().splitlines()
        if password2 in verify:
            print("login success")
        else:
            print("unidentified password")
    else:
        print("User not found")
    
    
def login():
    global loginScreen
    loginScreen = Tk()
    loginScreen.title("LOGIN")
    loginScreen.geometry("400x350")

    global username2
    global password2
    
    # Holds a string; the default value is an empty string
    username2 = StringVar()
    password2 = StringVar()

    # text for instructions
    userLogInstruct = Label(loginScreen, text = "Please enter details below", font = ("calibri", 11))
    userLogInstruct.pack(pady=10)

    # user inserts username and password here
    usernameLBLog = Label(loginScreen, text = 'Username *', font = ("calibri", 9))
    usernameLBLog.pack()
    global usernameLogEntry
    usernameLogEntry = Entry(loginScreen, textvariable = username2)
    usernameLogEntry.pack()
    
    passwordLBLog = Label(loginScreen, text = 'Password *', font = ("calibri", 9))
    passwordLBLog.pack()
    global passwordLogEntry
    passwordLogEntry = Entry(loginScreen, textvariable = password2)
    passwordLogEntry.pack()

    # login button
    logButton = Button(loginScreen, text = "LOGIN", bg = "lightgray", width = 10, height = 1, font = ("calibri", 9), command = verifyLogin)
    logButton.pack(ipady=2, ipadx = 2, pady=15)
    

#function for the opening screen
def mainScreen():
    window = Tk()
    window.title("Multi-User To Do")
    window.geometry("400x350")

    # "Multi-User To Do title
    title = Label(window, text= 'Multi-User To Do', font = ("calibri", 15))
    title.pack(pady=20)
    
    # login button
    loginButton = Button(window, text = "LOGIN", bg = "lightgray", height = 2, width = 30, font = ("calibri", 11), command = login)
    loginButton.pack()

    # register button
    registerButton = Button(window, text = "REGISTER", bg = "lightgray", height = 2, width = 30, font = ("calibri", 11), command = register)
    registerButton.pack(pady = 10)

    window.mainloop()

mainScreen()

