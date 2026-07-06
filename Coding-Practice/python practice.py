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

'''Online Store Sales Report'''
def sales_report(products):
    total_sales = sum(products.values())
    best_selling_product= max(products, key=products.get)
    least_selling_product = min(products, key=products.get)

    list_of_products = [name for name, sales in products.items() if sales > 100]
    return total_sales, best_selling_product, least_selling_product, list_of_products

products = { 
"Laptop": 120, 
"Mouse": 85, 
"Keyboard": 60, 
"Monitor": 150, 
"Headphones": 95 
}

total_sales, best_selling_product, least_selling_product, list_of_products = sales_report(products)

print("Total Sales:", total_sales)
print("Best Selling Product:", best_selling_product)
print("Least Selling Product:", least_selling_product)
print("Products with Sales Above 100:", list_of_products)

'''Student Attendance Management System'''
def attendance_summary(all_students, present_students):
    absent_students = set(all_students) - set(present_students)
    attendance_percentage = (len(present_students) / len(all_students)) * 100

    a_letter_students = [name for name in all_students if name.startswith("A")]
    if attendance_percentage > 75:
        check = True
    else:
        check = False

    return absent_students, attendance_percentage, a_letter_students, check

all_students = ["Aman", "Riya", "Rahul", "Ankit", "Priya", "Karan"] 
present_students = ["Aman", "Rahul", "Ankit", "Priya"]

absent_students, attendance_percentage, a_letter_students, check = attendance_summary(all_students, present_students)

print("Absent Students:", absent_students)
print("Attendance Percentage:", attendance_percentage)
print("Students with Names Starting with 'A':", a_letter_students)
print("Is the Attendance above 75%:", check)

'''Library Analytics System'''
def library_reports(books):
    count = len(books)
    unique_books = len(set(books))
    repeated_books = [book for book in set(books) if books.count(book) > 1]
    arranged_books = sorted(books)

    return count, unique_books, repeated_books, arranged_books

books = [ 
"Python", 
"Java", 
"Python", 
"C++", 
"Java", 
"Machine Learning" 
]

count, unique_books, repeated_books, arranged_books = library_reports(books)

print("Total Number of Books:", count)
print("Number of Unique Books:", unique_books)
print("Repeated Books:", repeated_books)
print("Books Arranged in Alphabetical Order:", arranged_books)

'''University Result Processing System (Mini Project)'''
def result_analysis(students):
    topper = max(students, key=lambda student: student["marks"]) ["name"]
    average_marks = sum(student["marks"] for student in students) / len(students)
    passed_students = [student for student in students if student["marks"] >= 40]

    grade_distribution = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0
    }

    for student in students:
        marks = student["marks"]
        if marks >= 90:
            grade_distribution["A"] += 1
        elif 75 <= marks <= 89:
            grade_distribution["B"] += 1
        elif 60 <= marks <= 74:
            grade_distribution["C"] += 1
        else:
            grade_distribution["D"] += 1

    above_average_students = [student["name"] for student in students if student["marks"] > average_marks]
    percentage_passed_students = (len(passed_students) / len(students)) * 100

    return topper, average_marks, passed_students, above_average_students, percentage_passed_students, grade_distribution

students = [ 
{"name": "Aman", "marks": 85}, 
{"name": "Riya", "marks": 95}, 
{"name": "Rahul", "marks": 38}, 
{"name": "Priya", "marks": 72}, 
{"name": "Karan", "marks": 58}]

topper, average_marks, passed_students, above_average_students, percentage_passed_students, grade_distribution = result_analysis(students)

print("Topper:", topper)
print("Average Marks:", average_marks)
print("Students scoring above average:", above_average_students)
print("Percentage of Students Passed:", percentage_passed_students, "%")

'''Tournament Ranking System'''

def add_match_result(matches, team1, team2, score1, score2):
    """Store a single match result."""
    matches.append({
        "team1": team1,
        "team2": team2,
        "score1": score1,
        "score2": score2
    })


def initialize_table(matches):
    """Create an empty stats entry for every team found in matches."""
    table = {}
    for match in matches:
        for team in (match["team1"], match["team2"]):
            if team not in table:
                table[team] = {
                    "played": 0,
                    "won": 0,
                    "drawn": 0,
                    "lost": 0,
                    "goals_for": 0,
                    "goals_against": 0,
                    "points": 0
                }
    return table


def update_table(table, matches):
    """Fill in stats based on match results."""
    for match in matches:
        t1, t2 = match["team1"], match["team2"]
        s1, s2 = match["score1"], match["score2"]

        table[t1]["played"] += 1
        table[t2]["played"] += 1
        table[t1]["goals_for"] += s1
        table[t1]["goals_against"] += s2
        table[t2]["goals_for"] += s2
        table[t2]["goals_against"] += s1

        if s1 > s2:
            table[t1]["won"] += 1
            table[t1]["points"] += 3
            table[t2]["lost"] += 1
        elif s2 > s1:
            table[t2]["won"] += 1
            table[t2]["points"] += 3
            table[t1]["lost"] += 1
        else:
            table[t1]["drawn"] += 1
            table[t2]["drawn"] += 1
            table[t1]["points"] += 1
            table[t2]["points"] += 1

    return table


def calculate_goal_difference(table):
    """Add goal difference to each team's stats."""
    for team in table:
        table[team]["goal_diff"] = table[team]["goals_for"] - table[team]["goals_against"]
    return table


def get_sorted_rankings(table):
    """Sort teams by points, then goal difference, then goals scored."""
    teams = list(table.items())
    teams.sort(
        key=lambda x: (x[1]["points"], x[1]["goal_diff"], x[1]["goals_for"]),
        reverse=True
    )
    return teams


def display_rankings(rankings):
    """Print a formatted points table."""
    print(f"{'Rank':<5}{'Team':<12}{'P':<4}{'W':<4}{'D':<4}{'L':<4}{'GF':<4}{'GA':<4}{'GD':<4}{'Pts':<4}")
    for i, (team, stats) in enumerate(rankings, start=1):
        print(f"{i:<5}{team:<12}{stats['played']:<4}{stats['won']:<4}"
              f"{stats['drawn']:<4}{stats['lost']:<4}{stats['goals_for']:<4}"
              f"{stats['goals_against']:<4}{stats['goal_diff']:<4}{stats['points']:<4}")


def get_winner_and_runner_up(rankings):
    """Return the top two teams."""
    winner = rankings[0][0] if len(rankings) > 0 else None
    runner_up = rankings[1][0] if len(rankings) > 1 else None
    return winner, runner_up

def main():
    matches = []

    add_match_result(matches, "India", "Australia", 3, 1)
    add_match_result(matches, "England", "Pakistan", 2, 2)
    add_match_result(matches, "India", "England", 1, 0)
    add_match_result(matches, "Australia", "Pakistan", 2, 3)
    add_match_result(matches, "India", "Pakistan", 4, 0)
    add_match_result(matches, "Australia", "England", 1, 1)

    table = initialize_table(matches)
    table = update_table(table, matches)
    table = calculate_goal_difference(table)

    rankings = get_sorted_rankings(table)

    print("Tournament Points Table:\n")
    display_rankings(rankings)

    winner, runner_up = get_winner_and_runner_up(rankings)
    print(f"Winner: {winner}")
    print(f"Runner-up: {runner_up}")

if __name__ == "__main__":
    main()