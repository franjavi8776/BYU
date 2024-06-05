# Program to calculate wind chill based on temperature and wind speed

# Prompt user for temperature
userTemperature = float(input("What is the temperature? "))

# Prompt user for temperature unit
forC = input("Fahrenheit or Celsius (F/C)? ").upper()

# Convert temperature to Fahrenheit if it's in Celsius
if forC == "C":
    userTemperature = (userTemperature * (9/5)) + 32


def windChill(V):

    # Formula to calculate wind chill
    wind_chill = 35.74 + (0.6215*userTemperature) - 35.75 * \
        (V**0.16) + (0.4275*userTemperature)*(V**0.16)

    # Print wind chill
    print(f"At temperature {userTemperature:.1f}F, and wind speed {
          V} mph, the windchill is: {wind_chill:.2f}F")


# Loop to calculate wind chill for wind speeds from 5 to 60mph, in increments of 5
for V in range(5, 60, 5):
    windChill(V)
