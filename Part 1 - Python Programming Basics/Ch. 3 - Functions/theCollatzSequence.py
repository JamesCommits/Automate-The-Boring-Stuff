def collatz(number):
    if number % 2 == 0:
        even = number // 2
        print(even)
        return even
    else:
        odd = 3 * number +1
        print(odd)
        return odd

userNumber = input("What's your Collatz number?")
userNumberCollatz = collatz(userNumber)
if userNumberCollatz > 1:
    
