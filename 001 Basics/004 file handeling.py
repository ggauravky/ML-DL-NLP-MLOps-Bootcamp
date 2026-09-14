"""
=============================================================================
📁 Python File Handling Revision Sheet
Author: Gaurav Kumar Yadav
Topics Covered:
  1. File Modes ('r', 'w', 'a', 'x', 'b')
  2. Context Manager (`with open(...)`)
  3. Reading Files (.read, .readline, .readlines, line-by-line loop)
  4. Writing & Appending Files
  5. File Pointer Management (.tell() & .seek())
  6. Working with Structured Data (JSON & CSV)
  7. Modern File Handling with `pathlib`
  8. Exception Handling with Files (FileNotFoundError)
=============================================================================
"""

import os
import csv
import json
from pathlib import Path

# Temporary file name for demonstrations
DEMO_FILE = "sample_demo.txt"


# =============================================================================
# 1. FILE OPENING MODES
# =============================================================================
# • 'r'  : Read (default). Fails if file does not exist.
# • 'w'  : Write. Creates new file OR completely truncates/overwrites existing.
# • 'a'  : Append. Adds new data to the end without deleting existing content.
# • 'x'  : Exclusive creation. Creates new file; fails if file already exists.
# • 'b'  : Binary mode (e.g., 'rb', 'wb' for images, model weights, pickles).
# • '+'  : Updating / read+write mode (e.g., 'r+', 'w+').


# =============================================================================
# 2. CONTEXT MANAGER (`with` statement) - BEST PRACTICE
# =============================================================================
# • Why use `with open(...)`:
#   - Automatically closes the file even if exceptions occur.
#   - Prevents memory leaks and file lock issues.
#   - Eliminates the need to call `file.close()` manually.

# Writing to a file using 'w' mode
with open(DEMO_FILE, "w", encoding="utf-8") as f:
    f.write("Line 1: Machine Learning Basics\n")
    f.write("Line 2: Deep Learning Architectures\n")
    f.write("Line 3: MLOps Production Pipelines\n")

print("[1 & 2] File created and written safely with context manager.")


# =============================================================================
# 3. READING FILES
# =============================================================================

# --- A. read() : Reads entire file as a single string ---
with open(DEMO_FILE, "r", encoding="utf-8") as f:
    full_content = f.read()
    print("\n[3.1] f.read():\n" + full_content.strip())

# --- B. readline() : Reads one line at a time ---
with open(DEMO_FILE, "r", encoding="utf-8") as f:
    first_line = f.readline().strip()
    second_line = f.readline().strip()
    print(f"\n[3.2] f.readline():\n      1 -> {first_line}\n      2 -> {second_line}")

# --- C. readlines() : Reads all lines into a Python List of strings ---
with open(DEMO_FILE, "r", encoding="utf-8") as f:
    lines_list = f.readlines()
    print(f"\n[3.3] f.readlines() (List): {lines_list}")

# --- D. Iterating Line-by-Line (Memory-Efficient for Large Datasets) ---
# • Best practice: Doesn't load the entire file into RAM at once.
print("\n[3.4] Iterating line-by-line:")
with open(DEMO_FILE, "r", encoding="utf-8") as f:
    for idx, line in enumerate(f, start=1):
        print(f"      [{idx}] {line.strip()}")


# =============================================================================
# 4. APPENDING TO A FILE ('a' mode)
# =============================================================================
# • Appends data to the end of the file without overwriting.
with open(DEMO_FILE, "a", encoding="utf-8") as f:
    f.write("Line 4: Cloud Deployment with Docker & AWS\n")

with open(DEMO_FILE, "r", encoding="utf-8") as f:
    print(f"\n[4] After Append (Total lines: {len(f.readlines())})")


# =============================================================================
# 5. FILE POINTER MANAGEMENT (.tell & .seek)
# =============================================================================
# • .tell() : Returns the current cursor position in bytes.
# • .seek(offset) : Repositions the file cursor to a specific byte index.
with open(DEMO_FILE, "r", encoding="utf-8") as f:
    print(f"\n[5] Cursor start position: {f.tell()}")
    f.read(10)  # Read first 10 bytes
    print(f"    Cursor after reading 10 bytes: {f.tell()}")
    
    f.seek(0)   # Reset cursor back to the beginning of the file
    print(f"    Cursor reset with seek(0): {f.tell()}")
    print(f"    Re-read first line: {f.readline().strip()}")


# =============================================================================
# 6. STRUCTURED DATA FILES (JSON & CSV - ESSENTIAL FOR ML/DATA SCIENCE)
# =============================================================================

# --- A. Working with JSON (.json) ---
json_file = "sample_config.json"
model_metadata = {
    "model_name": "ResNet50",
    "epochs": 25,
    "batch_size": 64,
    "accuracy": 0.942
}

# json.dump() : Python dict -> file
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(model_metadata, f, indent=2)

# json.load() : file -> Python dict
with open(json_file, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print(f"\n[6.1] JSON Loaded: model={loaded_data['model_name']}, acc={loaded_data['accuracy']}")

# --- B. Working with CSV (.csv) ---
csv_file = "sample_data.csv"
dataset = [
    ["Name", "Score", "Result"],
    ["Alice", 92, "Pass"],
    ["Bob", 45, "Fail"],
    ["Charlie", 78, "Pass"]
]

# csv.writer : writing tabular data
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(dataset)

# csv.DictReader : reading rows as convenient Python dictionaries
print("\n[6.2] CSV Read with DictReader:")
with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"      {row['Name']} -> Score: {row['Score']}, Result: {row['Result']}")


# =============================================================================
# 7. MODERN FILE HANDLING WITH `pathlib` (OBJECT-ORIENTED)
# =============================================================================
# • Recommended standard in modern Python 3.
# • Cross-platform: handles Windows '\' vs Linux '/' automatically.
p = Path("sample_pathlib.txt")

# Quick write & read without explicit open/close boilerplate:
p.write_text("Fast one-liner write using pathlib Path.write_text()", encoding="utf-8")
print(f"\n[7] Pathlib Read: {p.read_text(encoding='utf-8')}")
print(f"    File exists: {p.exists()} | Is file: {p.is_file()} | File size: {p.stat().st_size} bytes")


# =============================================================================
# 8. EXCEPTION HANDLING WITH FILES
# =============================================================================
# • Always handle missing files or permission errors gracefully.
missing_file = "non_existent_data.csv"
try:
    with open(missing_file, "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print(f"\n[8] Handled Exception: '{missing_file}' not found. Fallback triggered.")
except PermissionError:
    print(f"\n[8] Permission denied to access '{missing_file}'.")


# =============================================================================
# 9. CLEANUP DEMO FILES
# =============================================================================
# Clean up temporary sample files created during this run
for temp_file in [DEMO_FILE, json_file, csv_file, "sample_pathlib.txt"]:
    if os.path.exists(temp_file):
        os.remove(temp_file)

print("\n[SUCCESS] File Handling Revision Complete! (Demo files cleaned up)")
