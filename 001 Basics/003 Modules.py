"""
=============================================================================
📦 Python Modules, Packages & Standard Library - Quick Reference
Author: Gaurav Kumar Yadav
Topics:
  1. Modules (Definition, Import Styles, __name__ == '__main__')
  2. Packages (Folder Structure, __init__.py, Importing Submodules)
  3. Standard Library (Top built-in modules with practical examples)
  4. Standard Library vs Third-Party Packages (pip)
=============================================================================
"""

# =============================================================================
# 1. MODULES
# =============================================================================
# • Definition: A module is simply any single Python file (.py) containing code
#   (functions, classes, variables) that can be reused across other files.
# • Why use it: Code reusability, organization, and cleaner namespace.

# --- 1.1 Different Ways to Import ---

# A. Standard import (Access via module_name.item)
import math
print("[1.1A] math.sqrt(25):", math.sqrt(25))

# B. Import with alias (Rename for brevity - common in Data Science: np, pd)
import math as m
print("[1.1B] m.pi:", round(m.pi, 4))

# C. Specific import (Direct access without prefix)
from math import ceil, floor
print("[1.1C] ceil(4.2):", ceil(4.2), "| floor(4.8):", floor(4.8))

# D. Wildcard import (from module import *)
# • Avoid in production: Pollutes the global namespace & causes name collisions.


# --- 1.2 The __name__ == '__main__' Pattern ---
# • __name__ is a special built-in variable in Python.
# • When a file is RUN DIRECTLY: __name__ is set to "__main__".
# • When a file is IMPORTED: __name__ is set to the module's filename.
def calculate_area(radius: float) -> float:
    """Helper function inside this module."""
    return m.pi * (radius ** 2)

if __name__ == "__main__":
    # This block executes ONLY when running this file directly,
    # NOT when another file imports this file.
    print(f"[1.2] Direct Execution: Area of circle (r=3): {calculate_area(3):.2f}")


# =============================================================================
# 2. PACKAGES
# =============================================================================
# • Definition: A package is a directory/folder containing multiple modules (.py files)
#   along with a special `__init__.py` file.
# • Role of __init__.py:
#   - Tells Python to treat the folder as an importable package.
#   - Can be completely empty, or used to expose specific functions.
#
# • Typical Structure:
#   my_ml_project/
#   │
#   ├── ml_pipeline/              <-- Package folder
#   │   ├── __init__.py           <-- Marks directory as package
#   │   ├── data_prep.py          <-- Module 1
#   │   ├── model.py              <-- Module 2
#   │   └── evaluate.py           <-- Module 3
#   │
#   └── main.py                   <-- Application entry point
#
# • Usage in main.py:
#   from ml_pipeline.data_prep import clean_data
#   from ml_pipeline.model import train_model


# =============================================================================
# 3. PYTHON STANDARD LIBRARY (BATTERIES INCLUDED)
# =============================================================================
# • Definition: A rich set of built-in modules bundled with Python by default.
# • No `pip install` required — ready to use out of the box.

print("\n--- Standard Library Highlights ---")

# --- 3.1 `os` & `pathlib` (File & Operating System Operations) ---
import os
from pathlib import Path

current_dir = os.getcwd()
print("[3.1] Current Working Directory:", os.path.basename(current_dir))
file_path = Path("data") / "raw" / "dataset.csv"  # Cross-platform safe path joining
print("      Pathlib path:", file_path)

# --- 3.2 `sys` (System & Python Interpreter Settings) ---
import sys
print(f"[3.2] Python Version: {sys.version.split()[0]} | Platform: {sys.platform}")

# --- 3.3 `random` (Random Number Generation & Sampling) ---
import random
random.seed(42)  # For reproducibility in ML experiments
random_num = random.randint(1, 100)
chosen_tech = random.choice(["PyTorch", "TensorFlow", "Scikit-Learn"])
print(f"[3.3] Random Int: {random_num} | Random Choice: {chosen_tech}")

# --- 3.4 `datetime` (Date and Time Handling) ---
from datetime import datetime
now = datetime.now()
print(f"[3.4] Current Timestamp: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# --- 3.5 `json` (Serialization & Deserialization - Essential for APIs & Configs) ---
import json
config_dict = {"batch_size": 32, "learning_rate": 0.001, "optimizer": "Adam"}
json_string = json.dumps(config_dict)  # Python Dict -> JSON String
parsed_dict = json.loads(json_string)  # JSON String -> Python Dict
print(f"[3.5] JSON Serialized: {json_string}")
print(f"      Parsed lr: {parsed_dict['learning_rate']}")

# --- 3.6 `collections` (High-Performance Specialized Data Structures) ---
from collections import Counter
tokens = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_freq = Counter(tokens)
print(f"[3.6] Word Frequency (Counter): {dict(word_freq)}")


# =============================================================================
# 4. STANDARD LIBRARY VS THIRD-PARTY PACKAGES
# =============================================================================
# • Standard Library:
#   - Built-in with Python (e.g., math, os, sys, json, re, sqlite3).
#   - Zero installation needed.
#
# • Third-Party Packages:
#   - Created by the open-source community.
#   - Installed via package manager: `pip install numpy pandas requests`.
#   - Installed into: your virtual environment's `site-packages/` directory.

print("\n[SUCCESS] Modules, Packages & Standard Library Overview Completed!")
