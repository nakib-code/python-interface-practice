
class Employee:
    role = "Employee"

    def __init__(self, name, salary, employee_id=None):
        self.id = employee_id
        self.name = name
        self.salary = float(salary)

    def format_salary(self):
        return f"${self.salary:,.2f}"

    def show_details(self):
        return f"{self.role}: {self.name} | Salary: {self.format_salary()}"


class Manager(Employee):
    role = "Manager"

    # Method Overriding
    def show_details(self):
        base_details = super().show_details()
        return f"{base_details} | Leads team and oversees projects"


class Developer(Employee):
    role = "Developer"

    # Method Overriding
    def show_details(self):
        base_details = super().show_details()
        return f"{base_details} | Designs, writes, and maintains code"


# Mapping of roles to their corresponding child classes
ROLE_CLASSES = {
    "Manager": Manager,
    "Developer": Developer,
}


def create_employee(name, salary, role, employee_id=None):
    employee_class = ROLE_CLASSES.get(role)

    if employee_class is None:
        raise ValueError(f"Unsupported role: {role}")

    return employee_class(name=name, salary=salary, employee_id=employee_id)
