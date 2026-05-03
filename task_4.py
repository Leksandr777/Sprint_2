class EmployeeSalary:
    hourly_payment = 400
    default_domain = "email.com"  

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def calculate_hours(cls, rest_days):
        return (7 - rest_days) * 8

    @classmethod
    def generate_email(cls, name):
        return f"{name}@{cls.default_domain}"

    def get_hours(self):
        if self.hours is None:
            return self.calculate_hours(self.rest_days)
        return self.hours

    def get_email(self):
        if self.email is None:
            return self.generate_email(self.name)
        return self.email

    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment

    def salary(self):
        return self.get_hours() * self.hourly_payment


employee = EmployeeSalary(
    name="Ivanov",
    hours=None,
    rest_days=2,
    email=None
)

print(f"Имя: {employee.name}")
print(f"Часы: {employee.get_hours()}")
print(f"Email: {employee.get_email()}") 
print(f"Зарплата: {employee.salary()} руб.")


