monday_temperatures = [9.1, 8.8, 7.6]

for tempature in monday_temperatures:
  print(round(tempature))

for letter in "hello":
  print(letter)
  print("done")


numbers = [11, 34, 98, 43, 45, 54, 54]
for number in numbers:
    if number > 50:
        print (number)

print("Finish")

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for color in colors:
  if color == int(color):
    print (color)

print("Finish")

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for color in colors:
  if color == int(color) and color > 50:
    print (color)

print("Finish")

############################# convert cm -> in 
def converter(cm):
  return cm * 0.393701

dimensions = [1, 200, 10, 1.5]

for dimension in dimensions:
  print (converter(dimension))

print("Finish")

#############################

def converter(cm):
  return cm * 0.393701

dimensions = [1, 200, 10, 1.5]

for dimension in dimensions:
  print (f"{dimension} cm is equal to: {converter(dimension)} in")

print("Finish")


###############################
#Loop over a dictionary

student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

for grade in student_grades.items():
  print (grade)
#this will print tuples ('Marry', 9.1) ('Sim', 8.8) ('John', 7.5)

print("Finish")

for grade in student_grades.keys():
  print (grade)

for grade in student_grades.values():
  print (grade)

print("Finish")

###
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for contact in phone_numbers.items():
    #print("%s: %s" % (contact[0], contact[1]) )
    print(f"{contact[0]}: {contact[1]}")
#this will output:
#John Smith: +37682929928
#Marry Simpons: +423998200919

################################
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for number in phone_numbers.values():
  formated_numbers = number[1:]
  print(f"00{formated_numbers}")
#this will print
#0037682929928
#00423998200919
