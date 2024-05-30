# Data Analysis - Milestone Submission
# This program reads a CVS file containing life expectancy data.

# Open the file life-expectancy.csv
with open('life-expectancy.csv') as f:

    # Create the variables for the minimum and maximum life expectancy
    min_life_expectancy = 9999
    max_life_expectancy = -1

    min_life_expectancy_year = 9999
    max_life_expectancy_year = -1

    total = 0
    count = 0
    # Skip the header line
    next(f)

    year_of_interest = int(input("Enter ther year of interest: "))

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


        if year_of_interest == year:
            total += life_expectancy
            count += 1


            if life_expectancy < min_life_expectancy_year:
               min_life_expectancy_year = life_expectancy
               min_country_year = country

            if life_expectancy > max_life_expectancy_year:
                max_life_expectancy_year = life_expectancy
                max_country_year = country
    average = total/count
    print()
    print(f"The overall min life expectancy is: {min_life_expectancy} from {min_country} in {min_year}")
    print(f"The overall max life expectancy is: {max_life_expectancy} from {max_country} in {max_year}")
    print()
    print(f"For the year {year_of_interest}:")
    print(average)
    print(f"The max life expectancy was in {max_country_year} with {max_life_expectancy_year}")
    print(f"The min life expectancy was in {min_country_year} with {min_life_expectancy_year}")
