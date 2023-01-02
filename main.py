from models.calculator import Calculator


def main() -> None:

    while True:
        print("A. Addition")
        print("B. Substraction")
        print("C. Multiplication")
        print("D. Division")
        print("E. Exit")

        choice: str = (
            str(input("Input your choice: ")).strip().upper()
        )  # Convert to string, remove any leading/trailing whitespace, and return uppercase string

        if choice == "A":
            print("Addition")
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            Calculator.add(a, b)
        elif choice == "B":
            print("Substraction")
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            Calculator.sub(a, b)
        elif choice == "C":
            print("Multiplication")
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            Calculator.mult(a, b)
        elif choice == "D":
            print("Division")
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            Calculator.div(a, b)
        elif choice == "E":
            print("Program Ended\n")
            quit()
        else:
            print("Invalid input\n")


main()
