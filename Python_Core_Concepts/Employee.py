class Employee:

    company = "Uber Inc" # class attribute
    pay_rate = 45.5
    amount_of_employees = 0

    def __init__(self,name,position,id_number,hours_worked):
        self.name = name
        self.position = position
        self.id_number = id_number
        self.hours_worked = hours_worked

    def get_salary(self):
        return "{} bi-weekly salary is ${}".format(self.name,self.hours_worked * Employee.pay_rate)

    def get_employee_informations(self):
        return "Name : {}\nPosition : {}\nID number : {}\nHours Worked : {}\n".format(self.name, self.position, self.id_number, self.hours_worked)

    def total_amount_of_employees():
