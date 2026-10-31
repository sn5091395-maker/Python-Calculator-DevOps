
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def modulus(a, b):
    if b == 0:
        raise ValueError("Cannot calculate modulus with zero")
    return a % b


def power(a, b):
    return a ** b


def main():
    print("===== PYTHON CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")

    try:
        choice = int(input("Enter your choice (1-6): "))

        if choice not in range(1, 7):
            print("Invalid choice")
            return

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        operations = {
            1: add,
            2: subtract,
            3: multiply,
            4: divide,
            5: modulus,
            6: power
        }

        result = operations[choice](a, b)
        print("Result:", result)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
