import random

correct = False

val = random.randint(0, 10)
guesses = 0
while not correct:   
    num = int(input("Guess a number between 0 and 10: "))
    guesses += 1
    if val > num:
        print("Higher")
    elif val < num:
        print("Lower")
    else:
        print("You guessed correct!")
        print(val)
        print(num)
        print(f"Guesses: {guesses}")
        correct = True
