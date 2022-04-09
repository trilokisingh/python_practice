
# def sum(num,**kwargs):
#
#     print(kwargs)
#     num  +=kwargs["add"]
#     num *= kwargs["multi"]
#     print(num)
#
# sum(2,add = 12, multi = 4) # will pass one normal var and a in form of dict.


class car:
    def __init__(self,**args):
        self.name =args["name"]  # will give the value which is stored in name
        self.model =args["model"]
        self.price =args["price"]
        self.color = args.get("color")  # get method is use if key is not found in args than it will return none


my_car =car(name="bmw", model="2022",price=9815851)
my_car2 =car(name="jaguar", model="2021",price=7815851 ,color="red")
print(my_car.price)

print(my_car.name)
print(my_car.model)
print(my_car.color)  # here key will not found it will return none 
print("\n\n")
print(my_car2.price)
print(my_car2.name)
print(my_car2.model)
print(my_car2.color)