class Person:
    def __init__(self, name, money, mode, healthRate):
        self.name = name
        self.money = 1000
        self.mode = "happy"
        self.healthRate = 100

    @property
    def healthRate(self):
        return self.healthRate

    @healthRate.setter
    def healthRate(self, healthRate):
        if 0 < healthRate <= 100:
            self.healthRate = healthRate
        else:
            print("error healthRate must be between 0 to 100")

    def sleep(self, hours):
        if hours == 7:
            self.mode = "happy"
        elif hours < 7:
            self.mode = "tired"
        elif hours > 7:
            self.mode = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def buy(self, items):
        self.money -= (items*10)


class Employee(Person):
    def __init__(self, name,  money, mode, healthRate, id, car, email, salary, distanceToWalk):
        super(Employee, self).__init__(name, money, mode, healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary

    @property
    def salary(self):
        return self.salary

    @salary.setter
    def salary(self, salary):
        if salary >= 1000:
            self.salary = salary
        else:
            print("salary must be 1000 or more")

    def work(self, hours):
        if hours == 8:
            self.mode = "happy"
        elif hours > 8:
            self.mode = "tired"
        elif hours < 8:
            self.mode = "lazy"

    def drive(self, distanceToWalk):
        pass
        # Car.velocity = distanceToWalk/1
        # Car.run(distanceToWalk)

    def refuel(self):
        pass

    def send_mail(self):
        pass


class Office:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def get_all_employees(self):
        pass

    def get_employee(self):
        pass

    def hire(self):
        pass

    def fire(self):
        pass

    def calculate_lateness(self):
        pass

    def deduct(self):
        pass

    def reward(self):
        pass


class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    def run(self):
        pass

    def stop(self):
        pass


#emp1 = Employee(name,  money, mode, healthRate, id, car, email, salary, distanceToWalk)
emp1 = Employee("ahmad", 200, "happy", 50, 1, "fiat", "hgggfgh", 900, 55)
emp1.buy(2)
print(emp1.money)
emp1.work(9)
print(emp1.mode)
emp1.eat(3)
print(emp1.healthRate)
