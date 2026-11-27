from employee import Admin, Manager
from interfaces import EmployeeInterface


def delete_with_role(role: EmployeeInterface, employee_id: int) -> None:
    result = role.delete_employee(employee_id)
    print("Deleted:", result)


def main() -> None:
    employees: dict = {}
    admin = Admin(employees)
    manager = Manager(employees)

    admin.add_employee(101, "Ahmed", 23, "Developer")
    manager.add_employee(102, "Hasan", 28, "Engineer")
    manager.add_employee(101, "Karim", 30, "Tester")
    admin.add_employee(0, "Invalid", 25, "QA")

    for role in (manager, admin):
        delete_with_role(role, 102)


if __name__ == "__main__":
    main()
