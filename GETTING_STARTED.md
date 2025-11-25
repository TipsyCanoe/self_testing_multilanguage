# Getting Started Guide

Welcome to your personal coding assessment platform! This guide will help you get started.

## 🎯 What You'll Learn

This repository contains **30 beginner-level challenges** (10 each in C, Java, and Python) covering:

### Python Challenges
1. Hello World - Basic functions
2. Sum Two Numbers - Arithmetic operations
3. Is Even - Conditionals and boolean logic
4. List Sum - List iteration
5. Find Maximum - Comparison logic
6. Count Vowels - String processing
7. Reverse String - String manipulation
8. Character Frequency - Dictionaries
9. FizzBuzz - Classic programming problem
10. Filter Evens - List comprehension

### C Challenges
1. Hello World - Basic I/O
2. Sum Two Numbers - Functions with parameters
3. Is Even - Modulo operator
4. Factorial - Loops and multiplication
5. Array Sum - Array traversal
6. Find Maximum - Array operations
7. String Length - Pointers and strings
8. Reverse Array - In-place modification
9. Count Vowels - String processing
10. Simple Struct - Struct basics and geometry

### Java Challenges
1. Hello World - Methods and return values
2. Sum Two Numbers - Method parameters
3. Is Even - Boolean logic
4. Array Sum - Array operations
5. Find Maximum - Array traversal
6. Count Vowels - String methods
7. Reverse String - StringBuilder
8. ArrayList Basics - Collections
9. Simple Class - OOP fundamentals
10. Exception Handling - Try-catch blocks

## 🚀 Quick Start (5 Minutes)

### Step 1: Install Python Dependencies
```bash
pip install pytest pytest-json-report
```

### Step 2: Try Your First Challenge
```bash
# Navigate to the first Python challenge
cd beginner/python/01_hello_world

# Read the challenge description
cat README.md  # or open README.md in your editor

# Open and edit solution.py
# Implement the hello_world() function

# Run the tests
pytest ../../tests/python/test_01_hello_world.py -v
```

### Step 3: Get Your Grade
```bash
# From the root directory
cd ../../..
python grading/grade_all.py --language python
```

## 📝 Typical Workflow

1. **Choose a challenge** - Start with 01_hello_world
2. **Read the README** - Understand requirements
3. **Implement solution** - Edit the solution file
4. **Run tests** - Verify your implementation
5. **Debug if needed** - Fix failing tests
6. **Move to next** - Progress through challenges

## 🧪 Testing Commands

### Python
```bash
# Test one challenge
pytest tests/python/test_01_hello_world.py -v

# Test all Python challenges
pytest tests/python/ -v

# Get detailed output
pytest tests/python/test_01_hello_world.py -vv
```

### C
```bash
# Compile and run
cd beginner/c/01_hello_world
gcc solution.c -o solution
./solution

# For challenges using math.h
gcc solution.c -o solution -lm
./solution
```

### Java
```bash
# Compile and run
cd beginner/java/01_hello_world
javac Solution.java
java Solution
```

## 📊 Grading System

### View All Grades
```bash
python grading/grade_all.py
```

### View Progress
```bash
python grading/view_progress.py
```

### Grade Options
```bash
# Grade all challenges
python grading/grade_all.py

# Grade specific language
python grading/grade_all.py --language python

# Grade specific challenge
python grading/grade_all.py --challenge beginner/python/01_hello_world

# Save report to file
python grading/grade_all.py --language python --output my_grade.txt
```

## 💡 Tips for Success

### 1. Start Simple
Don't jump ahead. Each challenge builds on previous concepts.

### 2. Read Carefully
The README contains all the information you need, including:
- Requirements
- Function signatures
- Example inputs/outputs
- Skills being tested

### 3. Test Frequently
Run tests after each change to catch errors early.

### 4. Understand the Tests
Look at the test files to understand what's being tested.

### 5. Don't Cheat Yourself
These are for YOUR learning. Don't just look up solutions.

## 🐛 Common Issues

### Import errors in tests
```bash
# Make sure pytest is installed
pip install pytest pytest-json-report
```

### C compilation errors
```bash
# Make sure gcc is installed
gcc --version

# For math functions, use -lm flag
gcc solution.c -o solution -lm
```

### Java compilation errors
```bash
# Make sure Java is installed
java -version
javac -version
```

## 📈 Progress Tracking

Your progress is automatically tracked when you run the grading script. View it anytime:

```bash
python grading/view_progress.py
```

This shows:
- Challenges completed per language
- Average scores
- Recent activity
- Overall progress

## 🎯 What's Next?

After completing all beginner challenges:

1. **Review your weak areas** - Check which topics scored lowest
2. **Redo challenging problems** - Strengthen understanding
3. **Move to Intermediate** - Coming soon!

### Future Levels (To Be Built)

- **Intermediate**: Advanced data structures, algorithms, design patterns
- **Advanced**: System design, optimization, complex problems
- **Master**: Expert-level challenges, real-world scenarios

## 🆘 Need Help?

1. **Read the README** - Most answers are there
2. **Check test files** - See exactly what's being tested
3. **Review examples** - Each README has examples
4. **Debug step by step** - Use print statements

## 🎓 Skills You'll Master

By completing the beginner level, you'll be comfortable with:

**Python:**
- Functions and return values
- Lists and dictionaries
- String manipulation
- List comprehension
- Basic algorithms

**C:**
- Pointers and memory
- Arrays and strings
- Structs
- Function pointers
- Memory management basics

**Java:**
- Object-oriented programming
- Classes and objects
- Collections (ArrayList)
- Exception handling
- Static methods

---

## Ready to Start?

```bash
# Install dependencies
pip install -r requirements.txt

# Start your first challenge
cd beginner/python/01_hello_world
cat README.md

# Good luck! 🚀
```
