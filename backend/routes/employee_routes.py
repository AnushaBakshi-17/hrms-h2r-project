from flask import Blueprint, render_template, request, redirect
from models.employee import add_employee, get_all_employees, delete_employee

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/')
def home():
    return render_template("index.html")

@employee_bp.route('/add', methods=['GET', 'POST'])
def add_emp():
    if request.method == 'POST':
        name = request.form['name']
        role = request.form['role']
        salary = request.form['salary']

        if not name or not role or not salary:
            return "⚠️ All fields are required!"

        add_employee(name, role, salary)
        return redirect('/view')

    return render_template("add_employee.html")

@employee_bp.route('/view')
def view_emp():
    employees = get_all_employees()
    return render_template("view_employee.html", employees=employees)

@employee_bp.route('/payroll')
def payroll():
    employees = get_all_employees()
    return render_template("payroll.html", employees=employees)

@employee_bp.route('/retire/<int:id>')
def retire(id):
    delete_employee(id)
    return redirect('/view')