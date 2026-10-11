#===========================================================
# PROJECT 7: MODULAR & PACKAGER
#===========================================================



import datetime
import time
import math
import random
import uuid
import os
import secrets
import string


SEPARATOR = "=" * 40


def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            current = datetime.datetime.now()
            print("\nCurrent Date and Time:", current.strftime(
                "%Y-%m-%d %H:%M:%S"
            ))

        elif choice == "2":
            try:
                date1 = input("Enter the first date (YYYY-MM-DD): ")
                date2 = input("Enter the second date (YYYY-MM-DD): ")

                d1 = datetime.datetime.strptime(date1, "%Y-%m-%d").date()
                d2 = datetime.datetime.strptime(date2, "%Y-%m-%d").date()

                difference = abs((d2 - d1).days)
                print("Difference:", difference, "days")

            except ValueError:
                print("Invalid date! Please use YYYY-MM-DD.")

        elif choice == "3":
            now = datetime.datetime.now()
            print("Formatted Date:", now.strftime("%d-%m-%Y"))
            print("Formatted Time:", now.strftime("%I:%M:%S %p"))
            print("Day:", now.strftime("%A"))
            print("Month:", now.strftime("%B"))

        elif choice == "4":
            input("Press Enter to start the stopwatch...")
            start = time.perf_counter()
            input("Press Enter to stop the stopwatch...")
            elapsed = time.perf_counter() - start
            print(f"Elapsed Time: {elapsed:.2f} seconds")

        elif choice == "5":
            try:
                seconds = int(input("Enter countdown seconds: "))

                if seconds < 0:
                    print("Please enter a non-negative number.")
                    continue

                while seconds > 0:
                    print(f"Time remaining: {seconds} seconds")
                    time.sleep(1)
                    seconds -= 1

                print("Countdown completed!")

            except ValueError:
                print("Please enter a valid whole number.")

        elif choice == "6":
            break

        else:
            print("Invalid choice! Try again.")



def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                number = int(input("Enter a number: "))

                if number < 0:
                    print("Factorial is not defined for negative integers.")
                else:
                    print("Factorial:", math.factorial(number))

            except ValueError:
                print("Please enter a valid integer.")

        elif choice == "2":
            try:
                principal = float(input("Enter principal amount: "))
                rate = float(input("Enter annual interest rate (%): "))
                years = float(input("Enter time (in years): "))

                if principal < 0 or rate < 0 or years < 0:
                    print("Values cannot be negative.")
                    continue

                amount = principal * (1 + rate / 100) ** years
                interest = amount - principal

                print(f"Final Amount: {amount:.2f}")
                print(f"Compound Interest: {interest:.2f}")

            except ValueError:
                print("Please enter valid numerical values.")

        elif choice == "3":
            try:
                angle = float(input("Enter angle in degrees: "))
                radians = math.radians(angle)

                print(f"Sin({angle}): {math.sin(radians):.4f}")
                print(f"Cos({angle}): {math.cos(radians):.4f}")
                print(f"Tan({angle}): {math.tan(radians):.4f}")

            except ValueError:
                print("Please enter a valid angle.")

        elif choice == "4":
            print("\nGeometric Shapes:")
            print("1. Circle")
            print("2. Rectangle")
            print("3. Triangle")
            print("4. Square")

            shape = input("Choose a shape: ")

            try:
                if shape == "1":
                    radius = float(input("Enter radius: "))
                    if radius < 0:
                        print("Radius cannot be negative.")
                    else:
                        print("Area of Circle:", round(
                            math.pi * radius ** 2, 2
                        ))

                elif shape == "2":
                    length = float(input("Enter length: "))
                    width = float(input("Enter width: "))
                    if length < 0 or width < 0:
                        print("Dimensions cannot be negative.")
                    else:
                        print("Area of Rectangle:", length * width)

                elif shape == "3":
                    base = float(input("Enter base: "))
                    height = float(input("Enter height: "))
                    if base < 0 or height < 0:
                        print("Dimensions cannot be negative.")
                    else:
                        print("Area of Triangle:", 0.5 * base * height)

                elif shape == "4":
                    side = float(input("Enter side: "))
                    if side < 0:
                        print("Side cannot be negative.")
                    else:
                        print("Area of Square:", side ** 2)

                else:
                    print("Invalid shape choice.")

            except ValueError:
                print("Please enter valid dimensions.")

        elif choice == "5":
            break

        else:
            print("Invalid choice! Try again.")



