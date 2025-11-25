# Self-Testing Multi-Language Coding Platform

A comprehensive coding challenge repository with **automated testing and grading** across C, Java, and Python. Practice programming fundamentals, get instant feedback, and track your progress.

## 🎯 Overview

This repository contains **30 beginner-level coding challenges** (10 per language) with complete automated testing infrastructure. Each challenge includes a problem description, solution template, and comprehensive test suite. Perfect for learning, interview prep, or maintaining your coding skills.

## 💻 Languages & Challenges

### **Python** (10 challenges)
Functions, lists, dictionaries, string manipulation, list comprehension, and iteration patterns.

### **C** (10 challenges)  
Pointers, arrays, memory management, structs, and systems programming fundamentals.

### **Java** (10 challenges)
Object-oriented programming, classes, collections, exception handling, and enterprise patterns.

**Total: 30 challenges** covering fundamental programming concepts across three languages.

## 📁 Repository Structure

```
self_testing_multilanguage/
├── beginner/                    # All challenges (only level currently)
│   ├── python/                  # 10 Python challenges
│   │   ├── 01_hello_world/
│   │   ├── 02_sum_two_numbers/
│   │   ├── 03_is_even/
│   │   └── ... (7 more)
│   ├── c/                       # 10 C challenges  
│   │   ├── 01_hello_world/
│   │   ├── 02_sum_two_numbers/
│   │   └── ... (8 more)
│   └── java/                    # 10 Java challenges
│       ├── 01_hello_world/
│       ├── 02_sum_two_numbers/
│       └── ... (8 more)
│
├── tests/                       # Automated test suites
│   ├── python/                  # pytest test files (10 files)
│   ├── c/                       # C test runner (run_tests.sh)
│   └── java/                    # Java test infrastructure
│
├── grading/                     # Automated grading system
│   ├── grade_all.py            # Main grading script
│   └── view_progress.py        # Progress tracking
│
├── notebooks/                   # Jupyter notebooks for Python challenges
│   └── beginner_python_challenges.ipynb
│
└── [Documentation files...]     # Guides and references
```

## 🧪 Automated Testing & Grading

### Run All Tests
```bash
# Test all languages at once
./test_all.sh
# or
python grading/grade_all.py
```

### Test by Language
```bash
# Python only
python grading/grade_all.py --language python

# C only  
python grading/grade_all.py --language c

# Java only
python grading/grade_all.py --language java
```

### Test Specific Challenge
```bash
python grading/grade_all.py --challenge beginner/python/01_hello_world
```

### Test Manually
```bash
# Python (using pytest)
pytest tests/python/test_01_hello_world.py -v

# C (compile and run)
cd beginner/c/01_hello_world
gcc solution.c -o solution && ./solution

# Java (compile and run)
cd beginner/java/01_hello_world
javac Solution.java && java Solution
```

## 📊 Grading System

Grades are calculated based on test pass rate:

| Score | Grade | Description |
|-------|-------|-------------|
| 100% | A+ | Perfect! All tests pass |
| 90-99% | A | Excellent |
| 80-89% | B | Good |
| 70-79% | C | Satisfactory |
| 60-69% | D | Needs improvement |
| <60% | F | Keep trying |

### View Your Progress
```bash
python grading/view_progress.py
```

Shows completion statistics, average scores, and recent activity across all challenges.

## 🚀 Quick Start

### 1. Verify Prerequisites
```bash
python verify_setup.py
```

**Required:**
- Python 3.8+
- GCC (for C challenges)
- Java 11+ (for Java challenges)

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Try Your First Challenge
```bash
# Navigate to a challenge
cd beginner/python/01_hello_world

# Read the problem
cat README.md

# Edit solution.py with your implementation

# Run tests
pytest ../../tests/python/test_01_hello_world.py -v

# Get your grade
python ../../../grading/grade_all.py --challenge beginner/python/01_hello_world
```

## 🎓 Skills You'll Practice

### Core Programming Concepts
- Functions and method definitions
- Variables and data types
- Control flow (if/else, loops)
- Basic data structures (arrays, lists, dictionaries)
- String manipulation and processing

### Language-Specific Skills
- **Python**: List comprehension, dictionary operations, Pythonic patterns
- **C**: Pointer arithmetic, memory management, manual string handling
- **Java**: OOP principles, classes/objects, exception handling, collections

### Testing & Quality
- Writing testable code
- Understanding test cases
- Debugging failed tests
- Code verification and validation

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [START_HERE.md](START_HERE.md) | Best starting point for new users |
| [GETTING_STARTED.md](GETTING_STARTED.md) | Comprehensive beginner guide |
| [SETUP.md](SETUP.md) | Installation and configuration |
| [CHALLENGE_INDEX.md](CHALLENGE_INDEX.md) | Complete list of all challenges |
| [QUICK_REFERENCE.md](QUICK_REFERENCE.md) | Common commands and shortcuts |
| [EXAMPLES.md](EXAMPLES.md) | Sample solutions and patterns |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | Common issues and fixes |
| [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) | What's been built |
| [ROADMAP.md](ROADMAP.md) | Future plans |

## 🔄 Auto-Grading Submissions

Want solutions to be **automatically graded** when you save or commit? Three powerful options available:

### Option 1: Watch Mode (Real-time)
```bash
# Auto-grade as you save files
python3 grading/watch_and_grade.py
```
Monitors your solution files and runs tests automatically when changes are detected.

### Option 2: Git Pre-Commit Hook
```bash
# Install the pre-commit hook
cp .git/hooks/pre-commit-autograde .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```
Automatically tests your code before each commit and blocks commits if tests fail.

### Option 3: GitHub Actions (CI/CD)
Push your code to GitHub and get automatic grading via GitHub Actions. Tests run on every push and pull request. See `.github/workflows/auto-grade.yml` for configuration.

📖 **[Read the full Auto-Grading Guide →](AUTO_GRADING_QUICKSTART.md)**

## 💡 Use Cases

### 🎯 Personal Skill Assessment
Work through challenges at your own pace, track progress, and identify areas for improvement.

### 📝 Interview Preparation
Practice common coding interview problems (FizzBuzz, array manipulation, string processing) across multiple languages.

### 🔧 Skill Maintenance
Regular practice to stay sharp between jobs or projects. Implement solutions multiple ways to deepen understanding.

### 🎓 Learning New Languages
Use challenges in a familiar language as a reference while learning new syntax and paradigms.

## 📊 Project Statistics

- **30 total challenges** (10 Python, 10 C, 10 Java)
- **50+ test cases** for Python alone
- **30+ individual README files** with problem descriptions
- **Automated grading** with detailed reports
- **Progress tracking** with statistics
- **90+ files created**, 4,000+ lines of code

## 🔮 Future Expansion

This repository currently contains **beginner-level challenges only**. Future levels could include:

- **Intermediate**: Binary search, linked lists, recursion, dynamic programming, hash tables
- **Advanced**: System design, concurrency, memory optimization, API design
- **Master**: Distributed systems, performance optimization, expert algorithms

## 🤝 Contributing

This is a personal learning repository. Feel free to:
- Fork for your own use
- Submit issues for bugs
- Suggest new challenges
- Share your solutions

## �� License

MIT License - Free to use for personal learning and education.

---

## 🚀 Ready to Start?

```bash
# Quick setup
python verify_setup.py && pip install -r requirements.txt

# Start with Python challenge #1
cd beginner/python/01_hello_world && cat README.md

# Or read the getting started guide
cat START_HERE.md
```

**Happy Coding! 🚀**
