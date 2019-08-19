# You may not want your original list or dictionary values changed.  For this, Python provides a module named
# copy that provides both the copy() and deepcopy() function.  
import copy
spam = ['A', 'B', 'C', 'D']
# Now utilizing the copy.copy() function here, the spam and cheese variables are referencing two seperate lists.
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)

# If the list you need to copy contains lists, then use the copy.deepcopy() function instead of copy.copy().
# The copy.deepcopy() function will copy these inner lists as well