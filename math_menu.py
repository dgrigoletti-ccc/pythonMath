import math

def fibonacci(n):
    if n <= 0:
        print("Please enter a positive integer")
        return
    a, b = 0, 1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

def factorial(n):
    if n < 0:
        print("Factorial not defined for negative numbers")
        return
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"Factorial of {n} is {result}")

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def exponentiation_table(base, exp):
    for i in range(1, exp + 1):
        print(f"{base}^{i} = {base ** i}")

def trigonometry(angle_deg):
    angle_rad = math.radians(angle_deg)
    print(f"sin({angle_deg}°) = {math.sin(angle_rad):.4f}")
    print(f"cos({angle_deg}°) = {math.cos(angle_rad):.4f}")
    print(f"tan({angle_deg}°) = {math.tan(angle_rad):.4f}")

def main():
    while True:
        print("\nMenu:")
        print("1. Fibonacci")
        print("2. Factorial")
        print("3. Multiplication Table")
        print("4. Exponentiation Table")
        print("5. Trigonometry")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            n = int(input("Enter number of terms: "))
            fibonacci(n)
        elif choice == '2':
            n = int(input("Enter number: "))
            factorial(n)
        elif choice == '3':
            n = int(input("Enter number: "))
            multiplication_table(n)
        elif choice == '4':
            base = int(input("Enter base: "))
            exp = int(input("Enter max exponent: "))
            exponentiation_table(base, exp)
        elif choice == '5':
            angle = float(input("Enter angle in degrees: "))
            trigonometry(angle)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()