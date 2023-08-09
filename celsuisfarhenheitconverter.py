def main():
    main_menu()

def main_menu():
    welcome_intro()
    compute_conversion()

def welcome_intro():
    print("Welcome to Celsius and Fahrenheit converter")

def menu():
    print("Main Menu")
    print("a. Celsius to Fahrenheit")
    print("b. Fahrenheit to Celsius")
    conv = input("Select a conversion (a/b): ")
    return conv

def celsius_to_fahrenheit(celsius):
    while celsius < 1:
        celsius = float(input("Please enter celsius as a number greater than zero(0): "))
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    while fahrenheit < 1:
        fahrenheit = float(input("Please enter fahrenheit as a number greater than zero(0): "))
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def compute_conversion():
    selected = menu()
    if selected == "a":
        celsius = float(input("Enter celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:.2f} Celsius is equal to {fahrenheit:.2f} Fahrenheit.")
    elif selected == "b":
        fahrenheit = float(input("Enter fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit:.2f} Fahrenheit is equal to {celsius:.2f} Celsius.")
    else:
        print("You did not enter a valid selection.")
    
    convert = input("Would you like to perform another conversion? (y/n): ").upper()
    if convert == "Y":
        compute_conversion()
    else:
        print("Thanks, bye!")

main()
