def printPicnic (itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for key, value in itemsDict.items():
        print(key.ljust(leftWidth, '.') + str(value).rjust(rightWidth))

picnicItems = {'sandwiches' : 4, 'apples' : 12, 'cups' : 4, 'cookies' : 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

# In this program we define a printPicnic() function that will take in a dictionary of
# information and use center(), ljust() and rjust() to display that information in a 
# neatly aligned table like format.  

# The dictionary that we'll pass printPicnic() is picnicItems. We want to organize this
# information into two columns, with the name on the left and the quantity on the right.

# printPicnic() takes in a dictionary, a leftWidth for the left column of a table,
# and a rightWidth() for the right column.  It prints a title, PICNIC ITEMS, centered
# above the table.  Then, it loops through the dictionary, printing each key-value
# pair on a line with the key justified left and padded by peiods, and the value
# justified right and padded by spaces.

# After defining printPicnic(), we define the dictionary picnicItems{} and call
# printPicnic() twice, passing it different widths for the left and right
# table columns.