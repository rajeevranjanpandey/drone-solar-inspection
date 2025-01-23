import os
import random
import time

# Sample data to simulate drone inspection
SOLAR_PANEL_COUNT = 10
INSPECTION_DATA = {f"Panel_{i}": random.choice(["Healthy", "Damaged"]) for i in range(1, SOLAR_PANEL_COUNT + 1)}

def inspect_solar_panels():
    """
    Simulates the inspection of solar panels by a drone.
    """
    print("Starting drone inspection...\n")
    for panel, status in INSPECTION_DATA.items():
        time.sleep(0.5)  # Simulate drone processing time
        print(f"Inspecting {panel}... Status: {status}")
    print("\nInspection complete!")

def save_results(directory="results"):
    """
    Saves the inspection results to a file.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    results_file = os.path.join(directory, "inspection_results.txt")
    with open(results_file, "w") as file:
        for panel, status in INSPECTION_DATA.items():
            file.write(f"{panel}: {status}\n")
    print(f"\nInspection results saved to {results_file}")
    

if __name__ == "__main__":
    inspect_solar_panels()
    save_results()
