# Examples of global and local variables

def spam():
    global eggs
    eggs = 'spam' # this is the global 'eggs'

def bacon():
    eggs = 'bacon' # this is the local to the function bacon()

def ham():
    print(eggs) # this is the global 'eggs'

eggs = 42 # this is the global 'eggs'
spam()
print(eggs)