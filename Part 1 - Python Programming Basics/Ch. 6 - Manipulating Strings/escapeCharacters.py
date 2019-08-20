# An escape character lets you use characters that are otherwise impossible to put into a string

# Escape Characters         Prints As
#       \'                  Single quote
#       \"                  Double Quote
#       \t                  tab
#       \n                  Newline (line break)
#       \\                  Backslash

print("Hellow there!\nHow are you?\nI\'m doing fine.")

# You can place an 'r' before the beginning quotation marks of a string to make it a raw string.
# A raw string completely ignores all escape characters and prints any backslash that appears
# in the string.

(print(r'That is Carol\'s cat.'))