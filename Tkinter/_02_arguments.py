# # # def add(*args): # *args can receve lort of arguments
# # #     sum = 0;
# # #     for i in args:
# # #         sum += i
# # #
# # #     return sum
# # #
# # # print(add(4,5,8,10))
# # #
# # # print(add(1,2,5,8,8,5,5,5,2,4,3)) # we can pass any number of arguments
# #
# #
# # # kwargs    keyword arguments
# #
# # def name(**kwargs):
# #     for key, value in kwargs.items():
# #         print(key, value)
# #
# #
# # detail = {"naman": "etawah",
# #           "aman": "delhi",
# #           "vijay": "kanpur ",
# #           "age":[10, 15, 42, 14]}
# #
# # name(**detail)
#
# def name(**kwargs):
#     for i,j in kwargs.items():
#         print(i,j)
#
#
# names ={ "aman":1,"chaman":2,"raman":3}
#
# name(**names)
#
#
#
#
import tkinter
win = tkinter.Tk()
win.title("Gui programm")
win.minsize(height=300, width=200)

greet = tkinter.Label(text= "hello alls",font = ("arial",24))
greet.pack(side = "top")
win.mainloop()
