# Quick Reference Card

## 🚀 Common Commands

### Testing
```bash
# Python - test one challenge
pytest tests/python/test_01_hello_world.py -v

# Python - test all
pytest tests/python/ -v

# C - compile and run
cd beginner/c/01_hello_world
gcc solution.c -o solution -lm
./solution

# Java - compile and run
cd beginner/java/01_hello_world
javac Solution.java
java Solution
```

### Grading
```bash
# Grade all
python grading/grade_all.py

# Grade specific language
python grading/grade_all.py --language python

# Grade specific challenge
python grading/grade_all.py --challenge beginner/python/01_hello_world

# View progress
python grading/view_progress.py
```

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Verify setup
python verify_setup.py
```

## 📁 File Locations

| Item | Path |
|------|------|
| Challenges | `beginner/{language}/{challenge_number}_name/` |
| Tests | `tests/{language}/test_{challenge_number}_name.py` |
| Grading | `grading/grade_all.py` |
| Progress | `grading/view_progress.py` |

## 🎯 Challenge Template Structure

Each challenge has:
- `README.md` - Problem description
- `solution.{py|c|java}` - Your implementation file

## ⚡ Workflow

1. `cd` to challenge directory
2. Read `README.md`
3. Edit solution file
4. Run tests
5. Debug if needed
6. Get grade
7. Move to next challenge

## 🐛 Debugging Tips

```bash
# Python - verbose output
pytest test_file.py -vv

# Python - print output during tests
pytest test_file.py -v -s

# Python - run specific test
pytest test_file.py::test_function_name -v

# C - enable warnings
gcc -Wall -Wextra solution.c -o solution

# Java - show all errors
javac -Xlint:all Solution.java
```

## 📊 Grade Scale

| Score | Grade | Meaning |
|-------|-------|---------|
| 100% | A+ | Perfect! |
| 90-99% | A | Excellent |
| 80-89% | B | Good |
| 70-79% | C | Satisfactory |
| 60-69% | D | Needs improvement |
| <60% | F | Keep trying |

## 🔗 Documentation

- [README.md](README.md) - Project overview
- [GETTING_STARTED.md](GETTING_STARTED.md) - Beginner guide
- [CHALLENGE_INDEX.md](CHALLENGE_INDEX.md) - All challenges
- [SETUP.md](SETUP.md) - Installation guide

## 💡 Pro Tips

1. **Read carefully** - Requirements are in the README
2. **Test often** - Run tests after each change
3. **Start simple** - Don't skip ahead
4. **Understand tests** - Look at test files to see what's checked
5. **Track progress** - Use `view_progress.py` regularly

## 🆘 Quick Fixes

### pytest not found
```bash
pip install pytest pytest-json-report
```

### Import errors in tests
```bash
# Make sure you're in the right directory
cd /path/to/project/root
pytest tests/python/test_file.py -v
```

### C math functions
```bash
# Include -lm flag for math.h
gcc solution.c -o solution -lm
```

---

Keep this card handy! 📌
