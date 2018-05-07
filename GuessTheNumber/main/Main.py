from random import randint

ans = randint(1, 10)
loop = True

while loop:
    for i in range(3):

        guess = int(raw_input("Pick a number between 1 and 10."))

        if guess == ans:
            print "You win!"
            break

        if guess > ans:
            print "Too high."

        if guess < ans:
            print "Too low."

        if i == 2:
            print "Sorry, you lose. The answer was " + str(ans)

    loop = bool(raw_input("True, to go again. False to stop"))
