secret_word = "mosiah"
count_guesses = 0


underscore = ""
for letter in secret_word:
    underscore += "_ "

print(f"The hint is {underscore}")

game_over = True

while game_over:
    user_guesses = input("What is your guesses? ")
    count_guesses += 1

    if len(user_guesses) != len(secret_word):
        print("The user guess must have the same number of letters as the secret word.")
    else:
        if user_guesses == secret_word:
            print("Congratulations, you guessed it!")
            print(f"it took you {count_guesses} guesses")
            game_over = False
        else:
            hint = ""
            for i in range(len(secret_word)):
                if user_guesses[i] == secret_word[i]:
                    hint += user_guesses[i].upper()
                elif user_guesses[i] in secret_word:
                    hint += user_guesses[i].lower()
                else:
                    hint += "_"
            print(hint)
