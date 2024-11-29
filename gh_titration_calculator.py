def main():
    print("Welcome to the General Hardness (GH) Calculator!")
    print("This program calculates water hardness in multiple units using titration data.")

    try:
        # Input EDTA titre in moles/L (M)
        edta_titre = float(
            input("Enter the titre of EDTA solution (moles/L): "))
        if edta_titre <= 0:
            print("EDTA titre must be a positive value.")
            return

        # Input water sample volume in milliliters (mL)
        sample_volume = float(
            input("Enter the volume of the water sample (mL): "))
        if sample_volume <= 0:
            print("Sample volume must be a positive value.")
            return

        # Input titrant volume used in milliliters (mL)
        titrant_volume = float(
            input("Enter the volume of titrant added (mL): "))
        if titrant_volume <= 0:
            print("Titrant volume must be a positive value.")
            return

        # Calculation: moles of EDTA used
        moles_edta = edta_titre * titrant_volume / \
            1000  # Convert titrant volume to liters

        # Calcium carbonate equivalent in mg (assuming molar mass CaCO₃ = 100.0869 g/mol)
        mg_caco3 = (moles_edta * 100.0869 / sample_volume) * \
            1000000  # mg/L CaCO₃
        print(mg_caco3)

        # Conversion to other units
        degrees_german = mg_caco3 / 17.848  # °dH
        degrees_french = mg_caco3 / 10      # °fH
        # ppm (parts per million, equivalent to mg/L CaCO₃)
        ppm = mg_caco3

        # Display results
        print("\nResults:")
        print(f"General Hardness (GH) in °dH (German degrees): {
              degrees_german:.2f}")
        print(f"General Hardness (GH) in °fH (French degrees): {
              degrees_french:.2f}")
        print(f"General Hardness (GH) in ppm (mg/L CaCO₃): {ppm:.2f}")

    except ValueError:
        print("Invalid input. Please enter numerical values.")


# Run the program
if __name__ == "__main__":
    main()
