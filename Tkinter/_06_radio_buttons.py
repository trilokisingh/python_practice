from tkinter import *

window = Tk()
window.title("RADIO BUTTONS")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

# label
my_lable = Label(text = " HI THERE")
#my_lable.pack()
#my_lable.place(x=0,y= 0)
my_lable.grid(row =0, column=3)
my_lable.config(padx=5,pady=5)

# button
button = Button(text = "click me ")
button.grid(row=3, column= 2)
button.config(padx=5,pady=5)

button2 =Button(text="im second Button")
button2.grid(row =7, column= 3)
button2.config(padx=5,pady=5)  # will add space arround the buttons
#button.pack()


input = Entry()
input.get()
input.grid(row= 7, column=1)
window.mainloop()