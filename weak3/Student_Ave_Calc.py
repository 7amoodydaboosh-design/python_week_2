def main():
    while True:
        print("\n--- Student Grade Calculator ---")
        
        # 1. Ask the user to enter three quiz marks
        try:
            quiz1 = float(input("Enter marks for Quiz 1: "))
            quiz2 = float(input("Enter marks for Quiz 2: "))
            quiz3 = float(input("Enter marks for Quiz 3: "))
        except ValueError:
            print("Invalid input! Please enter numeric values for marks.")
            continue

        # 2. Calculate the average mark
        average = (quiz1 + quiz2 + quiz3) / 3

        # 3. Display the average
        print(f"The average mark is: {average:.2f}")

        # 4. Determine whether the student passes or fails (Assuming 50 is passing)
        if average >= 50:
            print("Result: Pass")
        else:
            print("Result: Fail")

        # 5. Allow another student's marks to be entered
        another = input("\nDo you want to enter marks for another student? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Exiting program. Goodbye!")
            break

if __name__ == "__main__":
    main()