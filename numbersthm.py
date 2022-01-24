import random
print("Number Guessing game")
number = random.randint(1, 9)
chances = 0
print("Guess a number between 1 and 9: ")
while chances < 5:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("Congrats, You Win!")
        break
    elif guess < number:
        print("Your guess was too low. Guess a number higher than")
        print(guess)
    else:
        print("Your guess was too high. Guess a number lower than")
        print(guess)
    chances += 1
    if not chances < 5:
        print("You lose. The number was")
        print(number)
