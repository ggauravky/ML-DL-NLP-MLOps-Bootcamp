"""
=============================================================================
🐍 Python Fundamentals Revision Sheet
Author: Gaurav Kumar Yadav
Topics Covered:
  1. Syntax, Printing & Comments
  2. Variables & Primitive Data Types
  3. Type Casting
  4. Operators (Arithmetic, Comparison, Logical, Membership, Identity)
  5. Core Collections (List, Tuple, Set, Dictionary)
  6. Conditionals (if, elif, else & Ternary)
  7. Loops (for, while, range, enumerate, zip, break/continue)
  8. List Comprehensions
  9. Functions (*args, **kwargs, defaults, lambda)
=============================================================================
"""

# ==========================================
# 1. SYNTAX, COMMENTS & PRINTING
# ==========================================
# Single-line comment starts with '#'
"""
Multi-line comment / Docstring
using triple quotes
"""

name = "Gaurav"
role = "AI/ML Learner"

# Modern printing using f-strings (formatted strings)
print(f"[1] Hello, {name}! Role: {role}")


# ==========================================
# 2. VARIABLES & DATA TYPES
# ==========================================
age: int = 20                 # Integer
gpa: float = 8.5              # Floating point number
is_student: bool = True       # Boolean (True / False)
middle_name: None = None      # NoneType (absence of a value)

print(f"[2] Types: age={type(age)}, gpa={type(gpa)}, is_student={type(is_student)}, None={type(middle_name)}")


# ==========================================
# 3. TYPE CASTING (CONVERSION)
# ==========================================
num_str = "100"
converted_int = int(num_str)       # "100" -> 100
converted_float = float(num_str)   # "100" -> 100.0
converted_bool = bool(1)           # 1 -> True (0 is False, empty string/list is False)

print(f"[3] Casting: {num_str} -> int: {converted_int}, float: {converted_float}, bool: {converted_bool}")


# ==========================================
# 4. OPERATORS
# ==========================================
a, b = 10, 3

# Arithmetic: +, -, *, /, // (floor div), % (modulus), ** (power)
print(f"[4.1] Arithmetic: {a} / {b} = {a / b:.2f}, {a} // {b} = {a // b}, {a} % {b} = {a % b}, {a} ** {b} = {a ** b}")

# Comparison: ==, !=, >, <, >=, <=
print(f"[4.2] Comparison: {a} > {b} is {a > b}, {a} == {b} is {a == b}")

# Logical: and, or, not
print(f"[4.3] Logical: (a > 5 and b < 5) -> {a > 5 and b < 5}, not(a == 10) -> {not (a == 10)}")

# Membership: in, not in
nums = [1, 2, 3, 4, 5]
print(f"[4.4] Membership: 3 in nums -> {3 in nums}, 10 not in nums -> {10 not in nums}")

# Identity: is, is not (checks exact memory address/identity, not just value equality)
x, y = [1, 2], [1, 2]
print(f"[4.5] Identity vs Equality: x == y is {x == y} (same values), but x is y is {x is y} (different objects in memory)")


# ==========================================
# 5. CORE COLLECTIONS / DATA STRUCTURES
# ==========================================

# --- A. LIST: Ordered, Mutable, Allows Duplicates ---
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")      # Add to end
fruits.insert(1, "orange")  # Insert at index 1
fruits.pop()                # Removes last item ("mango")
# Slicing: [start:stop:step]
print(f"[5.1] List: {fruits}, Sliced (first 2): {fruits[:2]}")

# --- B. TUPLE: Ordered, IMMUTABLE (cannot change after creation) ---
coordinates = (19.0760, 72.8777)  # Lat, Long
lat, lon = coordinates            # Unpacking
print(f"[5.2] Tuple: {coordinates}, Unpacked: lat={lat}, lon={lon}")

