"""
=============================================================================
🧱 Python OOP (Object-Oriented Programming) Revision Sheet
Topics Covered:
  1. Class & Object
  2. Inheritance (Single, Multilevel, Multiple) & super()
  3. Polymorphism (Method Overriding)
  4. Encapsulation (Public, Protected, Private & @property)
  5. Abstraction (ABC & @abstractmethod)
=============================================================================
"""

from abc import ABC, abstractmethod


# =============================================================================
# 1. CLASS & OBJECT
# =============================================================================
# • Class : Blueprint/template for creating objects.
# • Object: An actual instance of the class in memory.
# • self  : Refers to the current instance of the class.
# • __init__: Constructor method called automatically when creating an object.

class Car:
    wheels = 4  # Class variable (shared across all instances)

    def __init__(self, brand: str, speed: int):
        self.brand = brand  # Instance variable (unique to each object)
        self.speed = speed

    def drive(self):
        return f"{self.brand} is driving at {self.speed} km/h."

# Creating objects (instances)
car1 = Car("Tesla", 120)
car2 = Car("BMW", 140)

print("[1] Class & Object:")
print(f"    {car1.drive()}")
print(f"    {car2.drive()} (Total wheels: {Car.wheels})")


# =============================================================================
# 2. INHERITANCE
# =============================================================================
# • Allows a child class to inherit attributes and methods from a parent class.
# • super(): Calls the parent class constructor or methods.

# --- 2.1 Single Inheritance (Parent -> Child) ---
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name)  # Inherit parent properties
        self.breed = breed

    def speak(self):  # Method overriding
        return f"{self.name} ({self.breed}) barks!"

d = Dog("Buddy", "Golden Retriever")
print("\n[2.1] Single Inheritance:")
print(f"      {d.speak()}")


# --- 2.2 Multilevel Inheritance (Grandparent -> Parent -> Child) ---
class Vehicle:
    def start(self):
        return "Engine started."

class FourWheeler(Vehicle):
    def doors(self):
        return "Has 4 doors."

class ElectricCar(FourWheeler):
    def battery(self):
        return "Runs on Battery."

ev = ElectricCar()
print("\n[2.2] Multilevel Inheritance:")
print(f"      {ev.start()} -> {ev.doors()} -> {ev.battery()}")


# --- 2.3 Multiple Inheritance (Two parents -> Child) ---
class Flyer:
    def fly(self):
        return "Can fly in air."

class Swimmer:
    def swim(self):
        return "Can swim in water."

class Duck(Flyer, Swimmer):
    pass

duck = Duck()
print("\n[2.3] Multiple Inheritance:")
print(f"      Duck: {duck.fly()} and {duck.swim()}")


# =============================================================================
# 3. POLYMORPHISM
# =============================================================================
# • "Many forms": Different classes implement the same method name,
#   allowing objects to be used interchangeably.

class Cat:
    def make_sound(self):
        return "Meow!"

class Cow:
    def make_sound(self):
        return "Moo!"

class Lion:
    def make_sound(self):
        return "Roar!"

animals = [Cat(), Cow(), Lion()]

print("\n[3] Polymorphism:")
for a in animals:
    print(f"    {a.__class__.__name__} -> {a.make_sound()}")


# =============================================================================
# 4. ENCAPSULATION
# =============================================================================
# • Restricting direct access to data to prevent accidental modification.
# • Public    : `var`    (accessible anywhere)
# • Protected : `_var`   (convention: internal/subclass use only)
# • Private   : `__var`  (name-mangled: cannot be accessed directly from outside)

class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner              # Public
        self._account_type = "Savings"  # Protected
        self.__balance = balance        # Private

    # Getter using @property
    @property
    def balance(self):
        return self.__balance

    # Setter with validation logic
    @balance.setter
    def balance(self, amount: float):
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self.__balance = amount

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid amount."

acc = BankAccount("Gaurav", 500.0)
print("\n[4] Encapsulation:")
print(f"    Owner (Public)            : {acc.owner}")
print(f"    Account Type (Protected)  : {acc._account_type}")
print(f"    Balance (Private via @prop): ${acc.balance}")
acc.deposit(250.0)
print(f"    After Deposit             : ${acc.balance}")
# acc.__balance  -> raises AttributeError (cannot access directly)


# =============================================================================
# 5. ABSTRACTION
# =============================================================================
# • Hiding complex internal logic and enforcing a standard interface.
# • Uses `ABC` and `@abstractmethod` from the `abc` module.
# • Any child class MUST implement all abstract methods to be instantiated.

class MLModel(ABC):
    @abstractmethod
    def train(self, data: list):
        """Every ML model must implement training."""
        pass

    @abstractmethod
    def predict(self, sample: list):
        """Every ML model must implement prediction."""
        pass

class LinearRegression(MLModel):
    def train(self, data: list):
        return f"Model trained on {len(data)} data points."

    def predict(self, sample: list):
        return f"Prediction output for {sample}: 42.5"

model = LinearRegression()
print("\n[5] Abstraction:")
print(f"    {model.train([1, 2, 3, 4, 5])}")
print(f"    {model.predict([10])}")

print("\n[SUCCESS] OOP Concepts Revision Complete!")
