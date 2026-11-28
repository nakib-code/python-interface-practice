# Employee Management System (Python OOP Inheritance + Flask)

A simple, beginner-friendly full-stack Employee Management System built with **Python Flask**, **SQLite**, **Jinja2**, **HTML**, and **CSS**. Its main goal is to demonstrate **Inheritance in Python OOP** in a working web application.

## OOP Inheritance Concepts Demonstrated

All OOP logic lives in `models.py` and is used directly by `database.py`, `main.py`, and `templates/index.html`:

1. **Class Inheritance**: `Manager(Employee)` and `Developer(Employee)` inherit attributes (`id`, `name`, `salary`) and methods from the parent `Employee` class.
2. **Method Inheritance**: Both `Manager` and `Developer` inherit `format_salary()` directly from `Employee` without redefining it.
3. **Method Overriding**: Both `Manager` and `Developer` override `show_details()` (using `super().show_details()`) to provide role-specific descriptions displayed on the home page.

## Project Structure

```text
python/
├── main.py
├── models.py
├── database.py
├── templates/
│   ├── index.html
│   └── add_employee.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md
```

## Features

- View all employees with role summary cards (Total, Managers, Developers)
- Add a new employee (`Manager` or `Developer`) with form validation
- Delete an employee record
- Persist records in SQLite (`employees.db` is created automatically on first run)
- Clear success and error flash messages

## Installation & Run Instructions

1. Navigate to the project directory:
   ```bash
   cd /Users/macbookair/project/python
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   *(On Windows: `venv\Scripts\activate`)*

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python3 main.py
   ```

5. Open your browser and visit:
   ```text
   http://127.0.0.1:5000
   ```
