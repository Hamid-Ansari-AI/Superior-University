import csv
from manager import Manager
from worker import Worker

class FileHandler:
    @staticmethod
    def save_employees(employees):
        with open("employees.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Age", "Salary", "Department", "Hours Worked"])
            for employee in employees:
                if isinstance(employee, Manager):
                    writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(), employee.get_department(), ""])
                elif isinstance(employee, Worker):
                    writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(), "", employee.get_hours_worked()])

    @staticmethod
    def load_employees(filename):
        employees = []
        try:
            with open(filename, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Department"]:
                        employees.append(Manager(row["Name"], int(row["Age"]), int(row["Salary"]), row["Department"]))
                    elif row["Hours Worked"]:
                        employees.append(Worker(row["Name"], int(row["Age"]), int(row["Salary"]), int(row["Hours Worked"])))
                    
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with new employee.")
        return employees

    @staticmethod
    def add_employee(employees):
        employee_type = input("Enter employee type (manager/worker): ").strip().lower()
        name = input("Enter name:").title()
        age = int(input("Enter age:"))
        salary = int(input("Enter salary:"))
        if employee_type == "manager":
            department = input("Enter department:").upper()
            employees.append(Manager(name, age, salary, department))
        elif employee_type == "worker":
            hours_worked = int(input("Enter hours worked:"))
            employees.append(Worker(name, age, salary, hours_worked))

    @staticmethod
    def display_employees(employees):
        for employee in employees:
            employee.display_info()
            print('-' * 20)
    
    @staticmethod
    def update_employee(employees):
        name = input("\nEnter the name of the employee to update:").lower()
        for emp in employees:
            if emp.get_name().lower() == name:
                if isinstance(emp, Manager):
                    emp.set_name(input("Enter new name:").title())
                    emp.set_age(int(input("Enter new age:")))
                    emp.set_salary(int(input("Enter new salary:")))
                    emp.set_department(input("Enter new department:").upper())
                elif isinstance(emp, Worker):
                    emp.set_name(input("Enter new name:").title())
                    emp.set_age(int(input("Enter new age:")))
                    emp.set_salary(int(input("Enter new salary:")))
                    emp.set_hours_worked(int(input("Enter new hours worked:")))
                print("Employee updated successfully!")
                return
        print("Employee not found!")

    @staticmethod
    def delete_employee(employees):
        name = input("\nEnter the name of the employee to delete: ").lower()
        for emp in employees:
            if emp.get_name().lower() == name:
                employees.remove(emp)
                print(f"Employee: {emp.get_name()} deleted successfully!")
                return
        print("Employee not found!")
