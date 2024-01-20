def main():
    mass_kg = int(input("Enter mass in kilograms: "))
    energy_joules = mass_kg * (3 * 10** 8)** 2  # Using E = mc^2 formula
    print("Equivalent energy in Joules:", energy_joules)

main()