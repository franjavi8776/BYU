print("Welcome to the word guessing game!\n")

secret_word = "mosiah"
secret_word_lower = secret_word.lower()
count_guesses = 0

# Generate initial hint
initial_hint = ""
for letter in secret_word:
    initial_hint += "_ "
print("Your hint is:", initial_hint)

# Start the game loop
while True:
    guess = input("What is your guess? ").lower()
    count_guesses += 1

    # Check if guess has the same number of letters as the secret word
    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.\n")
        continue

    # Check if guess matches the secret word
    if guess == secret_word_lower:
        print("Congratulations! You guessed it!")
        print(f"It took you {count_guesses} guesses.")
        break

    # Generate and display hint
    hint = ""
    for i in range(len(secret_word)):
        if guess[i] == secret_word_lower[i]:
            hint += guess[i].upper()
        elif guess[i] in secret_word_lower:
            hint += guess[i].lower()
        else:
            hint += '_'
    print(f"Your hint is: {hint}")
