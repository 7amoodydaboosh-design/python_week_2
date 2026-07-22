from ticket import create_ticket
from display import display_ticket


def main():
    student_name, student_id, issue, location, priority = create_ticket()

    if priority.lower() == "high":
        technician = "Ahmed"
    elif priority.lower() == "medium":
        technician = "Siti"
    else:
        technician = "Ali"

    display_ticket(
        student_name,
        student_id,
        issue,
        location,
        priority,
        technician
    )


if __name__ == "__main__":
    main()