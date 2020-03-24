# Recursion is just a function that calls itself

# Example: 
def Print1ToNum(num):
    if num == 1:
        print(1)
        return
    Print1ToNum(num - 1)    
    print(num)
    return

Print1ToNum(10)

# Algorithm for recursively solving the sigma (or summation)
# of a number
# i.e. Sigma(4) = 4 + 3 + 2 + 1 => 10
def Sigma(num):
    if num == 1:
        return num
    num += Sigma(num-1)
    return num


def Factorial(num):
    # write a factorial function using recursion, where Factorial(num) will return the 
    # factorial of that number. Example: 4! = 4 * 3 * 2 * 1 || 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1
    pass