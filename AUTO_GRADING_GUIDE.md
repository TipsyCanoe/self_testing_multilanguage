# 🔄 Auto-Grading Setup Guide

This guide explains how to set up **automatic grading** for your coding challenge solutions. When enabled, your code will be tested automatically as you work, giving you instant feedback without manually running tests.

## 📋 Table of Contents

1. [Option 1: Watch Mode (Real-time)](#option-1-watch-mode-real-time)
2. [Option 2: Pre-Commit Hook (Git)](#option-2-pre-commit-hook-git)
3. [Option 3: GitHub Actions (CI/CD)](#option-3-github-actions-cicd)
4. [Comparison of Options](#comparison-of-options)
5. [Troubleshooting](#troubleshooting)

---

## Option 1: Watch Mode (Real-time)

**Best for:** Active coding sessions, immediate feedback while learning

### What it does
Monitors your solution files continuously and runs tests automatically whenever you save changes. You get instant feedback as you code!

### Setup

```bash
# Start watch mode from the repository root
python grading/watch_and_grade.py
```

Or with custom check interval (default is 2 seconds):

```bash
python grading/watch_and_grade.py --interval 5
```

### Usage

1. Start the watch script in one terminal
2. Open your solution file in your editor
3. Make changes and save
4. Tests run automatically in the watch terminal
5. See results immediately!

### Example Output

```
======================================================================
          WATCH MODE AUTO-GRADER - STARTED
======================================================================

Monitoring solution files for changes...
Check interval: 2 seconds
Press Ctrl+C to stop

Watching 30 solution files
======================================================================

🔄 Change detected: beginner/python/01_hello_world/solution.py

======================================================================
Testing Python: 01_hello_world
Time: 14:32:45
======================================================================

tests/python/test_01_hello_world.py::test_hello_world PASSED
tests/python/test_01_hello_world.py::test_return_type PASSED
tests/python/test_01_hello_world.py::test_exact_match PASSED

✅ All tests passed for 01_hello_world!
======================================================================
```

### Stopping Watch Mode

Press `Ctrl+C` to stop monitoring.

---

## Option 2: Pre-Commit Hook (Git)

**Best for:** Preventing broken code from being committed, maintaining clean history

### What it does
Automatically tests your solution files **before** each Git commit. If tests fail, the commit is blocked until you fix the issues.

### Setup

```bash
# From repository root
cp .git/hooks/pre-commit-autograde .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

### Usage

```bash
# Stage your changes
git add beginner/python/01_hello_world/solution.py

# Commit (tests run automatically)
git commit -m "Implement hello world solution"
```

If tests pass:
- ✅ Commit proceeds normally
- Code is committed to your repository

If tests fail:
- ❌ Commit is blocked
- You see which tests failed
- Fix the code and try again

### Example Output

```
======================================================================
                   PRE-COMMIT AUTO-GRADING
======================================================================

Testing Python solutions...
-----------------------------------
Testing: beginner/python/01_hello_world/solution.py

tests/python/test_01_hello_world.py::test_hello_world PASSED
tests/python/test_01_hello_world.py::test_return_type PASSED
tests/python/test_01_hello_world.py::test_exact_match PASSED

✅ Tests passed for beginner/python/01_hello_world/solution.py

======================================================================
✅ All tests passed! Proceeding with commit.
======================================================================
```

### Bypassing the Hook (Not Recommended)

If you need to commit without testing:

```bash
git commit --no-verify -m "Work in progress"
```

---

## Option 3: GitHub Actions (CI/CD)

**Best for:** Team projects, public repositories, continuous integration

### What it does
Runs tests automatically when you:
- Push code to GitHub
- Open a pull request
- Update a pull request

Tests run on GitHub's servers, and results appear in the Actions tab and PR comments.

### Setup

The workflow file is already created at `.github/workflows/auto-grade.yml`.

**To enable:**

1. Push your repository to GitHub:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```

2. GitHub Actions will automatically detect the workflow file and start running tests

### Usage

**For direct pushes:**

```bash
# Make changes
vim beginner/python/01_hello_world/solution.py

# Commit and push
git add .
git commit -m "Implement solution"
git push
```

**For pull requests:**

1. Create a new branch: `git checkout -b feature/challenge-01`
2. Make your changes
3. Push: `git push -u origin feature/challenge-01`
4. Open a pull request on GitHub
5. See test results in the PR

### Viewing Results

**Actions Tab:**
- Navigate to your repository on GitHub
- Click "Actions" tab
- See all test runs with pass/fail status

**Pull Request Comments:**
- Test results automatically posted as comments
- See detailed grading report
- Scores for each language

### Example Workflow

The workflow runs three parallel jobs:
1. **Python grading** - All Python challenges
2. **C grading** - All C challenges  
3. **Java grading** - All Java challenges
4. **Overall report** - Combined results

Each job:
- Sets up the required environment
- Installs dependencies
- Runs tests
- Uploads results as artifacts
- Comments on PRs with grades

---

## Comparison of Options

| Feature | Watch Mode | Pre-Commit Hook | GitHub Actions |
|---------|-----------|----------------|----------------|
| **Immediate feedback** | ✅ Instant | ⚠️ On commit | ❌ After push |
| **Requires internet** | ❌ No | ❌ No | ✅ Yes |
| **Blocks bad code** | ❌ No | ✅ Yes | ⚠️ In PRs |
| **Runs automatically** | ✅ Always | ✅ On commit | ✅ On push |
| **Best for** | Learning | Clean history | Teams/CI |
| **Resource usage** | Local CPU | Local CPU | GitHub servers |
| **Setup difficulty** | Easy | Easy | Medium |

### Recommended Combinations

**Solo learner:**
- Watch mode while actively coding
- Pre-commit hook for safety

**Student submitting assignments:**
- Pre-commit hook for validation
- GitHub Actions for submission proof

**Team/collaborative project:**
- All three for maximum coverage
- GitHub Actions as source of truth

---

## Troubleshooting

### Watch Mode Issues

**Script doesn't detect changes:**
```bash
# Increase check interval
python grading/watch_and_grade.py --interval 5
```

**Too many false positives:**
- Check if your editor creates temp files
- These may trigger unnecessary tests

### Pre-Commit Hook Issues

**Hook not running:**
```bash
# Verify it's executable
ls -la .git/hooks/pre-commit
# Should show executable permissions (x)

# Make executable if needed
chmod +x .git/hooks/pre-commit
```

**Hook always fails:**
```bash
# Test manually first
pytest tests/python/test_01_hello_world.py -v

# Check which files are staged
git diff --cached --name-only
```

### GitHub Actions Issues

**Workflow not running:**
- Verify `.github/workflows/auto-grade.yml` exists
- Check Actions tab for errors
- Ensure you pushed to main/master/develop branch

**Tests fail on GitHub but pass locally:**
- Different Python/Java/GCC versions
- Missing dependencies
- File path issues (case sensitivity)

**Workflow syntax error:**
```bash
# Validate YAML locally
python -c "import yaml; yaml.safe_load(open('.github/workflows/auto-grade.yml'))"
```

---

## Advanced Configuration

### Watch Mode - Custom Patterns

Edit `grading/watch_and_grade.py` to watch additional files:

```python
self.watch_patterns = [
    'beginner/python/**/solution.py',
    'beginner/c/**/solution.c',
    'beginner/java/**/Solution.java',
    # Add custom patterns here
]
```

### Pre-Commit Hook - Selective Testing

Edit `.git/hooks/pre-commit` to customize which files are tested or change test verbosity.

### GitHub Actions - Notifications

Add Slack/Discord notifications by adding steps to `.github/workflows/auto-grade.yml`:

```yaml
- name: Notify on failure
  if: failure()
  run: |
    # Add your notification command here
```

---

## Manual Testing vs Auto-Grading

You can always test manually alongside auto-grading:

```bash
# Manual Python test
pytest tests/python/test_01_hello_world.py -v

# Manual C compile and run
cd beginner/c/01_hello_world
gcc solution.c -o solution && ./solution

# Manual Java compile and run
cd beginner/java/01_hello_world
javac Solution.java && java Solution

# Full grading report
python grading/grade_all.py
```

---

## Summary

Choose the auto-grading method that fits your workflow:

1. **Watch Mode** - Best for active learning and immediate feedback
2. **Pre-Commit Hook** - Best for preventing mistakes before committing
3. **GitHub Actions** - Best for team projects and official submissions

Or use all three for comprehensive coverage! 🚀

---

**Questions or issues?** Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md) or open an issue.
