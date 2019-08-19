# This is a much better coding of allMyCats1.py

catNames = []
while True:
    print('Enter the name of your cat: ' + str(len(catNames) + 1) + ' (or enter nothing to stop.):')
    name = input()
    if name == '':
        break
   
    catNames = catNames + [name] # Here we add the catName to the list
    
    print('The cat names are:')
    for name in catNames:
        print('  ' + name)