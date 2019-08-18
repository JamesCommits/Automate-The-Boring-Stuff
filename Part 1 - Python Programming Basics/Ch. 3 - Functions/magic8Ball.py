# Defines a function that returns a different string depending on what
# number it is passed as an argument.
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain.'
    elif answerNumber == 2:
        return 'It is decidedly so.'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy...try again later'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtfful'

# r = random.randint(1, 9)
# fortune = getAnswer(r)
# print(fortune)
# We can reduce the above code down to a single line
print(getAnswer(random.randint(1, 9)))