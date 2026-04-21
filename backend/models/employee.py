from database.db import get_db_connection

def add_employee(name, role, salary):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO employees (name, role, salary) VALUES (?, ?, ?)",
        (name, role, salary)
    )
    conn.commit()
    conn.close()

def get_all_employees():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    employees = cur.fetchall()
    conn.close()
    return employees

def delete_employee(emp_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM employees WHERE id=?", (emp_id,))
    conn.commit()
    conn.close()