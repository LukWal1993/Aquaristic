import random

def simulate_sensor_data():
    """
    Simulates sensor data for temperature, pH, and nitrate levels.

    Returns:
        dict: Dictionary containing random values for keys 'temperature', 'ph', and 'nitrate'.
    """
    temperature = round(random.uniform(20, 30), 2)
    ph = round(random.uniform(6.0, 8.5), 2)
    nitrate = round(random.uniform(0, 50), 2)
    return {'temperature': temperature, 'ph': ph, 'nitrate': nitrate}

# Safety thresholds for different aquarium types
AQUARIUM_THRESHOLDS = {
    'malawi': {
        'temperature': (24, 28),
        'ph': (7.5, 8.5),
        'nitrate': (0, 20)
    },
    'planted': {
        'temperature': (22, 26),
        'ph': (6.5, 7.5),
        'nitrate': (0, 30)
    },
    'tanganyika': {
        'temperature': (25, 27),
        'ph': (8.0, 9.0),
        'nitrate': (0, 10)
    }
}

# Map numeric choices to aquarium types
AQUARIUM_CHOICES = {
    '1': 'malawi',
    '2': 'planted',
    '3': 'tanganyika'
}

# Function to check safety levels
def check_safety_levels(data, thresholds):
    """
    Checks each parameter in the data against safety thresholds and prints an alert if any value is out of range.

    Args:
        data (dict): Dictionary containing the current sensor data
        thresholds (dict): Dictionary with safety thresholds for each parameter
    """
    for param, (min_val, max_val) in thresholds.items():
        value = data[param]
        if value < min_val:
            print(f"Alert: {param.capitalize()} is too low! Current value: {value}")
        elif value > max_val:
            print(f"Alert: {param.capitalize()} is too high! Current value: {value}")
        else:
            print(f"{param.capitalize()} is within the safe range.")

# Aquarium type selection with numeric choices
print("Choose your aquarium type:")
print("1 - Malawi")
print("2 - Planted")
print("3 - Tanganyika")
choice = input("Enter the number corresponding to your aquarium type (1, 2, or 3): ")

# Check if the choice is valid and assign the corresponding thresholds
if choice in AQUARIUM_CHOICES:
    aquarium_type = AQUARIUM_CHOICES[choice]
    selected_thresholds = AQUARIUM_THRESHOLDS[aquarium_type]
    print(f"Selected aquarium type: {aquarium_type.capitalize()}")
    # Simulate sensor data and check safety levels
    sensor_data = simulate_sensor_data()
    print("Sensor data:", sensor_data)
    check_safety_levels(sensor_data, selected_thresholds)
else:
    print("Invalid choice. Please enter 1, 2, or 3.")
