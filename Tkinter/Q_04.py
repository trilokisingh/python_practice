UserInput = int(input("Dear, which number you want to check : "))


# here we will make a reverse number
def reverse(num):
    if num < 10:
        return num
    else:
        return int(str(num % 10) + str(reverse(num // 10)))  # this will return reverse string wich converted into
        # int latter


# in this function we will chech both reverse and UseInput if equal than palindrome
def CheckIsPalindrome(num):
    if num == reverse(num):
        return True
    return 0


if CheckIsPalindrome(UserInput) == 1:
    print(f" number {UserInput} is a palindrome")
else:
    print(f" sorry number {UserInput} is a not palindrome")
