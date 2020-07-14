from tkinter import *

#this is the function for the "REGISTER" button
def register():
    canvas1 = Tk()
    canvas1.title("REGISTER")
    canvas1 = Canvas(canvas1, width=300, height=200)
    canvas1.pack()

    username = StringVar()
    password = StringVar()

    userInstruct = canvas1.create_text(150,100, text = 'Please enter details below')

    #this is where the user inputs data to register
    usernameLB = canvas1.create_text(150,125, text = 'Username *')
    Entry(canvas1, textvariable = username) # provides a place to accept a value from user
    passwordLB = canvas1.create_text(150, 130, text = 'Password *')
    Entry(canvas1, textvariable = password)

    #this button will submit the provided information
    Button(canvas1, text = "REGISTER", bg = "lightgray", width = 10, height = 1).pack() 
                 
def login():
    print("Login session started")

def mainScreen():
    window = Tk()
    window.title("Multi-User To Do")

    # canvas for objects on the screen
    canvas = Canvas(window, width=300, height=200)
    canvas.pack()

    # "Multi-User To Do title
    title = canvas.create_text(150, 125, text= 'Multi-User To Do', \
                        font = ('Helvetica', 13))
    # register button
    registerButton = Button(window, text = "REGISTER", bg = "lightgray", command = register)
    registerButton.pack()
    # login button
    loginButton = Button(window, text = "LOGIN", bg = "lightgray", command = login)
    loginButton.pack()

    window.mainloop()

mainScreen()
