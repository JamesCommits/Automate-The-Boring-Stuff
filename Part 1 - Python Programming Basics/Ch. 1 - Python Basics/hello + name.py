# This program says hello and asks for my name.

print("Hello world!")
print("What is your name?   ") # Asks for their name here
myName = input()
print("Nice to meet you, {}".format(myName))
myNameLength = len(myName)
print("{}, you have {} letters in your name".format(myName, myNameLength))
myAge = input("What's your age?     ")
print("You will be " + str(int(myAge) + 1) + " in a year.")
