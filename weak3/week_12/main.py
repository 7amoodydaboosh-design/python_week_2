def check_computers():
    computers = []  # initial value

    # iterate & check for 5 computers
    for i in range(5):
        # prompt the user to classify each computer
        # A - Available, U - Used, M - Maintenance
        status = input(f"Computer {i + 1} Status (A/U/M): ")

        computers.append(status)

    return computers


def count_available(computers):
    available = 0  # initial value

    for status in computers:
        if status == "A":
            available += 1

    return available


def display_status(computers, available):
    print("\n========== LAB STATUS ==========")

    for number in range(5):
        print(
            f"Computer {number + 1}: {computers[number]}"
        )

    print("--------------------------------")
    print(f"Available Computers: {available}")
    print("================================")


# Main program
while True:
    computers = check_computers()

    available = count_available(computers)

    display_status(computers, available)

    again = input("\nPerform another monitoring cycle? (Y/N): ")

    if again.upper() != "Y":
        break