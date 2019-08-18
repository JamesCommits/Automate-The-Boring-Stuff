# a ZeroDivisionError happens whenever you try to divide a number by zero.
# Errors can be handled with try and except statements.

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid Argument')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))