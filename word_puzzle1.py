# Word puzzle - Milestone submission

secret_word = "mosiah"
secret_word_lower = secret_word.lower()
count_guesses = 0

#
init_hint = ""
for letter in secret_word:
    init_hint += "_ "
print(f"The hint is: {init_hint}")

play_again = "yes"
while play_again == "yes":

    keep_going = True
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
        if count_guesses > 5:
            print(f"You lose, you exceeded the number of guesses {
                  count_guesses}.")
            keep_going = False

    play_again = input("Do you like to play again? (yes/not): ")
    if play_again != "yes":
        print("Thank you for playing")
