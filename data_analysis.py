# Data Analysis - Milestone Submission
# This program reads a CVS file containing life expectancy data.

# Open the file life-expectancy.csv
with open('life-expectancy.csv') as f:

    # Create the variables for the minimum and maximum life expectancy
    min_life_expectancy = 9999
    max_life_expectancy = -1

    # Skip the header line
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

        if life_expectancy > max_life_expectancy:
            max_life_expectancy = life_expectancy

    print(f"The overall min life expectancy is: {min_life_expectancy}")
    print(f"The overall max life expectancy is: {max_life_expectancy}")
