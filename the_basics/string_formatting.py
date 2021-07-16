#user_input = input("Enter your name:")
##this works in python 2 and 3
#message = "Hello %s!" % user_input
##this works from python 3.6
#message = f"Hello {user_input}"
#print(message)


name = input("Enter your name:")
surname = input("Enter your surname:")
when = "today"
#this works in python 2 and 3
#message = "Hello %s %s!" % (name, surname)
#this works from python 3.6
message = f"Hello {name} {surname}. What's up {when}"
print(message)


def greet(name):
    return "Hi %s" % name

def greet(name):
    return "Hi %s" % name.title()