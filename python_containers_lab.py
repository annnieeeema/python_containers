# Exercise 1
# Create a list named students containing some student names (strings). Print out the second student's name and print out the last student's name.
"""
students = ['Ryan', 'Annie', 'Jun', 'Jacky', 'Jerry']

second_student = students[1]
print(second_student)

last_student = students[-1]
print(last_student)
"""

# Exercise 2
# Create a tuple named foods containing the same # of foods (strings) as there are names in the students list. Use a for loop to print out the string "(food goes here) is a good food".
"""
foods = ('strawberries', 'porkbelly', 'dumplings', 'rice', 'cereal')
for a in foods:
    print(f'{a} is a good food')
"""

# Exercise 3
# Using a for loop, print out the last two food strings from foods. 
"""
foods = ('strawberries', 'porkbelly', 'dumplings', 'rice', 'cereal')
print(foods[3:])
"""

# Exercise 4
# Create a dictionary named home_town containing the keys of city, state, and population. Print a string with the format: "I was born in (city), (state) - population of (population)"
"""
home_town = {
    'city': 'Houston',
    'state': 'Texas',
    'population': 1000
}
print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")
"""

# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item
"""
home_town = {
    'city': 'Houston',
    'state': 'Texas',
    'population': 1000
}
for key, val in home_town.items():
    print(f"{key} = {val}")
"""

# Exercise 6
# Create an empty list named cohort. Using a for loop, add one dictionary to the cohort list for each student name. Iterate over cohort printing out each element. 
"""
cohort = []

cohort.extend([{ 'student': 'Ryan', 'fav_food': 'strawberries'}, { 'student': 'Annie', 'fav_food': 'porkbelly'}, { 'student': 'Jun', 'fav_food': 'dumplings'}, { 'student': 'Jacky', 'fav_food': 'rice'}, { 'student': 'Jerry', 'fav_food': 'cereal'}])

for each_student in cohort:
    print(each_student)
"""

# Exercise 7 
# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this: ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]. Iterate over awesome_students printing out each string. 
"""
students = ['Ryan', 'Annie', 'Jun', 'Jacky', 'Jerry']

awesome_students = [(f"{student} is awesome!") for student in students]

for awesomesauce in awesome_students:
    print(awesomesauce)
"""

# Exercise 8 
# Using the tuple foods and list comprehension within a for loop, print each food string that contains the letter a. 
"""
foods = ('strawberries', 'porkbelly', 'dumplings', 'rice', 'cereal')

for food in foods:
    if 'a' in food:
        print(food)
"""
