class Employee:
    # if im right this is the only function should remain, i hope i did not get fooled
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    # This violates the Single Responsibilty Principle (SRP) this should be in seperate classes
    # def calculate_annual_salary(self):
    #     return self.salary * 12
    
    # def generate_payslip(self):
    #     payslip = f"Payslip for {self.name}\nAnnual Salary: ${self.calculate_annual_salary()}"
    #     return payslip

    # def save_to_database(self):
    #     print(f"Saving {self.name}'s data to the database...")

    # def send_email(self, message):
    #     print(f"Sending email to {self.name}: {message}")

class CalcSalary:
    @staticmethod
    def calculate_annual_salary(employee):
        return employee.salary * 12

# Here i seperate the methods/function into GeneratePayslip, SaveData, SendEmail classes
class GeneratePayslip:

    # i used static method to access the attributes and function globaly in the class Employee
    @staticmethod
    def generate_payslip(employee):
        payslip = f"Payslip for {employee.name}\nAnnual Salary: ${CalcSalary.calculate_annual_salary(employee)}"
        return payslip
    
class SaveData:
    @staticmethod
    def save_to_database(employee):
        print(f"Saving {employee.name}'s data to the database...")
    
class SendEmail:
    def send_email(message):
        print(f"Sending email to {employee.name}: {message}")

# Test the refactored code
employee = Employee(101, "Alice", 5000)
print(GeneratePayslip.generate_payslip(employee))
SaveData.save_to_database(employee)
SendEmail.send_email("Your salary has been processed.")
