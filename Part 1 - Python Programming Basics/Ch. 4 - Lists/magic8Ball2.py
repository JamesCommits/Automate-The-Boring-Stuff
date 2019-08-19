# a more elegant version of the previous chapters Magic 8 Ball program

import random

# Exceptions to indentations rules apply to lists in Python
messages = ['It is certain,' 
            'It is decidedly so', 
            'Reply hazy...try again later', 
            'Ask again later', 
            'Concentrate and ask again', 
            'My reply is no', 
            'Outlook not so good', 
            'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])