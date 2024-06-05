# Data Analysis - Milestone Submission
# This program reads a CVS file containing life expectancy data.

# Open the file life-expectancy.csv
with open('life-expectancy.csv') as f:

    action = -1
    while action != 0:

        # Create the variables for the minimum and maximum life expectancy
        min_life_expectancy = 9999
        max_life_expectancy = -1

        min_life_expectancy_year = 9999
        max_life_expectancy_year = -1
        total = 0
        count = 0

        # Display the menu to the user
        print()
        print("Choose the action you want to: ")
        print("1. Year of your interest:")
        print("2. Country of your interest:")
        print("0. Exit")

        # Read the input for action selection
        action = int(input("Enter the action you want to: "))

        if action == 1:
            # User selected to find data by year
            year_of_interest = int(
                input("Enter the year of interest: "))

            # Reset the file pointer to the beginning and skip the header line
            f.seek(0)
            next(f)

            # Start the loop to read each line in the file
            for line in f:

                # Remove the white space from the line
                line = line.strip()

                # Split the line into parts using comma as the delimiter
                parts = line.split(",")

                # Assign each part to a corresponding variable
                country = parts[0]
                code = parts[1]
                year = int(parts[2])
                life_expectancy = float(parts[3])

                # Update the minimum and maximum life expectancy
                if life_expectancy < min_life_expectancy:
                    min_life_expectancy = life_expectancy
                    min_country = country
                    min_year = year

                if life_expectancy > max_life_expectancy:
                    max_life_expectancy = life_expectancy
                    max_country = country
                    max_year = year

                # Aggregate data for the year of interest
                if year_of_interest == year:
                    total += life_expectancy
                    count += 1

                    if life_expectancy < min_life_expectancy_year:
                        min_life_expectancy_year = life_expectancy
                        min_country_year = country

                    if life_expectancy > max_life_expectancy_year:
                        max_life_expectancy_year = life_expectancy
                        max_country_year = country

            # Calculate and print results for the year of interest
            if count > 0:
                average = total/count
                print()
                print(f"The overall max life expectancy is: {
                      max_life_expectancy} from {max_country} in {max_year}")
                print(f"The overall min life expectancy is: {
                      min_life_expectancy} from {min_country} in {min_year}")
                print()
                print(f"For the year {year_of_interest}:")
                print(f"The average life expectancy across all countries was {
                      average:.2f}")
                print(f"The max life expectancy was in {
                      max_country_year} with {max_life_expectancy_year}")
                print(f"The min life expectancy was in {
                      min_country_year} with {min_life_expectancy_year}")
            else:
                print(f"No data available for the year {year_of_interest}")

        elif action == 2:
            # User selected to find data by country
            country_of_interest = input(
                "Enter the country of interest: ").strip().capitalize()

            # Reset the file pointer to the beginning and skip the header line
            f.seek(0)
            next(f)

            # Start the loop to read each line in the file
            for line in f:

                # Remove the white space from the line
                line = line.strip()

                # Split the line into parts using comma as the delimiter
                parts = line.split(",")

                # Assign each part to a corresponding variable
                country = parts[0]
                code = parts[1]
                year = int(parts[2])
                life_expectancy = float(parts[3])

                # Aggregate data for the country of interest
                if country_of_interest == country:
                    total += life_expectancy
                    count += 1

                    if life_expectancy < min_life_expectancy_year:
                        min_life_expectancy_year = life_expectancy
                        min_country_year = country
                        min_country = country
                        min_year = year

                    if life_expectancy > max_life_expectancy_year:
                        max_life_expectancy_year = life_expectancy
                        max_country_year = country
                        max_country = country
                        max_year = year

            # Calculate and print results for the country of interest
            if count > 0:
                average = total / count
                print()
                print(f"For the country {country_of_interest}:")
                print(f"The average life expectancy across {country_of_interest} was {
                    average:.2f}")
                print(f"The max life expectancy in {
                    max_country_year} was {max_life_expectancy_year} in {max_year}.")
                print(f"The min life expectancy in {
                    min_country_year} was {min_life_expectancy_year} in {min_year}.")

            else:
                print(f"No data available for the country {
                      country_of_interest.capitalize()}")

        elif action == 0:
            # User selected to exit
            print("Goodbye!")
        else:
            print("Invalid action")
