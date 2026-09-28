# iterators:
# An iterator is an object that contains a countable number of values.

my_list = [1, 2, 3, 4]
for item in my_list:
    print(item)
    
type(my_list)  # <class 'list'>

itertor = iter(my_list)
type(itertor)  # <class 'list_iterator'>
print(next(itertor))  # 1
print(next(itertor))  # 2
print(next(itertor))  # 3
print(next(itertor))  # 4

# Generators:
# A generator is a function that returns an iterator that produces a sequence of values when iterated over. Generators are written like regular functions but use the yield statement whenever they want to return data.

def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    
gen = my_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # 4


# Decorators:
# A decorator is a function that takes another function as an argument, adds some functionality to it, and returns a new function. Decorators are often used to modify the behavior of functions or methods.

# function copy:
def welcome():
    return "Welcome to Python!"

wel=welcome()
print(wel())  # Welcome to Python!
del wel
print(welcome())  # Welcome to Python!
print(welcome)  # <function welcome at 0x7f8c8c8c8c80>


# closure:
# A closure is a function that has access to variables in its enclosing scope, even after the enclosing function has finished executing. Closures are often used to create functions that have some state or behavior that is preserved across multiple calls.

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(5)
print(closure(3))  # 8
print(closure(10))  # 15

# decorator example:

def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


@decorator
def hello():
    print("Hello!")


hello()

# Before function
# Hello!
# After function