# Adventure Game Project - Milestone submission
# This is a fun project, where the user have to choose an option to complete the game.

# Introduction to the game
print('You are about to enter the Madidi, which is a national reserve located in Bolivia.')
print('You have to paths to arrive to first stop, that is a local indigenous community.')

print()

# Convert path_choise to lowercase
path_choice = input('Which path will you take? LARGEST OR SHORTEST: ').lower()

print()

if path_choice == 'largest':
  print("The largest path is safe, but we need to be quiet because the area is the habitat of the jaguar🐯.")
elif path_choice == 'shortest':
  print("The shortest path is dangerous, it traverses through mountains and has waterfalls.")
else:
  print("Invalid choice. Please enter LARGEST or SHORTEST")


