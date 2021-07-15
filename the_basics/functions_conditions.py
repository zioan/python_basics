#FUNCTIONS
#create your own function (average calculator)
def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(mean([1, 4, 5]))


#list length calculator
def calculate_length(lst):
    return len(lst)

print (calculate_length([1, 2, 3, 4, 5]))


#calculate the area of a square (3 => 9, 7 => 49)
def square(val):
    return val * val

print(square(7))


#volume converter from ounces to mililiters
def vol_converter(val):
    return val * 29.57353

print(vol_converter(5))


#CONDITIONS

#if
def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean

student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

print(mean(student_grades))


#"and" / "or"
x = 1
y = 1
 
if x == 1 and y==1:
    print("Yes")
else:
    print("No")
#That will return Yes since x == 1 and y ==1 are both True.


x = 1
y = 1
 
if x == 1 or y==2:
    print("Yes")
else:
    print("No")
#That will return Yes since at least one of the conditions is True. In this case x == 1 is True.

##password controller exemple
def pass_check(x):
    if len(x) < 8:
        return False
    else:
        return True

print(pass_check("pass")) #False
print(pass_check("mylongpassword")) #True

#temperature controller
def temp_check(x):
    if x <= 7:
      return "Cold"
    else:
      return "Warm"

print(temp_check(7))

## else if

x=3
y=7
if x > y:
  print("x is greater than y")
elif x == y:
  print("x is equal to y")
else:
  print("x is less than y")



def temp_check2(x):
  if x < 15:
    return "Cold"
  elif x >= 15 and x <= 25:
    return "Warm"
  else:
    return "Hot"

print(temp_check2(26))