# List []

student_grades = [9.1, 8.8, 7.5]

temperatures = [5.4, 8, "something"]

#list containing another list (object inside object)
rainfall = [1.2, 9, "text", [2, 8.5]]

mysum = sum(student_grades)
length = len(student_grades)
mean = mysum / length
print(mean)

#############################################
#Exemples of builtins
#using dir(list)
# fint the bigest grade (max())
max_student_grades = max(student_grades)
print(max_student_grades)

#using dir(__builtins__)
#count how many 10.0 are in the list (.count())
student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]

count_2 = student_grades.count(10.0)
print(count_2)

#using dir(str)
# to lowercase ()
username = "Python3"
username = "Python3".lower()
print(username)

###############################################
#Dictionaty Types
#dictionary syntax
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

mysum = sum(student_grades.values())
length = len(student_grades)
mean = mysum / length
print(mean)
print(student_grades.keys())


day_temperatures = {"morning": 5.5, "noon": 12.8, "evening": 10.2}

#################################################
#Tuple Types (), []
#immutible ()
monday_temperatures = (1, 4, 5)
print(monday_temperatures)

#mutible (you can add more items to the list) []
monday_temperatures2 = [1, 4, 5]
monday_temperatures2.append(6)
print(monday_temperatures2)

monday_temperatures2.remove(4)
print(monday_temperatures2)

# a variable with a tuple assigned. inside the main tuple, another 3 tuples are asigned
color_codes = ((1, 5, 9), (4, 7, 2), (5, 9, 6))

# a dicionary with 3 keys that contains a tuple with 3 foats
day_temperatures = {"morning": (1.3, 4.8, 6.1), "noon": (10.5, 12.8, 15.3), "evening": (14.5, 13.8, 9.4)}

################################################
# Python Cheatsheet (Data Types)

# In this section, you learned that:
# Integers are for representing whole numbers:
# rank = 10
# eggs = 12
# people = 3


# Floats represent continuous values:
# temperature = 10.2
# rainfall = 5.98
# elevation = 1031.88


# Strings represent any text:
# message = "Welcome to our online shop!"
# name = "John"
# serial = "R001991981SW"

# Lists represent arrays of values that may change during the course of the program:
# members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
# pixel_values = [252, 251, 251, 253, 250, 248, 247]


# Dictionaries represent pairs of keys and values:
# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons":"+423998200919"}
# volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}

# Keys of a dictionary can be extracted with:
# phone_numbers.keys()

# Values of a dictionary can be extracted with:
# phone_numbers.values()


# Tuples represent arrays of values that are not to be changed during the course of the program:
# vowels = ('a', 'e', 'i', 'o', 'u')
# one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


# To find out what attributes a type has:
# dir(str)
# dir(list)
# dir(dict)


# To find out what Python builtin functions there are:
# dir(__builtins__)


# Documentation for a Python command can be found with:
# help(str)
# help(str.replace)
# help(dict.values)
