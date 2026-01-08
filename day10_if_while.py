while True:
    user_input = input("Enter a number (0 to exit): ").strip()

    # Validate input
    if user_input == "0":
        print("Bye.")
        break

    if not user_input.isdigit():
        print("Invalid input. Please enter a positive integer (example: 5).")
        continue

    num = int(user_input)

    # Compare with 10
    if num < 10:
        print("Less than 10")
    elif num == 10:
        print("Equal to 10")
    else:
        print("Greater than 10")
