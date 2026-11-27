from __future__ import annotations

from typing import Dict, Union

from interfaces import EmployeeInterface

EmployeeStore = Dict[int, Dict[str, Union[int, str]]]


def _is_positive_int(value: object) -> bool:
    "Return True if value is a positive integer (excluding bool)."
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def _add_employee_record(
    employees: EmployeeStore,
    role_name: str,
    employee_id: int,
    name: str,
    age: int,
    position: str,
) -> bool:
    "Validate and add an employee into the shared employee dictionary."
    if (
        not _is_positive_int(employee_id)
        or not isinstance(name, str)
        or not name.strip()
        or not _is_positive_int(age)
        or not isinstance(position, str)
        or not position.strip()
    ):
        print(f"{role_name} failed to add employee: invalid data.")
        return False

    if employee_id in employees:
        print(f"{role_name} failed to add employee: ID {employee_id} already exists.")
        return False

    clean_name = name.strip()
    clean_position = position.strip()

    employees[employee_id] = {
        "name": clean_name,
        "age": age,
        "position": clean_position,
    }
    print(f"{role_name} added employee: {clean_name} (ID: {employee_id})")
    return True


class Admin(EmployeeInterface):
    """Admin role with permission to add and delete employees."""

    def __init__(self, employees: EmployeeStore) -> None:
        self.employees = employees

    def add_employee(
        self, employee_id: int, name: str, age: int, position: str
    ) -> bool:
        return _add_employee_record(
            self.employees, "Admin", employee_id, name, age, position
        )

    def delete_employee(self, employee_id: int) -> bool:
        if not _is_positive_int(employee_id) or employee_id not in self.employees:
            print(f"Admin failed to delete: employee ID {employee_id} not found.")
            return False

        del self.employees[employee_id]
        print(f"Admin deleted employee ID: {employee_id}")
        return True


class Manager(EmployeeInterface):
    "Manager role with permission to add employees, but not delete them."

    def __init__(self, employees: EmployeeStore) -> None:
        self.employees = employees

    def add_employee(
        self, employee_id: int, name: str, age: int, position: str
    ) -> bool:
        return _add_employee_record(
            self.employees, "Manager", employee_id, name, age, position
        )

    def delete_employee(self, employee_id: int) -> bool:
        print(
            f"Permission denied: Manager cannot delete employee ID {employee_id}."
        )
        return False
