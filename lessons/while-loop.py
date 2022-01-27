""" An exaple of a while loop statement."""

counter: int = 0
maximun: int = int(input("Count up to, but not including what?"))
while counter < maximun:
    counter_squared: int = counter ** 2
    print("The square of " + str(counter) + " is " + str(counter_squared))
    counter = counter + 1

print("Done!")