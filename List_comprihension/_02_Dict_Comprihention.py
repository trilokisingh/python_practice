

dic = {i: f"item {i}" for i in range(20) if (i % 3 == 0)}  # Syntax
print(dic)

dict1 = {value: key for key, value in dic.items()}   # syntax
print(dict1)
