def get_employee():
    print("=== Employee Information ===")

    name = input("Employee Name: ")
    employee_id = input("Employee ID: ")
    basic_salary = float(input("Basic Salary (RM): "))
    allowance = float(input("Allowance (RM): "))

    return name, employee_id, basic_salary, allowance