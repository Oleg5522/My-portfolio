# Project 2
from datetime import datetime
import datetime

class Employee:
    #Constructor
    def __init__(self, name: str, job_title: str, department: str, salary: float, hire_year: str):
         self.name = name
         self.job_title = job_title
         self.department = department
         self.salary = salary
         self.hire_year = hire_year 

    #String representation         
    def __str__(self):
       return f'Employee name: {self.name}\nJob_title: {self.job_title}\nDepartment: {self.department}\nSalary: ${self.salary:.02f}\nEmployment date: {self.hire_year} '
        
    #Total days employee has worked here, based on the hire year
    def years_worked(self):
        hire_date = datetime.datetime.strptime(self.hire_year, '%m-%d-%Y')
        today = datetime.datetime.now()
        work_period = today - hire_date
        return f'Employee name: {self.name}\nWas hired: {work_period.days} days ago\nWorks at the company for: {int(work_period.days/365)}year(s)'
       
    #Calculate the total salary expense for the employee, which is the salary multiplied by the days worked 
    def total_expenses(self):
        hire_date = datetime.datetime.strptime(self.hire_year, '%m-%d-%Y')
        today = datetime.datetime.now()
        work_period = today - hire_date
        return f'Employee name: {self.name}\nEarned for the entire period of work at the enterprise: ${((self.salary/30.5) * work_period.days):.02f} '
    
    #Write  employee information to a text file.
    def write_employees(self):
        f = open('list_employees.txt', 'w')
        f.write(f'Employee name: {self.name}\nJob_title: {self.job_title}\nDepartment: {self.department}\nDate of hire: {self.hire_year}\nMonthly salary: ${self.salary}\nTotal salary: {self.total_expenses()}')
        f.close()
        
    #Changing employee information        
    def set_name(self, other):
        self.name = other
        
    def set_job_title(self, other):
        self.job_title = other
        
    def set_department(self, other):
        self.department = other
        
    def set_salary(self, other):
        self.salary = other
        
    def set_hire_year(self, other):
        self.hire_year = other

    #Receiving any data on an employee    
    def get_name(self):
        return self.name
        
    def get_job_title(self):
        return self.job_title
        
    def get_department(self):
        return self.department
        
    def get_salary(self):
        return self.salary
        
    def get_hire_year(self):
        return self.hire_year
         
        
              
Emp1 = Employee('Ivanov', 'CEO', 'Administration', 10000, '01-02-2010')
Emp2 = Employee('Sidorov', 'CFO', 'Accounting', 3500, '08-07-2013')
Emp3 = Employee('Petrov', 'CTO', 'Engineering', 2500, '12-12-2011')



print(Emp1)
print(Emp1.years_worked())
Emp1.write_employees()
#print(Emp2)
#print(Emp3) 
#print(Emp1.total_expenses())
#print(Emp2.total_expenses()) 
#print(Emp3.total_expenses())
#print(Emp3.set_hire_year('2012'))
#print(Emp2.get_name())
#print(Emp2.set_name('Oleg'))
#print(Emp2)
#Emp2.set_salary(float(3700))
#Emp2.set_hire_year(2014)
#print(Emp1.years_worked())
#print(Emp2.total_expenses_short())
#print(Employee.__dict__)
#print(Emp1.__str__)
#print(Emp2.__str__)
#print(Emp3.__str__) 

#Emp1.write_employees()
#Emp2.write_employees()
#Emp3.write_employees()



