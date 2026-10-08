print("welcome to the pattern generator and number analyzer")

while True:
    print("\nMenu:")
    print("1. generate pattern")
    print("2. number analysis")
    print("3. exit")

    choice = input("enter your choice (1-3):")

    # pattern generation

    if choice == "1":
        print("\npattern generation")
        print("1. right-angled triangle")
        print("2. back to main menu")

        pattern_choice = input("enter your choice")
        
        if pattern_choice == "1":
            rows = int(input("Enter the number of rows: "))

            if rows <= 0:
                print("Invalid row count! row count must be positive.")
                break

            print("\nRight-angled Triangle:")

            for i in range(1, rows + 1):
                for j in range(1, i + 1):
                    print("*", end=" ")
                print()

        elif pattern_choice == "2":
            continue

        else:
            print("Invalid choice")
            pass

    # Number Analysis
    elif choice == "2":
        print("\nNumber Analysis")

        start = int(input("Enter the start number: "))
        end = int(input("Enter the end number: "))

        if end <= start:
            print("Invalid range! End number must be greater than start number.")
            continue

        total = 0

        print("\nNumber Analysis:")

        for number in range(start, end + 1):

            if number == 0:
                continue

            if number % 2 == 0:
                print(number, "is Even")
            else:
                print(number, "is Odd")

            total = total + number

        print("\nSum of all numbers:", total)

    # Exit
    elif choice == "3":
        print("\nThank you for using the Pattern Generator and Number Analyzer!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
        continue
