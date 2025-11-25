# Troubleshooting Guide

Common issues and their solutions.

---

## Python Issues

### Issue: pytest not found
```
bash: pytest: command not found
```

**Solution:**
```bash
pip install pytest pytest-json-report
# or
pip install -r requirements.txt
```

---

### Issue: Import errors in tests
```
ImportError: No module named 'solution'
```

**Solution:**
- Make sure you're running pytest from the project root
- Or use the full path to the test file
```bash
cd /path/to/project/root
pytest tests/python/test_01_hello_world.py -v
```

---

### Issue: Tests fail with "NameError: name 'pass' is not defined"
```
NameError: name 'pass' is not defined
```

**Solution:**
- You forgot to replace `pass` with actual code
- `pass` is a placeholder - replace it with your implementation

**Before:**
```python
def hello_world():
    pass  # Replace with your code
```

**After:**
```python
def hello_world():
    return "Hello, World!"
```

---

### Issue: All tests fail immediately
```
FAILED tests/python/test_01_hello_world.py::test_hello_world
```

**Solution:**
1. Check if you saved the solution file
2. Verify function name matches exactly
3. Check return type (return, not print)
4. Run with `-vv` for detailed output:
```bash
pytest tests/python/test_01_hello_world.py -vv
```

---

## C Issues

### Issue: gcc not found
```
bash: gcc: command not found
```

**Solution (Windows with WSL):**
```bash
sudo apt update
sudo apt install build-essential
```

**Solution (Mac):**
```bash
xcode-select --install
```

**Solution (Linux):**
```bash
sudo apt install gcc
# or
sudo yum install gcc
```

---

### Issue: Math functions undefined
```
undefined reference to 'sqrt'
undefined reference to 'pow'
```

**Solution:**
Include the math library with `-lm` flag:
```bash
gcc solution.c -o solution -lm
```

---

### Issue: Compilation errors with structs
```
error: storage size of 'p' isn't known
```

**Solution:**
- Make sure struct is defined before use
- Check typedef syntax
```c
typedef struct {
    int x;
    int y;
} Point;  // Don't forget semicolon!
```

---

### Issue: Segmentation fault
```
Segmentation fault (core dumped)
```

**Common Causes:**
1. Array out of bounds
2. Null pointer dereference
3. String missing null terminator
4. Buffer overflow

**Debug tips:**
```bash
# Compile with debug info
gcc -g solution.c -o solution

# Run with gdb
gdb ./solution
```

---

## Java Issues

### Issue: javac not found
```
bash: javac: command not found
```

**Solution:**
Install Java JDK (not just JRE):

**Windows:**
Download from: https://www.oracle.com/java/technologies/downloads/

**Mac:**
```bash
brew install openjdk
```

**Linux:**
```bash
sudo apt install default-jdk
```

---

### Issue: Class name mismatch
```
Error: Could not find or load main class Solution
```

**Solution:**
- File name must match class name
- `Solution.java` must contain `public class Solution`
- Case-sensitive!

---

### Issue: Main method not found
```
Error: Main method not found in class Solution
```

**Solution:**
Check main method signature exactly:
```java
public static void main(String[] args) {
    // ...
}
```

Common mistakes:
- Missing `public`
- Missing `static`
- Wrong parameter type
- Typo in method name

---

## Grading System Issues

### Issue: grade_all.py - Module not found
```
ModuleNotFoundError: No module named 'pytest'
```

**Solution:**
```bash
pip install -r requirements.txt
```

---

### Issue: No tests found
```
No tests found
```

**Solution:**
1. Check you're in the project root
2. Verify test files exist in `tests/python/`
3. Make sure test files start with `test_`

---

### Issue: All challenges show 0%
```
Score: 0.0%
Grade: F
```

**Possible Causes:**
1. Solutions not implemented (still have `pass`)
2. Test files not found
3. Import errors in tests

**Solution:**
```bash
# Test directly to see detailed errors
pytest tests/python/test_01_hello_world.py -vv
```

---

## General Issues

### Issue: Permission denied
```
bash: ./script.sh: Permission denied
```

**Solution:**
```bash
chmod +x script.sh
./script.sh
```

---

### Issue: Line ending problems (Windows)
```
bash: ./script.sh: /bin/bash^M: bad interpreter
```

**Solution:**
Convert line endings:
```bash
dos2unix script.sh
# or
sed -i 's/\r$//' script.sh
```

---

### Issue: Path not found (Windows)
```
python: can't open file 'grading/grade_all.py'
```

**Solution:**
Use correct path separator:
```bash
# Windows CMD
python grading\grade_all.py

# Windows PowerShell or WSL
python grading/grade_all.py

# Or use forward slashes (works in all)
python grading/grade_all.py
```

---

## Test-Specific Issues

### Issue: Tests pass but grade shows 0%
```
3 passed in 0.02s
But grading shows: Score: 0.0%
```

**Solution:**
- Run grading script from project root
- Check if pytest-json-report is installed
```bash
pip install pytest-json-report
```

---

### Issue: Timeout errors
```
FAILED tests/python/test_09_fizzbuzz.py::test_fizzbuzz_15 - Timeout
```

**Possible Causes:**
1. Infinite loop in your code
2. Very inefficient solution

**Solution:**
- Check for infinite loops
- Use print statements to debug
- Simplify logic

---

## Getting More Help

### Enable Verbose Output

**Python:**
```bash
pytest test_file.py -vv -s
```

**C:**
```bash
gcc -Wall -Wextra solution.c -o solution
```

**Java:**
```bash
javac -Xlint:all Solution.java
```

### Check Setup
```bash
python verify_setup.py
```

### Common Debug Pattern
1. Read error message carefully
2. Check line number mentioned
3. Verify syntax
4. Test with simple input first
5. Add print statements
6. Run tests incrementally

---

## Still Stuck?

### Things to Check:
- [ ] Saved the file?
- [ ] In the right directory?
- [ ] Correct file name?
- [ ] Correct function/method name?
- [ ] Correct return type?
- [ ] All syntax correct?
- [ ] Dependencies installed?

### Get Specific Error Info:
```bash
# Python - very verbose
pytest test_file.py -vv -s

# C - show warnings
gcc -Wall -Wextra -pedantic solution.c

# Java - show all warnings
javac -Xlint:all Solution.java
```

---

**Most issues are simple typos or missing installations. Check the basics first!**
