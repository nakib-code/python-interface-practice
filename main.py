
import math
import os
from flask import Flask, flash, redirect, render_template, request, url_for

from database import (
    add_employee_record,
    delete_employee_record,
    get_all_employees,
    init_db,
)
from models import Developer, Manager, ROLE_CLASSES, create_employee

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-key-change-me")

# Ensure the SQLite table exists when the app starts
init_db()


@app.route("/")
def index():
    employees = get_all_employees()
    manager_count = sum(1 for emp in employees if isinstance(emp, Manager))
    developer_count = sum(1 for emp in employees if isinstance(emp, Developer))

    return render_template(
        "index.html",
        employees=employees,
        total_count=len(employees),
        manager_count=manager_count,
        developer_count=developer_count,
    )


@app.route("/add", methods=["GET", "POST"])
def add_employee():
    form_data = {"name": "", "salary": "", "role": "Developer"}

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        salary_raw = request.form.get("salary", "").strip()
        role = request.form.get("role", "").strip()
        form_data = {"name": name, "salary": salary_raw, "role": role}

        errors = []

        if not name:
            errors.append("Employee name is required.")

        if role not in ROLE_CLASSES:
            errors.append("Please select a valid role (Manager or Developer).")

        salary = None
        if not salary_raw:
            errors.append("Salary is required.")
        else:
            try:
                salary = float(salary_raw)
                if not math.isfinite(salary) or salary <= 0:
                    errors.append("Salary must be greater than zero.")
            except ValueError:
                errors.append("Salary must be a valid number.")

        if errors:
            for error in errors:
                flash(error, "error")
            return render_template("add_employee.html", form_data=form_data)

        # Create a Manager or Developer object and save it
        new_employee = create_employee(name=name, salary=salary, role=role)
        add_employee_record(new_employee)

        flash(f"Added {new_employee.role} '{new_employee.name}' successfully.", "success")
        return redirect(url_for("index"))

    return render_template("add_employee.html", form_data=form_data)


@app.route("/delete/<int:employee_id>", methods=["POST"])
def delete_employee(employee_id):
    deleted = delete_employee_record(employee_id)
    if deleted:
        flash("Employee deleted successfully.", "success")
    else:
        flash("Employee not found.", "error")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
