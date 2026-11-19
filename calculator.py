"""A simple four-operation calculator for the terminal."""


def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number, such as 5 or 2.5.")


def main():
    print("Simple Calculator")
    while True:
        operation = input("Choose +, -, *, /, or q to quit: ").strip().lower()
        if operation == "q":
            break
        if operation not in ("+", "-", "*", "/"):
            print("Please choose one of the listed operations.")
            continue

        first = read_number("First number: ")
        second = read_number("Second number: ")

        if operation == "+":
            result = first + second
        elif operation == "-":
            result = first - second
        elif operation == "*":
            result = first * second
        elif second == 0:
            print("Cannot divide by zero. Try another calculation.")
            continue
        else:
            result = first / second

        print("Result:", result)


if __name__ == "__main__":
    main()
