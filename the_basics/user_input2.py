def greet(name):
  #return "Hi %s " % user_input.title()
  return f"Hi {user_input.title()}"
#.title() make the first letter uppercase

user_input = input("What is your name?")
print(greet(user_input))


