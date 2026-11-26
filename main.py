
from abc import ABC, abstractmethod


# Employee Interface
class EmployeeInterface(ABC):

    @abstractmethod
    def add_employee(
        self,
        employee_id: int,
        name: str,
        age: int,
        position: str
    ) -> bool:
        pass


# Admin Class
class Admin(EmployeeInterface):

    def add_employee(
        self,
        employee_id: int,
        name: str,
        age: int,
        position: str
    ) -> bool:

        if employee_id <= 0 or not name or age <= 0 or not position:
            return False

        print("\nAdmin Added Employee")
        print(f"Employee ID: {employee_id}")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Position: {position}")

        return True


# Manager Class
class Manager(EmployeeInterface):

    def add_employee(
        self,
        employee_id: int,
        name: str,
        age: int,
        position: str
    ) -> bool:

        if employee_id <= 0 or not name or age <= 0 or not position:
            return False

        print("\nManager Added Employee")
        print(f"Employee ID: {employee_id}")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Position: {position}")

        return True


# Create Objects
admin = Admin()
manager = Manager()


# Call Methods
print(admin.add_employee(101, "Ahmed", 23, "Developer"))

print(manager.add_employee(102, "Rahim", 25, "Designer"))
