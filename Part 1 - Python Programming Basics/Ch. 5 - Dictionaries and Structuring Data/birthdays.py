birthdays = {'Skeptic' : 'Aug 7', 'grOOpy' : 'April 1', 'choochookazam' : 'December 4'}

while True:
    print('Enter a name:  (enter nothing to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of {}'.format(name))
    else:
        print('I don\'t have the birthday for {}'.format(name))
        print('Do you know their birthday instead?')
        bday = input()
        birthdays[name] = bday
        print('Thanks for adding {} birthday to the list!'.format(name))