import random

random_number = random.randint(1,100)

count_guesses = 0
#print(random_number)

game_over = "yes"

while game_over == "yes":


    user_guesses = -1

    while user_guesses != random_number:
        count_guesses += 1
        user_guesses = int(input("What is your guesses? "))
        if user_guesses < random_number:
            print("HIGHER")
        elif user_guesses > random_number:
            print("LOWER")
        else:
            print("Congratulations, you guessed it!!!")
            print(f"It took you {count_guesses} guesses.")

    game_over = input("Do you want to play again. (yes or no)? ")
print("Thank you for playing, goodbye.")
