def IsEven(i, N):
    if i <= N:
        print(f"the even value is {i+1}\n")
        IsEven(i + 2, N)  # here recursive call is done


initial = 100
IsEven(1, initial)  # here 1 is for iteration
