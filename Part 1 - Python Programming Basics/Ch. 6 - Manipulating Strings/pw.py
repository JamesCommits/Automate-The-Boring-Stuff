#! python3
# An insecure password locker project.

PASSWORDS = {'email' : 'F3fdf9r1fg39d', 'blog' : '4tgf233rgsg354FS', 'luggage' : '12345'}


import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

# sys.argv is a LIST[] that contains the arguments a user passes through the command line.
account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for {} has been copied to the clipboard!'.format(account))
else:
    print('There is no account named {}'.format(account))