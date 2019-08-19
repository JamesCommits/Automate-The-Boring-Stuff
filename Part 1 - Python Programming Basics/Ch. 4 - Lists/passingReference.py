

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

# Notice that when eggs() is called, a return value is not used to assign a new value to spam
# Instead, it modifies the list in place, directly.