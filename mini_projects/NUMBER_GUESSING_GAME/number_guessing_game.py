#number guessing game
import random
answer=random.randint(1,100)
print("----python number guessing game----")

while True:
    guess=input("select a number between 1 and 100:")
    if not guess.isdigit():
        print("enter a valid number")
        continue

    guesses=int(guess)
    if guesses<1 or guesses>100:
        print("enter a number between 1 and 100")

    elif guesses<answer:
        print("number too low.TRY AGAIN!!")

    elif guesses > answer:
        print("number too high.TRY AGAIN!!")

    else:
        print(f"the number guessed was:{guesses}")
        print(f"CONGRATULATIONS!! the answer was:{answer}")