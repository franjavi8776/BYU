# This Python script prompts the user to input various words to create a customized story. 
# It then constructs a story using the input words and prints it out.
print('Please enter the following: ');
print();

# Asking for words from the user.

# Capitalizing the exclamation word.
exclamation = input('Enter a exclamation: ').capitalize();

# Lowerizing the next words.
adjective1 = input('Enter an adjective: ').lower();
animal = input('Enter an animal: ').lower();
verb1 = input('Enter a verb: ').lower();
verb2 = input('Enter a verb: ').lower();
verb3 = input('Enter a verb: ').lower();
noun1 = input("Enter a noun: ").lower()
adjective2 = input("Enter an adjective: ").lower()
noun2 = input("Enter a noun: ").lower()
place = input("Enter a place: ").lower()
verb4 = input("Enter a verb: ").lower()



# Determine if "a" or "an" should precede the adjective
article_adjective = "an" if adjective1[0] in 'aeiou' else "a";


print();

print('Your story is: ');

print();

# Story with added word prompts.
print(f'The other day, I was really in trouble. It all started when I saw a very\n{adjective1} {animal} {verb1} down the hallway. "{exclamation}!" I yelled. But all\nI could think to do was to {verb2} over and over. Miraculously,\nthat caused it to stop, but not before it tried to {verb3}\nright in front of my family. After that incident, I found {article_adjective} {adjective2}\n{noun1} in the {noun2} and decided to take it to {place} to {verb4}.')


