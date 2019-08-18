# 'global eggs' is referencing the global variable eggs and is 
# not creating a new local variable of eggs.

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)