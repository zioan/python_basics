monday_temperatures = [9.1, 8.8, 7.5]
monday_temperatures.append(5.7)
print(monday_temperatures)

#find the index of an item
monday_temperatures = [9.1, 8.8, 7.5]
monday_temperatures.index(8.8)

#find the value asigned to the index
monday_temperatures = [9.1, 8.8, 7.5]
monday_temperatures.__getitem__(1)
print(monday_temperatures.__getitem__(1))
    #OR
monday_temperatures[1]
print(monday_temperatures[1])

# append the first item of the weekend to workdays
workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])
print(workdays)

#pop(index) - remove the item with the specified index
seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
seconds.pop(1)
print(seconds)

#remove last 3 items ....
seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
seconds.pop(1)
seconds.pop(1)
seconds.pop(1)
print (seconds)


#find the length
monday_temperatures = [9.7, 8.8, 7.5, 6.6, 9.9]
find_len = len(monday_temperatures)
print(find_len)

#access portion of a list based on index (upper limit is never included, so it will output the values from index 1 to 3 )
portion = monday_temperatures[1:4]
print(portion)

#extract the values from 0 to 2 (first 2 values because the last (2) is excluded)
#portion = monday_temperatures[0:2]
portion = monday_temperatures[:2]
#extract the last 2 values
#portion = monday_temperatures[3:5] (5 so it will include the last one, 4)
portion = monday_temperatures[3:]
print(portion)

#get the last index
monday_temperatures[-1]
#get the last index
monday_temperatures[-1]
#get the last but one (penultimul)
monday_temperatures[-2] #and so on... -3...
#get the last 2 items
monday_temperatures[-2:]

#Strings
mystring = "hello"
mystring[1] #e
mystring[-1] #o
mystring[:3] #hel

exemple = ["hello", 1, 2, 3]
exemple[0] #hello
exemple[0] [2] #l

##print out the slice ["b", "c", "d"] of the letter list
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:4])


#Items in dictionaries
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
student_grades["sim"] #8.8

eng_port = {"rain": "chuva", "sun": "sol"}
eng_port["sun"] #"sol"

#
#Converting Between Datatypes
#Sometimes you might need to convert between different data types in Python for one reason or another. That is very easy to do:

#From tuple to list:
data = (1, 2, 3)
list(data)
[1, 2, 3]

#From list to tuple:
data = [1, 2, 3]
tuple(data)
(1, 2, 3)

#From list to dictionary:
data = [["name", "John"], ["surname", "smith"]]
dict(data)
{'name': 'John', 'surname': 'smith'}

#Note that the original data type needs to have the data structured in a way that can be understood by the new data type. For example, the following would not work:
data = [1, 2, 3]
dict(data)
#TypeError: cannot convert dictionary update sequence element #0 to a sequence
#That's because a dictionary is made of key and value pairs, but the list was not constructed that way, so the above would generate an error.