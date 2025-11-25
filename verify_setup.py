#!/usr/bin/env python3
"""
Quick test script to verify the setup is working correctly
"""

import sys
import subprocess
from pathlib import Path


def test_python():
    """Test Python setup"""
    print("Testing Python setup...")
    try:
        result = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
        print(f"✓ Python version: {result.stdout.strip()}")
        return True
    except Exception as e:
        print(f"✗ Python test failed: {e}")
        return False


def test_pytest():
    """Test pytest installation"""
    print("\nTesting pytest installation...")
    try:
        result = subprocess.run(["pytest", "--version"], capture_output=True, text=True)
        print(f"✓ {result.stdout.strip()}")
        return True
    except Exception as e:
        print(f"✗ pytest not found. Install with: pip install pytest pytest-json-report")
        return False


def test_gcc():
    """Test GCC installation"""
    print("\nTesting GCC installation...")
    try:
        result = subprocess.run(["gcc", "--version"], capture_output=True, text=True)
        version_line = result.stdout.split('\n')[0]
        print(f"✓ {version_line}")
        return True
    except Exception as e:
        print(f"✗ GCC not found. Please install GCC.")
        return False


def test_java():
    """Test Java installation"""
    print("\nTesting Java installation...")
    try:
        result = subprocess.run(["java", "-version"], capture_output=True, text=True)
        # Java outputs to stderr
        version_line = (result.stderr or result.stdout).split('\n')[0]
        print(f"✓ {version_line}")
        return True
    except Exception as e:
        print(f"✗ Java not found. Please install Java JDK.")
        return False


def check_structure():
    """Check directory structure"""
    print("\nChecking directory structure...")
    root = Path(__file__).parent
    
    required_dirs = [
        "beginner/python",
        "beginner/c",
        "beginner/java",
        "tests/python",
        "grading"
    ]
    
    all_exist = True
    for dir_path in required_dirs:
        full_path = root / dir_path
        if full_path.exists():
            print(f"✓ {dir_path}")
        else:
            print(f"✗ {dir_path} not found")
            all_exist = False
    
    return all_exist


def main():
    print("=" * 70)
    print("CODING ASSESSMENT PLATFORM - SETUP VERIFICATION")
    print("=" * 70)
    
    tests = [
        ("Python", test_python()),
        ("pytest", test_pytest()),
        ("GCC (C compiler)", test_gcc()),
        ("Java", test_java()),
        ("Directory Structure", check_structure())
    ]
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    passed = sum(1 for _, result in tests if result)
    total = len(tests)
    
    for name, result in tests:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {name}")
    
    print(f"\nTotal: {passed}/{total} checks passed")
    
    if passed == total:
        print("\n🎉 All checks passed! You're ready to start coding.")
        print("\nNext steps:")
        print("  1. Read GETTING_STARTED.md")
        print("  2. cd beginner/python/01_hello_world")
        print("  3. Start solving challenges!")
    else:
        print("\n⚠️  Some checks failed. Please install missing dependencies.")
        print("\nTo install Python dependencies:")
        print("  pip install -r requirements.txt")
    
    print("=" * 70)


if __name__ == "__main__":
    main()
