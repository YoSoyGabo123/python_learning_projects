import random
print("Choose a number beween 10 and 20")
secretNumber = random.randint(10,21)
for guesses in range(10):
    print("You choose")
    guess = int(input())
    if guess == secretNumber:
        print("Success")
        break
    elif guess < secretNumber:
        print("Too low")
        continue
    else:
        print("Too high")
        continue

print("It took you " + str(guesses+1) + " guesses")