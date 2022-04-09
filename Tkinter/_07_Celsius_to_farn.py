from tkinter import*
window = Tk()
window.title("Wellcome")
window.minsize(width=200,height=200)
window.config(padx=10, pady=20)

# this is the function will call on button press
def celtoFarn():
    cel = float(input.get())
    far =(cel*1.8)+32
    result_lable.config(text=f"{far}")



input = Entry(width=12)
input.get()
input.grid(column=2, row= 1)

greet_lab =Label(text ="CELSIUS TO FAHRENHEIT ")
greet_lab.grid(column = 2, row=0)
greet_lab.config( pady=2)
greet_lab.config(font = "Didot")

celcius_lable = Label(text="CELSIUS")
celcius_lable.grid(column =3, row=1)
celcius_lable.config(padx=10, pady=20)

is_equal_lable= Label(text="IS EQUAL TO ")
is_equal_lable.grid(column =1, row=3)
is_equal_lable.config(padx=10, pady=20)

result_lable=Label(text="0")
result_lable.grid(column=2, row=3)
result_lable.config(padx=10, pady=20)

fornehite_lable =Label(text="FARNEHITE")
fornehite_lable.grid(column =3, row=3)
fornehite_lable.config(padx=10, pady=20)

calculate = Button(text="CALCULATE", command=celtoFarn)
calculate.grid(column =2, row=4)
calculate.config(padx=10, pady=20)


window.mainloop()