import random

def number_guessing():

    print("Welcome to the Number Guessing Game !")
    print("I'm thinking of a number between 1 to 100")
    print("You got the 7 chances to guess the number. Let's start the game")

    num_guess = random.randint(1,100)

    chance = 7

    guess_counter = 0

    while guess_counter < chance:
        
        guess_counter += 1
        your_guess = int(input("Enter Your Guess => "))

        if (your_guess == num_guess):
            print("Congratulations! the number is ",num_guess,"and you found it right !! in the ",guess_counter,"attempt !")
            break

        elif (guess_counter >= chance and your_guess != num_guess):
            print("Sorry ! the number is ",num_guess,"Better Luck Next Time !")

        elif (your_guess > num_guess):
            print("Try Again !! You Guessed Too High")

        elif (your_guess < num_guess):
            print("Try Again !! You Guessed Too Small")

        else:
            print("Invaild chioce")

number_guessing()
