myEmployees = {}

def add_employee():
    employee_id = input("Enter employee id: ")

    if employee_id not in myEmployees:
        print("Employee already exists")
        return
    employee_name = input("Enter employee name: ")
    basic_pay = float(input("Enter basic pay: "))
    allowance = float(input("Enter allowance: "))
    deductions = float(input("Enter deductions: "))
    taxes = float(input("Enter taxes: "))

    gross_pay = basic_pay + allowance
    net_pay = gross_pay - deductions - taxes

    myEmployees[employee_id] = {
        "employee_name": employee_name,
        "basic_pay": basic_pay,
        "allowance": allowance,
        "deductions": deductions,
        "taxes": taxes,
        "gross_pay": gross_pay,
        "net_pay": net_pay
    }
    print("Employee added Successfully")

def delete_employee():
    employee_id = input("Enter employee id to delete: ")

    if employee_id in myEmployees:
        del myEmployees[employee_id]
        print("Employee deleted Successfully")
    else:
        print("Employee not found")

def modify_employee():
    employee_id = input("Enter employee id to modify: ")

    if employee_id not in myEmployees:
        print("Employee not found")
        return
    employee_name = input("Enter employee name: ")
    basic_pay = float(input("Enter basic pay: "))
    allowance = float(input("Enter allowance: "))
    deductions = float(input("Enter deductions: "))
    taxes = float(input("Enter taxes: "))

    gross_pay = basic_pay + allowance
    net_pay = gross_pay - deductions - taxes

    myEmployees[employee_id] = {"employee_name": employee_name,
                                "basic_pay": basic_pay,
                                "allowance": allowance,
                                "deductions": deductions,
                                "taxes": taxes,
                                "gross_pay": gross_pay,
                                "net_pay": net_pay
                                }
    print("Employee modified Successfully")

def display_all_employees():
    if not myEmployees:
        print("employees not found")
        return
    for employee_id, employee in myEmployees.items():
        print("\n======================")
        print("Employee ID: ", employee_id)
        print("Employee Name: ", employee["employee_name"])
        print("Basic Pay: ", employee["basic_pay"])
        print("Allowance: ", employee["allowance"])
        print("Deductions: ", employee["deductions"])
        print("Taxes: ", employee["taxes"])
        print("gross_pay:", employee["gross Pay"])
        print("Net Pay: ", employee["net Pay"])
        print("=====================")

while True:
    print("\n==== EMPLOYEE PAYROLL MENU =====")
    print("1. Add employee")
    print("2. Delete employee")
    print("3. Modify employee")
    print("4. Display all employees")
    print("5. Exit")

    choice = int(input("Enter: "))
    if choice == 1:
        add_employee()

    elif choice == 2:
            delete_employee()

    elif choice == 3:
            modify_employee()

    elif choice == 4:
             display_all_employees()

    elif choice == 5:
            print("exiting the program...")
            break

    else:
            print("invalid choice. Please enter a number from 1 to 5")






