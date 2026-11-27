from __future__ import annotations

from abc import ABC, abstractmethod


class EmployeeInterface(ABC):
    "Abstract interface defining employee management operations."

    @abstractmethod
    def add_employee(
        self, employee_id: int, name: str, age: int, position: str
    ) -> bool:
        "Add an employee record and return True if successful."

    @abstractmethod
    def delete_employee(self, employee_id: int) -> bool:
        "Delete an employee record by ID and return True if successful."
