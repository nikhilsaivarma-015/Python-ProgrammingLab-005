import math  # required for pi in area of circle calculation
 
# Personal Utility Toolkit - menu-driven program
while True:
    # Display the menu
    print("\n========== PERSONAL UTILITY TOOL ==========")
    print("1. Celsius to Fahrenheit Conversion")
    print("2. Fahrenheit to Celsius Conversion")
    print("3. Calculate Area of Circle")
    print("4. Calculate Area of Rectangle")
    print("5. Calculate Simple Interest")
    print("6. Calculate Body Mass Index (BMI)")
    print("7. Exit")
 
    # Accept user's choice (type conversion: str -> int)
    choice = int(input("Enter your choice (1-7): "))
 
    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"Temperature in Fahrenheit = {fahrenheit:.2f} F")
 
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"Temperature in Celsius = {celsius:.2f} C")
 
    elif choice == 3:
        radius = float(input("Enter radius of circle: "))
        area_circle = math.pi * radius ** 2
        print(f"Area of Circle = {area_circle:.2f} sq. units")
 
    elif choice == 4:
        length = float(input("Enter length of rectangle: "))
        width = float(input("Enter width of rectangle: "))
        area_rectangle = length * width
        print(f"Area of Rectangle = {area_rectangle:.2f} sq. units")
 
    elif choice == 5:
        principal = float(input("Enter Principal Amount: "))
        rate = float(input("Enter Rate of Interest (%): "))
        time = float(input("Enter Time (in years): "))
        simple_interest = (principal * rate * time) / 100
        print(f"Simple Interest = Rs. {simple_interest:.2f}")
 
    elif choice == 6:
        weight = float(input("Enter Weight (in kg): "))
        height = float(input("Enter Height (in m): "))
        bmi = weight / (height ** 2)
        print(f"Body Mass Index (BMI) = {bmi:.2f}")
 
    elif choice == 7:
        print("Thank you for using the Personal Utility Tool!")
        break
 
    else:
        print("Invalid choice. Please select a valid option.")
