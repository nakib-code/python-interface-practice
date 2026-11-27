# Employee Management System

A small Python project demonstrating **Interfaces** and **OOP concepts** using an Employee Management System.

## Project Structure

```text
python/
├── interfaces.py   # EmployeeInterface (ABC)
├── employee.py     # Admin and Manager classes
├── main.py         # Demo script
└── README.md       # Project explanation
```

## OOP Concepts Demonstrated

- **Abstraction:** `EmployeeInterface` uses `ABC` and `@abstractmethod` to define `add_employee()` and `delete_employee()`.
- **Inheritance:** `Admin` and `Manager` both inherit from `EmployeeInterface`.
- **Method Overriding:** `Admin` allows deleting employees, while `Manager` denies deletion.
- **Polymorphism:** `delete_with_role(role: EmployeeInterface, employee_id: int)` works with any `EmployeeInterface` object (`Admin` or `Manager`).

## How to Run

```bash
python3 main.py
```

## Example Output

```text
Admin added employee: Ahmed (ID: 101)
Manager added employee: Hasan (ID: 102)
Manager failed to add employee: ID 101 already exists.
Admin failed to add employee: invalid data.
Permission denied: Manager cannot delete employee ID 102.
Deleted: False
Admin deleted employee ID: 102
Deleted: True
```

## Author

**Ahmed Nakib**
