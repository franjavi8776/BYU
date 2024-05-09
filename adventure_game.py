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

    # Convert option to lowercase
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
            print(
                "1. The BACKAWAY option will take you back to the beginning of the journey.")
            print()
            print("2. The CONFRONT option entails facing the jaguar directly, if you win, you'll could arrive at your destination, but there's a rick of death.")
            print()

            # Convert the option to lowercase
            backaway_confront = input(
                "Which option will you take? BACKAWAY or CONFRONT: ").lower()
            print()

            # User chose BACKAWAY
            if backaway_confront == "backaway":
                print(
                    "You rode too fast, and the jaguar couldn't catch you. You arrive back at the beginning of your journey.")

            # User chose CONFRONT
            elif backaway_confront == 'confront':
                print("You make a lot of noise, and the jaguar is afraid and run into the forest. You ride and arrive at the local indigenous community.")

            # When user chooses a invalid option
            else:
                print("Invalid choice. Please enter BACKAWAY or CONFRONT.")

        # User chose walkaway
        elif bicycle_walk == 'walkaway':
            print("When you're in the fourth part of the journey, you fall down, and your water spills. You have to options:")
            print()
            print(
                "1. The BACKAWAY option will take you back to the beginning of the journey.")
            print()
            print("2. The KEEPGOING option will put you at risk of dehydration and death")
            print()

            # Convert the option to lowercase
            backaway_keepGoing = input(
                "Which option will you take? BACKAWAY or KEEPGOING: ").lower()
            print()

            # User chose BACKAWAY
            if backaway_keepGoing == "backaway":
                print(
                    "You run too fast and arrive safely at the beginning of your journey.")

            # User chose KEEPGOING
            elif backaway_keepGoing == 'keepgoing':
                print("You keep going along the path, and when you were very tired and thirsty, you saw a river beside the path. You get water and rest, and then continue until finally arriving at the local indigenous community.")

            # When user chooses a invalid option
            else:
                print("Invalid choice. Please enter BACKAWAY or KEEPGOING.")

        # When the user chooses a invalid option
        else:
            print("Invalid choice. Please enter BICYCLE or WALKAWAY")

    # User chose the shortest path
    elif path_choice == 'shortest':
        print("You have two options to reach your destination:")
        print()
        print("1. The PARAGLIDING option might get you there faster, but it is very dangerous.")
        print()
        print("2. The WALKAWAY option might take longer to get there, but it could also keep you out of danger.")
        print()

        # Convert the option to lowercase
        paragliding_walk = input(
            "Which option will you take? PARAGLIDING or WALKAWAY: ").lower()
        print()

        # User chose the bicycle
        if paragliding_walk == 'paragliding':
            print("When you're on the top of the mountain, you feel afraid about paragliding, you have two option now:")
            print()
            print(
                "1. The BACKAWAY option will take you back to the beginning of the journey.")
            print()
            print("2. The GOPARAGLIDING option entails facing death directly, if you succeed, you could arrive at your destination.")
            print()

            # Convert the option to lowercase
            backaway_goparagliding = input(
                "Which option will you take? BACKAWAY or GOPARAGLIDING: ").lower()
            print()

            # User chose BACKAWAY
            if backaway_goparagliding == "backaway":
                print(
                    "You descend the mountain too fast, and arrive safely at the beginning of your journey.")

            # User chose GOPARAGLIDING
            elif backaway_goparagliding == 'goparagliding':
                print("When you're almost at your destination, one of the paragliding wing breaks, causing you fall into the river. You swim and arrive at the local indigenous community.")

            # When user chooses a invalid option
            else:
                print("Invalid choice. Please enter BACKAWAY or GOPARAGLIDING, ")

        # User chose walkaway
        elif paragliding_walk == 'walkaway':
            print("When you're in the fourth part of the journey, you are very tired, but you arrive at the waterfall, you have two options at this point:")
            print()
            print(
                "1. The BACKAWAY option will take you back to the beginning of the journey.")
            print()
            print(
                "2. The JUMP option will put you at risk of fracturing your bones and death.")
            print()

            # Convert the option to lowercase
            backaway_jump = input(
                "Which option will you take? BACKAWAY or jump: ").lower()
            print()

            # User chose BACKAWAY
            if backaway_jump == "backaway":
                print(
                    "You decent too fast and arrive safely at the beginning of your journey.")

            # User chose JUMP
            elif backaway_jump == 'jump':
                print(
                    "You jump into the waterfall , luckily the water is deep, and you swim at the local indigenous community.")

            # When user chooses a invalid option
            else:
                print("Invalid choice. Please enter BACKAWAY or JUMP.")

        # When the user chooses a invalid option
        else:
            print("Invalid choice. Please enter PARAGLIDING or WALKAWAY")

        # When the user chooses a invalid option
    else:
        print("Invalid choice. Please enter LARGEST or SHORTEST")

    # Asking the user to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print()
        print("Thank you for playing!")
        break
