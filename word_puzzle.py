print("Welcome to the word guessing game!\n")

secret_word = "mosiah"
secret_word_lowercase = secret_word.lower()
num_guesses = 0

# Generate initial hint
initial_hint = ""
for letter in secret_word:
    initial_hint += "_ "
print("Your hint is:", initial_hint)

# Start the game loop
while True:
    guess = input("What is your guess? ").lower()
    num_guesses += 1

    # Check if guess has the same number of letters as the secret word
    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.\n")
        continue

    # Check if guess matches the secret word
    if guess == secret_word_lowercase:
        print("Congratulations! You guessed it!")
        print("It took you", num_guesses, "guesses.")
        break

    # Generate and display hint
    hint = ""
    for i in range(len(secret_word)):
        if guess[i] == secret_word_lowercase[i]:
            hint += guess[i].upper()
        elif guess[i] in secret_word_lowercase:
            hint += guess[i].lower()
        else:
            hint += '_'
        hint += " "
    print("Your hint is:", hint)
    print()
