import pandas
dict ={
    1:"amit",
    2:"vijay",
    3:"chaman",
    4:"raman",
    5:["a","b","c","d"]
}
# for key,value in dict.items():
#     print(key,value)


Dict_datfram  =  pandas.DataFrame(dict)

print(Dict_datfram)


# DataFArame

Score = {
    "name":["A","B","C","D","E","F"],
    "marks":[15,85,74,15,63,136],
    "section":["gr","rfg","jf","lkj","ufhu","uhiu"]
}

result = pandas.DataFrame(Score)

print(result)

# loop through dataFrame
for key,value in result.items():
    print(value)
  


