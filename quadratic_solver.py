import math


def solve_quadratic(a, b, c):
    disc = b ** 2 - 4 * a * c
    if disc < 0:
        print("The equation has no real roots.")
        return

    # Calculate the two roots of the quadratic equation
    root1 = (-b + math.sqrt(disc)) / (2 * a)
    root2 = (-b - math.sqrt(disc)) / (2 * a)

    return root1, root2


# Read the coefficients of the quadratic equation
a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant: "))

# Solve the quadratic equation
roots = solve_quadratic(a, b, c)

# Print the roots
print("The roots are:", roots)
