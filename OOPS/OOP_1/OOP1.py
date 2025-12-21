# FIRST TASK

class BankAccount:
    def __init__(self, name, balance, account_number):
        self.name = name                  # public
        self._balance = balance           # protected
        self.__account_number = account_number  # private

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount

    def get_balance(self):
        return self._balance

    def display_info(self):
        print("Name:", self.name)
        print("Balance:", self._balance)
        print("Account number:", self.__account_number)


class SavingAccount(BankAccount):
    def __init__(self, name, balance, account_number, interest_rate):
        super().__init__(name, balance, account_number)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self._balance = self._balance + (self._balance * self.interest_rate)
"""------------------------------------------------------------------------------"""

# SECOND TASK
from abc import ABC, abstractmethod

# ABSTRACT CLASS 1
class Person(ABC):
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number

    @abstractmethod
    def get_role(self):
        pass


# ABSTRACT CLASS 2
class Payable(ABC):
    @abstractmethod
    def calculate_payment(self):
        pass


# CONCRETE CLASS 1
class Doctor(Person, Payable):  # multiple inheritance
    def __init__(self, name, age, id_number, specialty, salary, experience):
        super().__init__(name, age, id_number)
        self.specialty = specialty
        self.salary = salary
        self.experience = experience

    def get_role(self):
        return "Doctor"

    def calculate_payment(self):
        return self.salary

    def diagnose(self):
        return "Diagnosing patient"


# CONCRETE CLASS 2
class Nurse(Person, Payable):
    def __init__(self, name, age, id_number, shift, salary, department):
        super().__init__(name, age, id_number)
        self.shift = shift
        self.salary = salary
        self.department = department

    def get_role(self):
        return "Nurse"

    def calculate_payment(self):
        return self.salary

    def assist(self):
        return "Assisting doctor"


# CONCRETE CLASS 3
class Patient(Person):
    def __init__(self, name, age, id_number, illness, room, insured):
        super().__init__(name, age, id_number)
        self.illness = illness
        self.room = room
        self.insured = insured

    def get_role(self):
        return "Patient"

    def get_status(self):
        return self.illness


# CONCRETE CLASS 4
class Hospital:
    def __init__(self, name, address, capacity):
        self.name = name
        self.address = address
        self.capacity = capacity

    def open(self):
        return "Hospital opened"

    def close(self):
        return "Hospital closed"


# CONCRETE CLASS 5
class Appointment:
    def __init__(self, doctor, patient, time):
        self.doctor = doctor
        self.patient = patient
        self.time = time

    def schedule(self):
        return "Appointment scheduled"

    def cancel(self):
        return "Appointment canceled"


# CONCRETE CLASS 6
class Pharmacy:
    def __init__(self, name, location, medicines):
        self.name = name
        self.location = location
        self.medicines = medicines

    def sell(self):
        return "Medicine sold"

    def restock(self):
        return "Medicines restocked"
"""------------------------------------------------------------------------------"""

# THIRD TASK
import math

class Vector2D:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def add2(self, other):
        self.x += other.x
        self.y += other.y

    def sub(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def sub2(self, other):
        self.x -= other.x
        self.y -= other.y

    def mult(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def mult2(self, scalar):
        self.x *= scalar
        self.y *= scalar

    def __str__(self):
        return f"({self.x}, {self.y})"

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def scalar_product(self, other):
        return self.x * other.x + self.y * other.y

    def cos(self, other):
        return self.scalar_product(other) / (self.length() * other.length())

    def equals(self, other):
        return self.x == other.x and self.y == other.y

    # operator overloading
    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.sub(other)

    def __mul__(self, scalar):
        return self.mult(scalar)

    def __eq__(self, other):
        return self.equals(other)

