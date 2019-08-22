# This bulletPointAdder.py script will get the text from a clipboard
# add a star and space to the beginning of each line and then
# paste this new text to the clipboard


#! python 3
import sys, pyperclip

# This will paste our current clipboard into the variable text
text = pyperclip.paste()

# Seperate lines and add stars
lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes in the 'lines' list
    lines[i] = '* ' + lines[i] # add star to each string in 'lines' list

# pyperclip.copy() is expecting a single string value, not a list of string values.
# To make this a single string value, pass lines into the join() method to get
# a single string joined from the list's string.
text = '\n'.join(lines)

pyperclip.copy(text)