def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                low = int(input("Enter minimum number: "))
                high = int(input("Enter maximum number: "))

                if low > high:
                    print("Minimum cannot exceed maximum.")
                else:
                    print("Random Number:", random.randint(low, high))

            except ValueError:
                print("Enter valid integers.")

        elif choice == "2":
            try:
                count = int(input("How many numbers? "))
                low = int(input("Enter minimum number: "))
                high = int(input("Enter maximum number: "))

                if count < 0 or low > high:
                    print("Invalid range or list size.")
                else:
                    values = [
                        random.randint(low, high)
                        for _ in range(count)
                    ]
                    print("Random List:", values)

            except ValueError:
                print("Enter valid integers.")

        elif choice == "3":
            try:
                length = int(input("Enter password length: "))

                if length < 1:
                    print("Length must be at least 1.")
                    continue

                characters = string.ascii_letters + string.digits + "!@#$%"
                password = "".join(
                    secrets.choice(characters)
                    for _ in range(length)
                )

                print("Generated Password:", password)

            except ValueError:
                print("Enter a valid password length.")

        elif choice == "4":
            otp = "".join(
                secrets.choice(string.digits) for _ in range(6)
            )
            print("Generated OTP:", otp)
            print("Demo only: Do not use this as a real authentication system.")

        elif choice == "5":
            break

        else:
            print("Invalid choice! Try again.")



def uuid_menu():
    print("\nGenerate Unique Identifiers:")
    print("1. Generate UUID1")
    print("2. Generate UUID4")
    print("3. Back to Main Menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Generated UUID1:", uuid.uuid1())

    elif choice == "2":
        print("Generated UUID4:", uuid.uuid4())

    elif choice == "3":
        return

    else:
        print("Invalid choice!")



def file_menu():
    while True:
        print("\nFile Operations (Custom Module):")
        print("1. Create a New File")
        print("2. Write to a File")
        print("3. Read from a File")
        print("4. Append to a File")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "5":
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice!")
            continue

        filename = input("Enter file name: ").strip()

        if not filename:
            print("File name cannot be empty.")
            continue

        # Use only a file name in the current working directory.
        if os.path.basename(filename) != filename:
            print("Please enter a file name without a directory path.")
            continue

        try:
            if choice == "1":
                with open(filename, "x", encoding="utf-8") as file:
                    file.write("")
                print("File created successfully!")

            elif choice == "2":
                content = input("Enter data to write: ")

                with open(filename, "w", encoding="utf-8") as file:
                    file.write(content)

                print("Data written successfully!")

            elif choice == "3":
                with open(filename, "r", encoding="utf-8") as file:
                    print("\nFile Content:")
                    print(file.read())

            elif choice == "4":
                content = input("Enter data to append: ")

                with open(filename, "a", encoding="utf-8") as file:
                    file.write(content + "\n")

                print("Data appended successfully!")

        except FileExistsError:
            print("File already exists!")

        except FileNotFoundError:
            print("File not found. Create or write to it first.")

        except OSError as error:
            print("File operation error:", error)


def explore_modules():
    print("\nExplore Module Attributes (dir()):")
    print("1. math")
    print("2. random")
    print("3. datetime")
    print("4. os")
    print("5. Back to Main Menu")

    choice = input("Enter module choice: ")

    modules = {
        "1": ("math", math),
        "2": ("random", random),
        "3": ("datetime", datetime),
        "4": ("os", os)
    }

    if choice in modules:
        name, module = modules[choice]
        print(f"\nModule Name: {name}")
        print("Available Attributes:")
        print(dir(module))
    elif choice == "5":
        return
    else:
        print("Invalid choice!")



def main():
    while True:
        print("\n" + SEPARATOR)
        print("Welcome to Multi-Utility Toolkit")
        print(SEPARATOR)
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print(SEPARATOR)

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()

        elif choice == "2":
            math_menu()

        elif choice == "3":
            random_menu()

        elif choice == "4":
            uuid_menu()

        elif choice == "5":
            file_menu()

        elif choice == "6":
            explore_modules()

        elif choice == "7":
            print("\n" + SEPARATOR)
            print("Thank you for using the Multi-Utility Toolkit!")
            print(SEPARATOR)
            break

        else:
            print("Invalid choice! Please select 1-7.")



if __name__ == "__main__":
    main()