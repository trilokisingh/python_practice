import tkinter

window = tkinter.Tk()

window.title("My first GUI programm")
window.minsize(height=300,width=500)

# Lable
myLabble = tkinter.Label(text = "Code_x wellcomes You",font = ("Arial", 10, "bold"))
# myLabble.pack()
# myLabble.pack(side ="right")
# myLabble.pack(side ="left")
myLabble.pack(side ="bottom")


window.mainloop()