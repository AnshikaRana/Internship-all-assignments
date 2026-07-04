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

#16 Library Book Search System
def library_book_search(library, book_name):
    if book_name in library:
        return f"{book_name} is available in the library."
    else:
        return f"{book_name} is not available in the library."
    
book_name = [ 
    "Python", 
    "Java", 
    "C++", 
    "Machine Learning" 
] 
 
print(library_book_search(book_name, "Python"))

#17 Attendace Report Generator
def attendance_report(all_students, present_students):
    absent = set(all_students) - set(present_students)

    percentage = (len(present_students) / len(all_students)) * 100
    return absent, percentage

students = [ 
    "Aman", 
    "Riya", 
    "Rahul", 
    "Priya", 
    "Karan" 
] 
 
present = [ 
    "Aman", 
    "Priya", 
    "Rahul" 
] 
 
absent, percentage = attendance_report(students, present)

print("Present Students:", present)
print("Absent Students:", absent)
print("Attendance Percentage:", percentage)

#17 Shopping Cart Billing System
def shopping_cart_billing(cart):
    bill = sum(cart.values())
    return bill

cart = { 
    "Shoes": 2500, 
    "Bag": 1800, 
    "Watch": 2200 
}

bill = shopping_cart_billing(cart)

if bill > 5000:
    print("You are eligible for a discount of 10%")
    bill = bill * 0.9
    print ("Total Bill after discount:", bill)

else:
    print ("Total Bill:", bill)

#19 Cricket Statistics Analyzer
def cricket_analysis(players, scores):
    average = sum(scores) / len(players)
    highest = max(scores)
    above_average = [player for player, score in zip(players, scores) if score > average]

    return above_average, highest, average

runs = { 
    "Virat": 82, 
    "Gill": 45, 
    "Rohit": 71, 
    "Pant": 38 
}

above_average, highest, average = cricket_analysis(list(runs.keys()), list(runs.values()))
print("Players Scoring Above Average:", above_average)
print("Highest Score:", highest)
print("Average Runs:", average)

#20 Student Database Analyzer (Mini Project)
def student_analysis(records):
    total = 0
    topper = records[0]
    grades = { 
        "A": 0, 
        "B": 0, 
        "C": 0, 
        "D": 0 
    }
    above_80 = []

    for student in records:
        marks = student["marks"]
        total += marks

        if marks > topper["marks"]:
            topper = student

        if marks >= 90:
            grades["A"] += 1
        elif marks >= 75:
            grades["B"] += 1
        elif marks >= 60:
            grades["C"] += 1
        else:
            grades["D"] += 1

        if marks > 80:
            above_80.append(list(student["name"]))
    
    average = total / len(records)
    return average, topper["name"], grades, above_80

students = [
    {"name": "Aman", "marks": 85}, 
    {"name": "Riya", "marks": 95}, 
    {"name": "Rahul", "marks": 68}, 
    {"name": "Priya", "marks": 78}, 
    {"name": "Karan", "marks": 55} 
]

result = student_analysis(students)

print("Topper:", result[1]) 
print("Average Marks:", result[0]) 
print("Grades Distribution:", result[2]) 
print("Above 80:", result[3]) 


#PRACTICE PROBLEMS
'''Employee Performance Analyzer'''
def employee_analysis(employees):
    count = 0
    count2 = 0

    average_score = sum(employees.values())/ len(employees.items())
    highest_scorer = max(employees, key=employees.get)

    for score in employees.values():
        if score > average_score:
            list_of_employees = [name for name, score in employees.items() if score > average_score]
            list_of_employees.append
            count += 1

    count2 = len([name for name, score in employees.items() if score < 60])
    return count, highest_scorer, average_score, list_of_employees, count2

employees = { 
"Aman": 78, 
"Riya": 92, 
"Rahul": 55, 
"Priya": 81, 
"Karan": 48 
}

count, highest_scorer, average_score, list_of_employees, count2 = employee_analysis(employees)

print ("Highest Performing Employee:", highest_scorer)
print ("Average Performance Score:", average_score)
print ("Employees Performing Above Average:", list_of_employees)
print ("Employees Scoring Below 60:", count2)