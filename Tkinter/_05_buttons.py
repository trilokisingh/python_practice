from tkinter import *

win = Tk()
win.title("BOTTONS")
win.minsize(height=300, width=500)
my_label = Label(text= " wellcome")#same
my_label.config(text ="I LOVE YOU !")#same and overwrite
my_label.pack()


def onclicked():
    print("Ohh i got clicked ")
    #my_label.config(text= "I HATE YOU !!!") # if button clicked this line will sow
    new_text =input.get()
    my_label.config(text=new_text)# if button clicked input line will   will sow

# button
button = Button(text="click me !", command=onclicked)
button.pack()

# entry_component
input = Entry(width= 25)
input.pack()


win.mainloop()