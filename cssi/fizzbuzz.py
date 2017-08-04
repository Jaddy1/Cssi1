
# n = int(raw_input("Choose a number"))
def fizzBuzz(n):
    for i in range(0, n + 1):
        if i % 5 == 0 and n % 3 == 0:
            print "FizzBuzz"
        elif i % 3 == 0:
            print "Fizz"
        elif i % 5 == 0 :
            print "Buzz"
        else:
            print i

def fizzBuzzLoop():
    n = int(raw_input("Pick a number: "))
    fizzBuzz(n)
    while True:
        response = raw_input("Quit?")

        if response == "Yes" or response == "yes":
            break
    print "GoodBye"

fizzBuzzLoop()
