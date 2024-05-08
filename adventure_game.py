# Adventure Game Project - Milestone submission
# This is a fun project, where the user have to choose an option to complete the game.


# Main game loop
while True:

    print()
    # Introduction to the game
    print("You are about to enter the Madidi, which is a national reserve located in Bolivia.")
    print("You have two paths to arrive to first stop, that is a local indigenous community:")
    print()
    print("1. The LARGEST path is safe, but we need to be quiet because the area is the habitat of the jaguar🐯.")
    print()
    print("2. The SHORTEST path is dangerous, it traverses through mountains and has waterfalls.")
    print()

    # Convert path_choice to lowercase
    path_choice = input(
        "Which path will you take? LARGEST or SHORTEST: ").lower()
    print()

    # User chose the largest path
    if path_choice == "largest":
        print("You have two options to reach your destination:")
        print()
        print("1. The BICYCLE option might get you there faster, but it could also attract the attention of the jaguar.")
        print()
        print("2. The WALKAWAY option might take longer to get there, but it could also avoid attracting the attention of the jaguar.")
        print()

        # Convert the option to lowercase
        bicycle_walk = input(
            "Which option will you take? BICYCLE or WALKAWAY: ").lower()
        print()

        # User chose the bicycle
        if bicycle_walk == 'bicycle':
            print("When you're halfway through your journey, the jaguar appears in front of you. You have two options at this point:")
            print()
            print("1. The BACKAWAY option will take you back to the beginning of the journey.")
            print()
            print("2. The CONFRONT option entails facing the jaguar directly, if you win, you'll could arrive at your destination, but there's a rick of death.")
            print()

            # Convert the option to lowercase
            backaway_confront = input(
                "Which option will you take? BACKAWAY or CONFRONT: ").lower()
            print()

            # User chose BACKAWAY
            if backaway_confront == "backaway":
                print("You rode🚵‍♀️ too fast, and the jaguar🐯 couldn't catch you. You arrive back at the beginning of your journey.")

            # User chose CONFRONT
            elif backaway_confront == 'confront':
                print("You make a lot of noise, and the jaguar🐯 is afraid and run into the forest. You ride and arrive at the local indigenous community.")

            # When user chooses a invalid option
            else:
                print("Invalid choice. Please enter BACKAWAY or CONFRONT")

        # User chose walkaway
        elif bicycle_walk == 'walkaway':
            print()

        # When the user chooses a invalid option
        else:
            print("Invalid choice. Please enter BICYCLE or WALKAWAY")

    # You chose the shortest path
    elif path_choice == 'shortest':
        print()

    # When the user chooses a invalid option
    else:
        print("Invalid choice. Please enter LARGEST or SHORTEST")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print()
        print("Thank you for playing!")
        break
