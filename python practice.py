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

#9 Function to find frequency of an element
def frequency(numbers, element):
    count = 0

    for num in numbers:
        if num == element:
            count += 1
    return count

print(frequency([1, 2, 3, 4, 2, 5, 2], 2))

#10 Function to reverse a string
def reverse_string(string):
    return string[::-1]

print(reverse_string("Anshika"))

#11 Function to find prime numbers up to n
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
        
    return True
print(is_prime(23))

#12 Function to seperate Even and Odd Numbers
def separate_even_odd(numbers):
    even = []
    odd = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return even, odd

even, odd = separate_even_odd([1, 2, 3, 4, 5, 6, 7, 8])

print("Even numbers:", even)
print("Odd numbers:", odd)

#13 Building a Student Result Management System
def analyze_results(students): 

    average = sum(students.values()) / len(students)  
    topper = max(students, key=students.get)
 
    count = 0 
 
    for marks in students.values(): 
        if marks > average: 
            count += 1 
 
    return average, topper, count
 
students = { 
    "Aman": 85, 
    "Riya": 95, 
    "Rahul": 72, 
    "Priya": 80 
} 
 
average, topper, count = analyze_results(students) 
 
print("Average:", average) 
print("Topper:", topper)
print("Above Average:", count)
print("Average students:", [name for name, marks in students.items() if marks > average])

#14 Inventory Analyzer
def inventory_analyzer(products):
    total = sum(products.values())

    expensive = max(products, key=products.get)
    cheap = min(products, key=products.get)
    return total, expensive, cheap

inventory = { 
    "Laptop": 50000, 
    "Mouse": 800, 
    "Keyboard": 2000, 
    "Monitor": 15000 
}

total, expensive, cheap = inventory_analyzer(inventory)

print ("Total Inventory Value:", total)
print ("Most Expensive Product:", expensive)
print ("Cheapest Product:", cheap)

#15 Word Frequency Counter
def word_frequency_counter(text):
    words = text.split()
    frequency = {}

    for word in words:
        word = word.lower()
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

text = "I love NLP. It is very easy to learn NLP. Learn and love NLP."
print(word_frequency_counter(text))