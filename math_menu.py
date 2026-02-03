import math
import statistics
import io
import contextlib

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

def descriptive_stats(values=None):
    if values is None:
        values = []
        for i in range(10):
            val = float(input(f"Enter value {i+1}: "))
            values.append(val)
        mean = statistics.mean(values)
        median = statistics.median(values)
        try:
            mode = statistics.mode(values)
        except statistics.StatisticsError:
            mode = "No unique mode"
        stdev = statistics.stdev(values)
        min_val = min(values)
        max_val = max(values)
        range_val = max_val - min_val
        print(f"Mean: {mean:.2f}")
        print(f"Median: {median:.2f}")
        print(f"Mode: {mode}")
        print(f"Standard Deviation: {stdev:.2f}")
        print(f"Min: {min_val:.2f}")
        print(f"Max: {max_val:.2f}")
        print(f"Range: {range_val:.2f}")
    else:
        # values provided by caller (e.g. GUI): compute and return a string
        mean = statistics.mean(values)
        median = statistics.median(values)
        try:
            mode = statistics.mode(values)
        except statistics.StatisticsError:
            mode = "No unique mode"
        stdev = statistics.stdev(values) if len(values) > 1 else 0.0
        min_val = min(values)
        max_val = max(values)
        range_val = max_val - min_val
        out = []
        out.append(f"Mean: {mean:.2f}")
        out.append(f"Median: {median:.2f}")
        out.append(f"Mode: {mode}")
        out.append(f"Standard Deviation: {stdev:.2f}")
        out.append(f"Min: {min_val:.2f}")
        out.append(f"Max: {max_val:.2f}")
        out.append(f"Range: {range_val:.2f}")
        return "\n".join(out)

# Helpers to capture printed output from the existing functions for the GUI
def _capture_output(func, *args, **kwargs):
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        func(*args, **kwargs)
    return f.getvalue()

def get_fibonacci(n):
    return _capture_output(fibonacci, n)

def get_factorial(n):
    return _capture_output(factorial, n)

def get_multiplication_table(n):
    return _capture_output(multiplication_table, n)

def get_exponentiation_table(base, exp):
    return _capture_output(exponentiation_table, base, exp)

def get_trigonometry(angle_deg):
    return _capture_output(trigonometry, angle_deg)

def get_descriptive_stats_from_values(values):
    return descriptive_stats(values)

def main():
    while True:
        print("\nMath Menu:")

        print("1. Fibonacci")
        print("2. Factorial")
        print("3. Multiplication Table")
        print("4. Exponentiation Table")
        print("5. Trigonometry")
        print("6. Descriptive Statistics")
        print("7. Exit")
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
            descriptive_stats()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()