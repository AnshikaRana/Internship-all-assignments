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

#6 Function to find the factorial of a number
def factorial(num):
    result = 1
    for i in range (1, num + 1):
        result *= i

    return result
print(factorial(4))

#7 Function to count vowels
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0

    for char in string:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Python Programming"))

#8 Function to find largest element in a list
def largest_element(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
    return largest

print(largest_element([12, 45, 8, 67, 23]))