# Setup Instructions

## Quick Start

### 1. Install Dependencies

```bash
# Install Python dependencies
pip install -r requirements.txt

# Verify installation
pytest --version
python --version
```

### 2. Try Your First Challenge

```bash
# Navigate to a challenge
cd beginner/python/01_hello_world

# Read the challenge
cat README.md

# Edit the solution file
# (Implement your solution in solution.py)

# Run the tests
pytest ../../tests/python/test_01_hello_world.py -v
```

### 3. Get Your Grade

```bash
# From the root directory
python grading/grade_all.py --language python

# Or grade a specific challenge
python grading/grade_all.py --challenge beginner/python/01_hello_world
```

## Testing Individual Challenges

### Python
```bash
# Test a specific challenge
cd beginner/python/01_hello_world
pytest ../../tests/python/test_01_hello_world.py -v

# Test all Python challenges
pytest tests/python/ -v
```

### C
```bash
# Compile and test
cd beginner/c/01_hello_world
gcc solution.c -o solution -lm
./solution

# For struct challenge, include math library
gcc solution.c -o solution -lm
```

### Java
```bash
# Compile
cd beginner/java/01_hello_world
javac Solution.java

# Run
java Solution
```

## Automated Grading

### Grade All Challenges
```bash
python grading/grade_all.py
```

### Grade Specific Language
```bash
python grading/grade_all.py --language python
python grading/grade_all.py --language java
python grading/grade_all.py --language c
```

### Grade Specific Challenge
```bash
python grading/grade_all.py --challenge beginner/python/01_hello_world
```

### View Your Progress
```bash
python grading/view_progress.py
```

## Challenge Structure

Each challenge includes:
- `README.md` - Problem description and requirements
- `solution.{py|java|c}` - Template file for your solution
- Test file in `tests/` directory

## Tips

1. **Read the README carefully** - It contains all requirements and examples
2. **Start with beginner level** - Build your foundation first
3. **Run tests frequently** - Verify your solution as you code
4. **Check your progress** - Use `view_progress.py` to track your journey
5. **Don't skip challenges** - Each builds on previous concepts

## Grading Scale

- **100%**: Perfect! All tests pass
- **90-99%**: Excellent (A)
- **80-89%**: Good (B)
- **70-79%**: Satisfactory (C)
- **60-69%**: Needs improvement (D)
- **<60%**: Keep trying (F)

## Next Steps

After completing the beginner level, you can progress to:
- **Intermediate** (Coming soon)
- **Advanced** (Coming soon)
- **Master** (Coming soon)

---

**Happy Coding! 🚀**
