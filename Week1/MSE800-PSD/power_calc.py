try:
        base = float(input("Enter base (x): "))
        exponent = float(input("Enter exponent (y): "))
        result = base ** exponent
        print("Result :", result)
except ValueError:
        print("Please enter valid numbers.")