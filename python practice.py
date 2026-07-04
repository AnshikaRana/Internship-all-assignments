#1 Function to print a welcome messagge
def welcome():
    print("Welcome to python programming")

welcome()

#2 Function to add two numbers
def add(a,b):
    return a + b
result = add(5,10)
print(result)

#3 Function to check odd or even number
def check_even_odd(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"
print (check_even_odd(44))

#4 Function to find square of a number
def square(num):
    return num ** 2
print (square(5))

#5 Function to find maximum of two numbers
def maximum(a,b):
    if a > b:
        return a
    else:
        return b
print(maximum(16,61))