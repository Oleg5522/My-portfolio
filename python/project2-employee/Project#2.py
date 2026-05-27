# Project 2
import datetime

class Employee:
    """Represents a single employee in the management system."""
    
    # Constructor
    def __init__(self, name: str, job_title: str, department: str, salary: float, hire_year: int):
        """Initialize employee with name, job title, department, salary, and hire year."""
        self.name = name
        self.job_title = job_title
        self.department = department
        self.salary = salary
        self.hire_year = hire_year

    # String representation
    def __str__(self):
        """Return a string representation of the employee."""
        return (f'Employee name: {self.name}\n'
                f'Job title: {self.job_title}\n'
                f'Department: {self.department}\n'
                f'Salary: ${self.salary:.2f}\n'
                f'Hire year: {self.hire_year}')

    # Total years employee has worked here, based on the hire year
    def years_worked(self) -> int:
        """Return the total years this employee has worked here, based on hire year."""
        current_year = datetime.datetime.now().year
        return current_year - self.hire_year

    # Calculate the total salary expense: salary * years worked
    def total_expense(self) -> float:
        """Calculate total salary expense: salary multiplied by years worked."""
        return self.salary * self.years_worked()

    # Write employee information to a text file
    def write_employees(self):
        """Write employee information to a text file."""
        f = open('list_employees.txt', 'w')
        f.write(f'Employee name: {self.name}\n'
                f'Job title: {self.job_title}\n'
                f'Department: {self.department}\n'
                f'Hire year: {self.hire_year}\n'
                f'Monthly salary: ${self.salary:.2f}\n'
                f'Total expense: ${self.total_expense():.2f}')
        f.close()

    # Mutator methods
    def set_name(self, other: str):
        """Set employee name."""
        self.name = other

    def set_job_title(self, other: str):
        """Set job title."""
        self.job_title = other

    def set_department(self, other: str):
        """Set department."""
        self.department = other

    def set_salary(self, other: float):
        """Set salary."""
        self.salary = other

    def set_hire_year(self, other: int):
        """Set hire year."""
        self.hire_year = other

    # Accessor methods
    def get_name(self) -> str:
        """Return employee name."""
        return self.name

    def get_job_title(self) -> str:
        """Return job title."""
        return self.job_title

    def get_department(self) -> str:
        """Return department."""
        return self.department

    def get_salary(self) -> float:
        """Return salary."""
        return self.salary

    def get_hire_year(self) -> int:
        """Return hire year."""
        return self.hire_year


Emp1 = Employee('Ivanov', 'CEO', 'Administration', 10000, 2010)
Emp2 = Employee('Sidorov', 'CFO', 'Accounting', 3500, 2013)
Emp3 = Employee('Petrov', 'CTO', 'Engineering', 2500, 2011)

print(Emp1)
print(f'\nYears worked: {Emp1.years_worked()}')
print(f'Total expense: ${Emp1.total_expense():.2f}')
Emp1.write_employees()