#Мог неверно понять подсказку, но кажется подсказка в задании должна быть с точностью до наоборот
#Метод get_hours() должен вернуть cls: return cls(name, hours, rest_days, email). Метод get_email — аналогично. Методу set_hourly_payment() ничего возвращать не нужно, потому что он только меняет значение переменной.
# метод set_hourly_payment как раз воздействует на переменную класса, принемую ко всем объектам, поэтому должен быть cls

class EmployeeSalary:
    hourly_payment = 400
    def __init__(self,name,hours,rest_days,email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    
    def get_hours(self):
        if self.hours is None:
            return (7 - self.rest_days) * 8
        else:
            return self.hours
    
    def get_email(self):
        if self.email is None:
            return f"{self.name}@email.com"
        else:
            return self.email
            

    @classmethod
    def set_hourly_payment(cls,new_hourly_payment):
        cls.hourly_payment = new_hourly_payment

    def salary(self):
        return self.get_hours()* self.hourly_payment
    
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