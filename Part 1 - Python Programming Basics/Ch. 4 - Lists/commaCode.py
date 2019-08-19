spam = ['apples', 'bananas', 'tofu', 'cats']

def commaCode(someParameter):
    if len(words) == 1:
        return words[0]
    return '{}, and {}'.format(', '.join(words[:-1]), words[-1])

    # Now lets break this down
    # words[-1] takes the last element of a list.  words[:-1] slices the list to produce a new list
    # with all words EXCEPT the last one.

    # ', '.join() produces a new string, with all strings of the argument to str.join()
    # joined with ', '.  If there is just one element in the input list, that one
    # element is returned, unjoined.

    #'{}, and {}'.format{} inserts the comma-joined words and the last word into a template (complete with Oxford comma)
    
