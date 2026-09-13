"""
=============================================================================
⚠️ Python Exception Handling Revision Sheet
Author: Gaurav Kumar Yadav
Topics Covered:
  1. Core Structure (try, except, else, finally)
  2. Catching Specific Exceptions (ValueError, ZeroDivisionError, KeyError)
  3. Multiple Exceptions & Exception Aliasing (as e)
  4. The 'else' & 'finally' Blocks Explained
  5. Raising Exceptions Manually (raise)
  6. Custom User-Defined Exceptions (class MyError(Exception))
  7. Built-in Exception Hierarchy & Senior Best Practices
=============================================================================
"""

# =============================================================================
# 1. CORE SYNTAX (try - except)
# =============================================================================
# • Purpose: Prevents program crashes when runtime errors occur.
# • try block   : Code that might raise an exception.
# • except block: Code that handles the error if it occurs.

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"[1] Caught ZeroDivisionError: {e}")


# =============================================================================
# 2. CATCHING SPECIFIC EXCEPTIONS
# =============================================================================
# • Best Practice: Never use a bare 'except:' — always catch specific errors!
# • Common Built-in Exceptions:
#   - ValueError        : Right type, wrong value (e.g., int("abc"))
#   - TypeError         : Operation applied to wrong type (e.g., "5" + 5)
#   - IndexError        : Sequence index out of range
#   - KeyError          : Dictionary key not found
#   - ZeroDivisionError : Dividing by zero

def parse_age(age_str: str) -> int:
    try:
        age = int(age_str)
        return age
    except ValueError as e:
        print(f"[2] Invalid integer conversion: '{age_str}' -> {e}")
        return -1

parse_age("not_a_number")


# =============================================================================
# 3. MULTIPLE EXCEPT BLOCKS & GROUPING
# =============================================================================
# • You can chain multiple except blocks for different error types.
# • Or group related exceptions into a single tuple: except (TypeError, ValueError)

def access_and_divide(data_list: list, index: int, divisor: int):
    try:
        val = data_list[index]
        return val / divisor
    except IndexError:
        print(f"[3.1] IndexError: Index {index} is out of bounds.")
    except ZeroDivisionError:
        print("[3.2] ZeroDivisionError: Cannot divide by zero.")
    except (TypeError, ValueError) as err:
        print(f"[3.3] Type/Value error occurred: {err}")

access_and_divide([10, 20], 5, 2)   # Triggers IndexError
access_and_divide([10, 20], 0, 0)   # Triggers ZeroDivisionError


# =============================================================================
# 4. THE COMPLETE PATTERN: try - except - else - finally
# =============================================================================
# • try     : Run the risky code.
# • except  : Executes ONLY if an exception occurs.
# • else    : Executes ONLY if NO exception occurs (success block).
# • finally : ALWAYS executes, regardless of success or exception.
#             (Crucial for releasing resources: DB disconnects, closing files, etc.)

def divide_numbers(a: float, b: float):
    print(f"\n[4] Dividing {a} by {b}:")
    try:
        calc = a / b
    except ZeroDivisionError:
        print("    [except] Division by zero caught!")
    else:
        print(f"    [else] Success! Result = {calc}")
    finally:
        print("    [finally] Cleanup code executed (always runs).")

divide_numbers(10, 2)  # Success path (triggers try -> else -> finally)
divide_numbers(10, 0)  # Error path   (triggers try -> except -> finally)


# =============================================================================
# 5. RAISING EXCEPTIONS MANUALLY (raise)
# =============================================================================
# • Use 'raise' when business rules or data validation constraints are violated.

def validate_learning_rate(lr: float):
    if lr <= 0 or lr >= 1:
        raise ValueError(f"Learning rate must be between 0 and 1. Received: {lr}")
    return f"Valid learning rate: {lr}"

try:
    print(f"\n[5] {validate_learning_rate(0.01)}")
    validate_learning_rate(-0.5)  # Invalid value
except ValueError as err:
    print(f"    [Caught Raised Error] {err}")


# =============================================================================
# 6. CUSTOM USER-DEFINED EXCEPTIONS
# =============================================================================
# • Create custom exceptions by inheriting from Python's built-in `Exception` class.
# • Highly recommended in production ML/MLOps pipelines for custom domain errors.

class ModelNotTrainedError(Exception):
    """Raised when inference is attempted on an untrained ML model."""
    def __init__(self, model_name: str, message: str = "Model must be trained before predicting."):
        self.model_name = model_name
        self.message = f"[{model_name}] {message}"
        super().__init__(self.message)

class MockMLPipeline:
    def __init__(self, name: str):
        self.name = name
        self.is_trained = False

    def predict(self, sample_input: list):
        if not self.is_trained:
            raise ModelNotTrainedError(self.name)
        return [0.95]

pipeline = MockMLPipeline("CustomerChurnClassifier")
try:
    pipeline.predict([1, 0, 24])
except ModelNotTrainedError as e:
    print(f"\n[6] Custom Exception Caught: {e}")


# =============================================================================
# 7. SENIOR DEVELOPER BEST PRACTICES
# =============================================================================
# • 1. Specific over Generic: Catch `FileNotFoundError` instead of broad `Exception`.
# • 2. Keep try blocks minimal: Only wrap the lines that actually might fail.
# • 3. Never silence errors silently:
#      AVOID: except Exception: pass
#      PREFER: Log the error or handle it explicitly.
# • 4. Exception Hierarchy Reference:
#      BaseException
#       ├── KeyboardInterrupt  (Ctrl+C)
#       └── Exception          (All application errors inherit from here)
#            ├── ArithmeticError (ZeroDivisionError, OverflowError)
#            ├── LookupError     (IndexError, KeyError)
#            ├── ValueError
#            ├── TypeError
#            └── OSError         (FileNotFoundError, PermissionError)

print("\n[SUCCESS] Exception Handling Revision Complete!")
