import random
# Word puzzle - Milestone submission


play_again = "yes"
while play_again == "yes":

    keep_going = True
    count_guesses = 0
    guesses = 0

    secret_word_arr = ["Mosiah", "Moroni", "Alma", "Nephi", "Eter"]
    secret_word = random.choice(secret_word_arr)
    secret_word_lower = secret_word.lower()

    init_hint = ""
    for letter in secret_word:
        init_hint += "_ "
    print(f"The hint is: {init_hint}")

    invalid_level = True
    while invalid_level:
        game_level = input(
            "What level do you want to play: (easy/medium/hard)? ").lower()

        if game_level == "easy":
            guesses = 10
            print("You had chosen an easy level, you have 10 guesses.")
            invalid_level = False
        elif game_level == "medium":
            guesses = 8
            print("You had chosen a medium level, you have 8 guesses.")
            invalid_level = False
        elif game_level == "hard":
            guesses = 5
            print("You had chosen a hard level, you have 5 guesses.")
            invalid_level = False
        else:
            print("Invalid choice. Please choose a valid game level.")

    while keep_going:
        guess = input("What is your guess? ").lower()
        count_guesses += 1

        if len(guess) != len(secret_word):
            print("The guess must have the same number of letters as the secret word.")
        else:
            if guess == secret_word_lower:
                print("Congratulations!!!, you guessed it!!!")
                print(f"It took you {count_guesses} guesses.")
                keep_going = False
            else:
                hint = ""
                for i in range(len(secret_word)):
                    if guess[i] == secret_word_lower[i]:
                        hint += guess[i].upper()
                    elif guess[i] in secret_word_lower:
                        hint += guess[i].lower()
                    else:
                        hint += "_"
                print(f"Your hint is: {hint}")
        if count_guesses > guesses:
            print(f"You lose, you exceeded the {guesses} guesses.")
            keep_going = False

    play_again = input("Do you like to play again? (yes/not): ")
    if play_again != "yes":
        print("Thank you for playing")
