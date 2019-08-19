allGuests = {'Alice' : {'apples' : 5, 'pretzels' : 12}, 
            'Bob' : {'ham sandwiches' : 3, 'apples' : 2}, 
            'Carol' : {'cups' : 3, 'apple pies' : 1}}


# Inside the totalBrought() function, the for loop iterates over the key-value pairs in guests.
# Inside the loop, the string of the guest's name is assigned to k, and the dictionary of the
# picnic items they're bringing is assigned to v.  If the item parameter exists as a key
# in this dictionary, it's value (the quantity) is added to numBrought.  If it does not exist
# as a key, the get() method returns 0 to be added to numBrought.
def totalBrought(guests, items):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(items, 0)
    return numBrought

print('Number of things being brought to the picnic:')
print(' - Apples      {}'.format(str(totalBrought(allGuests, 'apples'))))
print(' - Cups        {}'.format(str(totalBrought(allGuests, 'cups'))))
print(' - Cakes       {}'.format(str(totalBrought(allGuests, 'cakes'))))
print(' - Ham Sandwiches {}'.format(str(totalBrought(allGuests, 'ham sandwiches'))))
print(' - Apple Pies  {}'.format(str(totalBrought(allGuests, 'apple pies'))))

