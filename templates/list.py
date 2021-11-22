# Challenge 1: Name the variable types of the following variables. Print them out into console in the format "Variable: Variable Type" (might have to google "how to print variables in python")
from flask import app

var1 = 3
var2 = "Mr. Mortensen"
var3 = 'f'
var4 = 0.4

print(var1,":" , type(var1))
print(var2,":" , type(var2))
print(var3,":" , type(var3))
print(var4,":" , type(var4))

# Challenge 2: Pass list1 into list2. However, list2 must contain the elements of list1 in order. Print list2. +0.3 if you can create a function to order a list and can display it on your website

list1 = [5, 3, 4, 1, 2]
def orderList (list):
    list1.sort()
    print(list1)

list2 = [list1[3], list1[4], list1[1], list1[2], list1[0]]
print(list2)

# Challenge 3: Find a way to add 3 to each element in the array. Then, take the average of the array and put it into the variable avg. +0.2 if you can turn this into a function and display it on your website.

averageList = [23, 41, 90, 55, 71, 83]
# Python program to get average of a list
# Using reduce() and lambda

# importing reduce()
from functools import reduce

def Average(lst):
    return sum(lst) / len(lst)

# Driver Code
lst = [23, 41, 90, 55, 71, 83]
average = Average(lst)

# Printing average of the list
print("Average of the list =", round(average, 2))

# TT7
student_list = ['pam','rob','joe','greg','bob','amy','matt']
# Activity 1
print(student_list[2:5])
print(student_list[:-5])
print(student_list[5:])
print(student_list)
if 'rob' in student_list:
    print("Rob is in student_list")
else:
    print("Rob is not in student_list")

# Activity 2
p1 = { "name":"John", "age":61, "city":"Eugene"}
p2 = { "name":"Risa", "age":16, "city":"New York"}
p3 = { "name":"Ryan", "age":16, "city":"Los Angeles"}
p4 = { "name":"Shekar", "age":16, "city":"San Francisco"}
# a list of dictionaries
list_of_people = [p1, p2, p3, p4]


# turn list to dictionary of people
dict_people = {'people': list_of_people}
print("List to Dictionary of people")
print(type(dict_people))
print(dict_people)
# write some code to Print People from Dictionary
# turn dictionary to JSON
print("** Dumps - Python to JSON String**")
json_people = json.dumps(list_of_people)
print("JSON People #1")
print(type(json_people))
print(json_people)
# write some code to pretty print the JSON dict


# write some code to unwind JSON using json.loads and print the people
print("** Loads - JSON to Python Dict**")
#json_dict = json.loads(json_people)
print(json_dict)
# to list
names = [person['name'] for person in json_dict]
print("Names of people to list: " + str(names))
print("Names of people: ")
# pretty print Names of People

if __name__ == "__main__":
    app.run(debug=True)

    student_list = ['pam','rob','joe','greg','bob','amy','matt']
    print(student_list[2:5])
