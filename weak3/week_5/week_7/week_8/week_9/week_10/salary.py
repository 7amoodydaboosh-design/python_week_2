def calculate_gross_salary(basic_salary, allowance):
    return basic_salary + allowance


def calculate_epf(gross_salary):
    return gross_salary * 0.11


def calculate_socso(gross_salary):
    return gross_salary * 0.005


def calculate_net_salary(gross_salary, epf, socso):
    return gross_salary - epf - socso