# --- C. SET: Unordered, Unique Elements (No Duplicates) ---
tags = {"python", "ai", "ml", "python"}  # "python" duplicate removed automatically
tags.add("nlp")
other_tags = {"ml", "deep learning"}
print(f"[5.3] Set: {tags}")
print(f"      Union: {tags | other_tags}")
print(f"      Intersection: {tags & other_tags}")

# --- D. DICTIONARY: Key-Value Pairs, Fast O(1) Lookups ---
student = {
    "name": "Gaurav",
    "track": "MLOps",
    "level": "Intermediate"
}
student["skills"] = ["Python", "Docker"]  # Add new key-value pair
student_track = student.get("track", "Unknown")  # Safe retrieval (.get prevents KeyError)
print(f"[5.4] Dict: name={student['name']}, track={student_track}, keys={list(student.keys())}")


# ==========================================
# 6. CONDITIONALS (CONTROL FLOW)
# ==========================================
score = 85

# Standard if-elif-else
if score >= 90:
    grade = "A+"
elif score >= 75:
    grade = "A"
elif score >= 50:
    grade = "B"
else:
    grade = "C"

# Ternary Operator (One-line if-else)
status = "Passed" if score >= 50 else "Failed"
print(f"[6] Grade: {grade}, Status: {status}")


# ==========================================
# 7. LOOPS & ITERATION
# ==========================================

# --- A. For Loop with range(start, stop, step) ---
print("[7.1] For Loop with range:", end=" ")
for i in range(1, 6):
    print(i, end=" ")
print()

# --- B. Iterating over list with enumerate() (gives both index & value) ---
print("[7.2] Enumerate:")
for idx, fruit in enumerate(fruits, start=1):
    print(f"      {idx}. {fruit}")

# --- C. Parallel Iteration with zip() ---
names = ["Alice", "Bob", "Charlie"]
scores = [92, 85, 78]
print("[7.3] Zip:")
for n, s in zip(names, scores):
    print(f"      {n} scored {s}")

# --- D. While Loop ---
print("[7.4] While Loop:", end=" ")
count = 3
while count > 0:
    print(count, end=" ")
    count -= 1
print("Blast off!")

# --- E. Loop Controls: break & continue ---
print("[7.5] break & continue:", end=" ")
for n in range(1, 10):
    if n == 3:
        continue  # Skip number 3
    if n == 6:
        break     # Stop loop when n reaches 6
    print(n, end=" ")
print()


# ==========================================
# 8. LIST COMPREHENSIONS (PYTHONIC SHORTCUTS)
# ==========================================
# Syntax: [expression for item in iterable if condition]
numbers = [1, 2, 3, 4, 5, 6]

# Square of even numbers only
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print(f"[8] List Comprehension (Even Squares): {even_squares}")


# ==========================================
# 9. FUNCTIONS
# ==========================================

# --- A. Basic Function with Default Argument ---
def greet(user: str, greeting: str = "Welcome") -> str:
    """Returns a formatted greeting message."""
    return f"{greeting}, {user}!"

print(f"[9.1] Function: {greet('Gaurav')}")
print(f"      Custom:   {greet('Gaurav', 'Good evening')}")

# --- B. *args (Variable Positional Args) & **kwargs (Variable Keyword Args) ---
def summarize(*args, **kwargs):
    print(f"[9.2] *args (tuple): {args}")
    print(f"      **kwargs (dict): {kwargs}")

summarize(10, 20, 30, framework="PyTorch", epoch=50, lr=0.001)

# --- C. Lambda Functions (Small One-line Anonymous Functions) ---
# Syntax: lambda arguments: expression
multiply = lambda x, y: x * y
print(f"[9.3] Lambda (4 * 5): {multiply(4, 5)}")

# Using lambda for custom sorting:
pairs = [(1, "b"), (3, "a"), (2, "c")]
sorted_pairs = sorted(pairs, key=lambda item: item[1])  # Sort by second element ('a', 'b', 'c')
print(f"      Sorted by letter: {sorted_pairs}")

print("\n[SUCCESS] Python Basics Revision Complete!")
