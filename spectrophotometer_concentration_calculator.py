import numpy as np


def main():
    print("Welcome to the spectrophotometer concentration calculator!")
    print("Provide calibration points (concentration, absorbance). Type 'done' to finish.")

    concentrations = []
    absorbances = []

    # Collecting calibration points from the user
    while True:
        try:
            concentration = input(
                "Enter concentration (or 'done' to finish): ")
            if concentration.lower() == 'done':
                break
            absorbance = input("Enter absorbance for this concentration: ")

            concentrations.append(float(concentration))
            absorbances.append(float(absorbance))
        except ValueError:
            print("Invalid input. Please enter numerical values.")

    if len(concentrations) < 2:
        print("Error: At least two calibration points are required.")
        return

    # Calculate the slope (epsilon) and intercept of the calibration curve
    slope, intercept = np.polyfit(concentrations, absorbances, 1)
    print(f"Calibration curve equation: Absorbance = {
          slope:.3f} * Concentration + {intercept:.3f}")

    # Get the absorbance of the sample
    try:
        sample_absorbance = float(
            input("Enter the absorbance of the sample: "))
        # Calculate the concentration of the sample
        sample_concentration = (sample_absorbance - intercept) / slope
        print(f"Calculated concentration of the sample: {
              sample_concentration:.3f}")
    except ValueError:
        print("Invalid input. Please enter a numerical value for absorbance.")
    except ZeroDivisionError:
        print("Error: The calibration curve slope is zero, cannot calculate concentration.")


# Run the program
main()
