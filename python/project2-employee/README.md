# Employee Management System

A Python project demonstrating object-oriented programming with a class that models an employee.

## What it does

- Defines an `Employee` class with attributes: name, job title, department, salary, and hire year
- Calculates how many years an employee has worked at the company
- Calculates the total salary expense for an employee over their time at the company
- Writes employee data to a text file
- Includes getter and setter methods for all attributes

## Technologies

- Python 3
- `datetime` module
- Object-oriented programming (OOP)

## How to run

```bash
python Project_2.py
```

Sample employees are created at the bottom of the file. You can modify or add new ones:

```python
Emp1 = Employee('Smith', 'CEO', 'Administration', 10000, 2010)
print(Emp1)
print(f'Years worked: {Emp1.years_worked()}')
print(f'Total expense: ${Emp1.total_expense():.2f}')
```

## Notes

This is a course project completed as part of a Python fundamentals course focused on OOP concepts.