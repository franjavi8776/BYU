#The program contains a hidden secret word stored in a variable. This word can have any number of letters in it. When the program runs, the user is shown underscores ( _ ) for each letter of the word.

#The user then enters a guess. If the guess is correct, the user wins and the game is over.

#If the guess is not correct, the user will be given a hint to help them improve their guess for the next round.

#The game continues prompting the user for new guesses and showing them hints until they guess the word correctly. When the game is over, the program displays the number of guesses that were made.

#The guess must be the same number of letters as the secret word. If the guess has a different numbers of letters, the user is given a message explaining this, and no hint is provided.

#The hint shows the letters of the guess, but each letter is rendered in a special way as follows:

#An underscore _ indicates that the letter was not present in the secret word.

#A lowercase letter indicates that the letter was present somewhere in the secret word, but not at that position.

#An uppercase letter indicates that the letter was present at that exact spot in the secret word. (In other words, if the second letter in the guess is also the second letter in the secret word, then that letter is shown as a capital.)

#For example, if the secret word were: mosiah, then the program would initially display:

secret_word = "mosiah"
secret_word_lower = secret_word.lower()
count_guesses = 0


init_hint = ""
for letter in secret_word:
    init_hint += "_ "
print(f"The hint is: {init_hint}")

game_over = True
while game_over:
    guess = input("What is your guess?").lower()
    count_guesses += 1

    if len(guess) != len(secret_word):
        print("The guess must have the same number of letters as the secret word.")
    else:
        if guess == secret_word_lower:
            print("Congratulations!!!, you guessed it!!!")
            print(f"It took you {count_guesses} guesses.")
            game_over = False
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
