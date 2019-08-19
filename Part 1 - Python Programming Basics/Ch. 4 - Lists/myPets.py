myPets = ['Zophie', 'Lela', 'Nola']
print('Enter a pet name: ')
name = input()
if name not in myPets:
    print('Hmmmm, {} is not my pet'.format(name))
else:
    print('I love all my pets including {}'.format(name))