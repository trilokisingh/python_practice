from tkinter import *

window = Tk()
window.title("code_x is here !")
window.minsize(width=500, height=300)

# lable
position = Label(text= "miss you 1")
position.pack()

# position.pack(side = "left")

def onclicked():
    print("Hey you clicked me")


# Button
button = Button(text= "click me !",bg= "pink",command = onclicked)# command method will  call the function by putting funct name only not()
button.pack()



window.mainloop()