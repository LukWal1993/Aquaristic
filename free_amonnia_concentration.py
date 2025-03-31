import math
def calculate_free_ammonia(pH, total_ammonium, temperature=25):
    """
    Calculate the amount of free ammonia (NH3) in water based on pH, 
    total ammonium concentration (NH3 + NH4+), and temperature.

    Args:
        pH (float): The pH of the water.
        total_ammonium (float): Total ammonium concentration (mg/L).
        temperature (float): Water temperature in °C. Default is 25°C.

    Returns:
        float: Concentration of free ammonia (NH3) in mg/L.
    """
    # Approximate pKa for NH3/NH4+ at different temperatures
    # Adjust pKa based on temperature
    pKa = 9.25 - (0.032 * (temperature - 25))

    # Fraction of TAN (Total Ammonia Nitrogen) that is NH3
    nh3_fraction = 1 / (1 + 10**(pKa - pH))

    # Free ammonia concentration (NH3) in mg/L
    free_ammonia = total_ammonium * nh3_fraction
    return free_ammonia


def main():
    print("Welcome to the Free Ammonia (NH3) Calculator!")
    print("This program calculates the amount of free ammonia in water based on pH and total ammonium concentration.")

    while True:
        try:
            # Input water parameters with validation
            pH = float(input("Enter the pH of the water (0-14): "))
            if 0 <= pH <= 14:
                break
            else:
                print("Error: pH must be between 0 and 14. Try again.")
        except ValueError:
            print("Error: Please enter a valid number for pH.")

    while True:
        try:
            total_ammonium = float(input("Enter total ammonium concentration (mg/L, non-negative): "))
            if total_ammonium >= 0:
                break
            else:
                print("Error: Ammonium concentration must be non-negative. Try again.")
        except ValueError:
            print("Error: Please enter a valid number for ammonium concentration.")

    while True:
        try:
            temperature_input = input("Enter the water temperature (°C, default is 25): ")
            temperature = float(temperature_input) if temperature_input else 25
            if 0 <= temperature < 100:
                break
            elif temperature < 0:
                print("Error: Temperature must be non-negative. Try again.")
            else:
                print("Error: Temperature must be lower than the boiling point (100°C). Try again.")
        except ValueError:
            print("Error: Please enter a valid number for temperature.")

    # Calculate free ammonia
    free_ammonia = calculate_free_ammonia(pH, total_ammonium, temperature)
    print(f"\nResults:")
    print(f"Free Ammonia (NH3) concentration: {free_ammonia:.3f} mg/L")


# Run the program
if __name__ == "__main__":
    main()
