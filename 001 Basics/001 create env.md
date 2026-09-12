# 🐍 Python Virtual Environment Guide

A quick, step-by-step reference for creating and managing Python virtual environments across all common methods.

---

## ⚡ Method 1: Built-in `venv` (Standard & Recommended)

No installation required — comes bundled with Python.

### Step 1: Open terminal in your project directory
```bash
cd /path/to/your/project
```

### Step 2: Create the virtual environment
```bash
# Windows / macOS / Linux
python -m venv myenv
```
*(Replace `myenv` with your preferred name, e.g., `.venv` or `env`)*

### Step 3: Activate the environment
- **Windows (PowerShell):**
  ```powershell
  .\myenv\Scripts\Activate.ps1
  ```
- **Windows (Command Prompt):**
  ```cmd
  myenv\Scripts\activate.bat
  ```
- **macOS / Linux (Bash/Zsh):**
  ```bash
  source myenv/bin/activate
  ```

### Step 4: Verify activation
```bash
# Should point to your virtual environment's python
where python    # Windows
which python    # macOS / Linux
```

### Step 5: Deactivate
```bash
deactivate
```

---

## ⚡ Method 2: `conda` (Best for Data Science & ML)

Ideal for managing complex C-libraries, CUDA, and different Python versions.

### Step 1: Create an environment
```bash
# With default Python version
conda create -n myenv

# With a specific Python version (Recommended)
conda create -n myenv python=3.11 -y
```

### Step 2: Activate
```bash
conda activate myenv
```

### Step 3: Verify
```bash
python --version
conda info --envs
```

### Step 4: Deactivate
```bash
conda deactivate
```

### Step 5: Delete environment (when no longer needed)
```bash
conda remove -n myenv --all -y
```

---

## ⚡ Method 3: `uv` (Ultra-Fast Modern Package Manager)

10x–100x faster than standard pip/venv.

### Step 1: Install `uv` (one-time)
```bash
pip install uv
# OR via curl/powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Step 2: Create a virtual environment
```bash
# Default Python
uv venv myenv

# With a specific Python version
uv venv myenv --python 3.11
```

### Step 3: Activate
- **Windows:**
  ```powershell
  .\myenv\Scripts\activate
  ```
- **macOS / Linux:**
  ```bash
  source myenv/bin/activate
  ```

### Step 4: Fast package installation
```bash
uv pip install numpy pandas scikit-learn
```

---

## ⚡ Method 4: `virtualenv` (Classic Tool)

Useful for older Python workflows or custom interpreters.

### Step 1: Install `virtualenv` (one-time)
```bash
pip install virtualenv
```

### Step 2: Create environment
```bash
# Default Python
virtualenv myenv

# Specific Python version
virtualenv -p python3.10 myenv
```

### Step 3: Activate
- **Windows:**
  ```powershell
  .\myenv\Scripts\activate
  ```
- **macOS / Linux:**
  ```bash
  source myenv/bin/activate
  ```

---

## 📓 Connect Virtual Environment to Jupyter Notebook

To use your environment inside Jupyter notebooks:

### Step 1: Activate your environment first
```powershell
.\myenv\Scripts\activate
```

### Step 2: Install `ipykernel`
```bash
pip install ipykernel
```

### Step 3: Register your environment as a Jupyter kernel
```bash
python -m ipykernel install --user --name=myenv --display-name "Python (myenv)"
```

### Step 4: Remove kernel (when done)
```bash
jupyter kernelspec uninstall myenv
```

---

## 📦 Essential Environment Commands

| Action | Command |
| :--- | :--- |
| **Save dependencies** | `pip freeze > requirements.txt` |
| **Install dependencies** | `pip install -r requirements.txt` |
| **List installed packages** | `pip list` |
| **Check current environment** | `python -c "import sys; print(sys.executable)"` |
| **Deactivate environment** | `deactivate` |
| **Delete `venv` environment** | Simply delete the `myenv` folder |

---

## ⚠️ Common Windows Issue: Script Execution Blocked

If PowerShell shows: `File ... Activate.ps1 cannot be loaded because running scripts is disabled on this system.`

**Run this once in PowerShell:**
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
Then run the activate command again:
```powershell
.\myenv\Scripts\Activate.ps1
```
