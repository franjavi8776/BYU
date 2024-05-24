import random

keep_going = "yes"
while keep_going == "yes":

    random_number = random.randint(1,10)

    user_guess = -1
    count_guesses = 0

    while user_guess != random_number:

        # magic_number = int(input("What is your magic number? "))
        count_guesses += 1
        user_guess = int(input("What is your guess? "))

        if random_number == user_guess:
            print(f"Congratulations!. It took you {count_guesses} guesses")
        elif random_number > user_guess:
            print("HIGHER")
        elif random_number < user_guess:
            print("LOWER")

    keep_going = input("Do you wanna play again? (yes/no) ").lower()
print("Thanks for playing.")
