from tkinter import *
window = Tk()
window.title("Multi-User To Do")

# canvas for objects on the screen
canvas = Canvas(window, width=300, height=200)
canvas.pack()

# "Multi-User To Do title
title = canvas.create_text(150, 125, text= 'Multi-User To Do', \
                        font = ('Helvetica', 13))

# register button
registerButton = Button(window, text = "REGISTER", bg = "lightgray")
registerButton.pack()
# login button
loginButton = Button(window, text = "LOGIN", bg = "lightgray")
loginButton.pack()


window.mainloop()
