# 🚀 Auto-Grading Quick Start

## Three Ways to Auto-Grade Your Code

### 1️⃣ Watch Mode (Instant Feedback)
```bash
python3 grading/watch_and_grade.py
```
**When to use:** While actively coding  
**What it does:** Tests automatically when you save files

---

### 2️⃣ Pre-Commit Hook (Safety Net)
```bash
# One-time setup
cp .git/hooks/pre-commit-autograde .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

# Then commit as normal
git commit -m "Your message"
```
**When to use:** Before committing code  
**What it does:** Blocks commits if tests fail

---

### 3️⃣ GitHub Actions (Cloud Testing)
```bash
# Just push to GitHub
git push origin main
```
**When to use:** For team projects or submissions  
**What it does:** Tests in the cloud, comments on PRs

---

## Full Documentation

📖 **[AUTO_GRADING_GUIDE.md](AUTO_GRADING_GUIDE.md)** - Complete setup guide  
📋 **[AUTO_GRADING_SUMMARY.md](AUTO_GRADING_SUMMARY.md)** - Technical details

---

## Example Workflow

```bash
# Terminal 1: Start watch mode
python3 grading/watch_and_grade.py

# Terminal 2: Code your solution
cd beginner/python/01_hello_world
vim solution.py
# Edit and save...

# Terminal 1: See results instantly! ✅

# When done, commit (pre-commit hook runs)
git add solution.py
git commit -m "Complete challenge 01"

# Push to GitHub (Actions run)
git push
```

---

## Need Help?

- **Setup issues:** See [AUTO_GRADING_GUIDE.md](AUTO_GRADING_GUIDE.md#troubleshooting)
- **General help:** See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **Quick commands:** See [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
