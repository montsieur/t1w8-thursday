def divide_numbers():
    try:
        # Get input from the user
        dividend = float(input("Enter the dividend: "))
        divisor = float(input("Enter the divisor: "))

        # Perform the division
        result = dividend / divisor
        print(f"result of division: {result}.")

    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")

    except ValueError:
        print("Error! Please enter valid numbers.")

    except Exception as e:
        print(f"Unexpected error occured: {e}")

    finally:
        print("Division operation closed.")

# Perform the division
divide_numbers()

    