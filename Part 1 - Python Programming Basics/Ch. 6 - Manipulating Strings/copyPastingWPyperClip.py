# The Pyperclip module has copy() paste() functions that can send text to 
# and receive text from your computer's clipboard.  Sending the output
# of your program to the clipboard will make it easy to paste
# outside of the terminal.

# pyperclip is a 3rd party module that is not standard with Python.

import pyperclip

pyperclip.copy('Hello World!')
pyperclip.paste()

# If you copy something outside of Python the past() method will
# still paste it into Python.