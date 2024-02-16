import json

class Employee:
    def __init__(self, employee_name, employee_id, title, department):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.title = title
        self.department = department

    def display_details(self):
        print(f"Employee_Name: {self.employee_name}\nID: {self.employee_id}\nTitle: {self.title}\nDepartment: {self.department}")

    def __str__(self):
        return f"{self.employee_name}-{self.employee_id}"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
        else:
            print("Employee already exist, please enter a different employee")

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            print("Employee doesn't exist, please enter a different employee")

    def list_employees(self):
        print(f"Employees in {self.name} department:")
        for employee in self.employees:
            print(employee)

class Company:
    def __init__(self):
        self.departments = {}

    def add_department(self, department):
        self.departments[department.name] = department

    def remove_department(self, department_name):
        if department_name in self.departments:
            del self.departments[department_name]

    def display_departments(self):
        print("Departments Name:- ")
        for department_name in self.departments:
            print(department_name)

def save_data(company):
    with open('company_data.json', 'w') as file:
        data = {'departments': {}}
        for department_name, department in company.departments.items():
            data['departments'][department_name] = {'employees': [str(emp) for emp in department.employees]}
        json.dump(data, file)

def load_data():
    try:
        with open('company_data.json', 'r') as file:
            data = json.load(file)
            company = Company()
            for department_name, department_data in data['departments'].items():
                department = Department(department_name)
                for employee_str in department_data['employees']:
                    name, employee_id = employee_str.split('-')
                    employee = Employee(name, employee_id, '', department_name)
                    department.add_employee(employee)
                company.add_department(department)
            return company
    except FileNotFoundError:
        return Company()

def main_menu():
    company = load_data()

    while True:
        print("\nEmployee Management System Menu:")
        print("1. Add Department")
        print("2. Remove Department")
        print("3. Display Departments")
        print("4. Add Employee")
        print("5. Remove Employee")
        print("6. List Employees in Department")
        print("7. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            department_name = input("Enter department name: ")
            department = Department(department_name)
            company.add_department(department)
            print(f"Department '{department_name}' has been added.")

        elif choice == '2':
            department_name = input("Enter department name to remove: ")
            company.remove_department(department_name)
            print(f"Department '{department_name}' has been removed.")

        elif choice == '3':
            company.display_departments()

        elif choice == '4':
            department_name = input("Enter department name: ")
            if department_name in company.departments:
                name = input("Enter employee name: ")
                employee_id = int(input("Enter employee ID: "))
                employee = Employee(name, employee_id, '', department_name)
                company.departments[department_name].add_employee(employee)
                print("Employee has been added.")
            else:
                print(f"Department '{department_name}' does not exist.")

        elif choice == '5':
            department_name = input("Enter department name: ")
            if department_name in company.departments:
                employee_id = int(input("Enter employee ID to remove: "))
                for employee in company.departments[department_name].employees:
                    if employee.employee_id == employee_id:
                        company.departments[department_name].remove_employee(employee)
                        print("Employee has been removed.")
                        break
                else:
                    print(f"Employee with ID {employee_id} not found in department '{department_name}'.")
            else:
                print(f"Department '{department_name}' does not exist.")

        elif choice == '6':
            department_name = input("Enter department name: ")
            if department_name in company.departments:
                company.departments[department_name].list_employees()
            else:
                print(f"Department '{department_name}' does not exist.")

        elif choice == '7':
            save_data(company)
            print("Data saved. Exiting.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main_menu()
