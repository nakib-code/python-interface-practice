
from contextlib import closing
import os
import sqlite3

from models import create_employee

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "employees.db")


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with closing(get_connection()) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                salary REAL NOT NULL,
                role TEXT NOT NULL
            )
            """
        )
        connection.commit()


def add_employee_record(employee):
    with closing(get_connection()) as connection:
        cursor = connection.execute(
            "INSERT INTO employees (name, salary, role) VALUES (?, ?, ?)",
            (employee.name, employee.salary, employee.role),
        )
        connection.commit()
        employee.id = cursor.lastrowid
    return employee


def get_all_employees():
    with closing(get_connection()) as connection:
        rows = connection.execute(
            "SELECT id, name, salary, role FROM employees ORDER BY id DESC"
        ).fetchall()

    employees = []
    for row in rows:
        # Create the matching Manager or Developer object
        employee = create_employee(
            name=row["name"],
            salary=row["salary"],
            role=row["role"],
            employee_id=row["id"],
        )
        employees.append(employee)
    return employees


def delete_employee_record(employee_id):
    with closing(get_connection()) as connection:
        cursor = connection.execute(
            "DELETE FROM employees WHERE id = ?",
            (employee_id,),
        )
        connection.commit()
        return cursor.rowcount > 0
