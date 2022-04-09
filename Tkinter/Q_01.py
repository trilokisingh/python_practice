def isOdd(num):
    N = 1   # N is for iteration
    if num >= N:
        print(f"the even number is  = {num-1}\n")
        isOdd(num - 2)  # this is the recursive call


isOdd(100) # here we are calling the function and passing the arguments
print("Thankyou")