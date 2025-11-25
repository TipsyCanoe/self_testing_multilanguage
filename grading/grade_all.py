#!/usr/bin/env python3
"""
Automated Grading System for Coding Challenges
Runs tests and generates grade reports
"""

import os
import sys
import json
import subprocess
import argparse
import time
from datetime import datetime
from pathlib import Path


class GradingSystem:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        self.results = {}
        
    def run_python_tests(self, level="beginner", challenge=None):
        """Run pytest for Python challenges"""
        test_dir = self.root_dir / "tests" / "python"
        
        if challenge:
            # Run specific challenge test
            test_file = test_dir / f"test_{challenge.split('/')[-1]}.py"
            if not test_file.exists():
                print(f"Test file not found: {test_file}")
                return None
            cmd = ["pytest", str(test_file), "-v", "--json-report", "--json-report-file=temp_report.json"]
        else:
            # Run all Python tests
            cmd = ["pytest", str(test_dir), "-v", "--json-report", "--json-report-file=temp_report.json"]
        
        try:
            start_time = time.time()
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.root_dir)
            elapsed_time = time.time() - start_time
            
            # Parse JSON report if it exists
            report_file = self.root_dir / "temp_report.json"
            if report_file.exists():
                with open(report_file, 'r') as f:
                    report_data = json.load(f)
                report_file.unlink()  # Delete temp file
                report_data['elapsed_time'] = elapsed_time
                return report_data
            else:
                # Fallback: parse text output
                result_data = self._parse_pytest_output(result.stdout, result.stderr)
                result_data['elapsed_time'] = elapsed_time
                return result_data
                
        except Exception as e:
            print(f"Error running Python tests: {e}")
            return None
    
    def run_c_tests(self, level="beginner"):
        """Run C tests using the bash script"""
        test_script = self.root_dir / "tests" / "c" / "run_tests.sh"
        
        if not test_script.exists():
            print(f"C test script not found: {test_script}")
            return None
        
        try:
            start_time = time.time()
            result = subprocess.run(
                ["bash", str(test_script)],
                capture_output=True,
                text=True,
                cwd=self.root_dir
            )
            elapsed_time = time.time() - start_time
            
            # Parse the output
            output = result.stdout
            passed = 0
            total = 0
            
            # Extract results from "Results: X/Y passed"
            for line in output.split('\n'):
                if 'Results:' in line and 'passed' in line:
                    # Format: "Results: 10/10 passed (100%)"
                    parts = line.split()
                    if len(parts) >= 2:
                        counts = parts[1].split('/')
                        if len(counts) == 2:
                            passed = int(counts[0])
                            total = int(counts[1])
            
            return {
                'summary': {
                    'passed': passed,
                    'failed': total - passed,
                    'total': total
                },
                'elapsed_time': elapsed_time,
                'output': output
            }
            
        except Exception as e:
            print(f"Error running C tests: {e}")
            return None
    
    def run_java_tests(self, level="beginner"):
        """Run Java tests by compiling and executing"""
        java_dir = self.root_dir / level / "java"
        
        if not java_dir.exists():
            print(f"Java directory not found: {java_dir}")
            return None
        
        try:
            start_time = time.time()
            passed = 0
            failed = 0
            results = []
            
            # Find all Java solution directories
            for challenge_dir in sorted(java_dir.iterdir()):
                if not challenge_dir.is_dir():
                    continue
                
                # Look for Solution.java or Rectangle.java
                solution_files = list(challenge_dir.glob("*.java"))
                solution_files = [f for f in solution_files if f.name not in ['Example.java']]
                
                if not solution_files:
                    continue
                
                challenge_name = challenge_dir.name
                
                # Compile
                compile_result = subprocess.run(
                    ["javac"] + [str(f) for f in solution_files],
                    capture_output=True,
                    text=True,
                    cwd=challenge_dir
                )
                
                if compile_result.returncode != 0:
                    failed += 1
                    results.append({
                        'name': challenge_name,
                        'status': 'FAIL',
                        'reason': 'Compilation error'
                    })
                    # Clean up any .class files
                    for class_file in challenge_dir.glob("*.class"):
                        class_file.unlink()
                    continue
                
                # Run (if has main method)
                main_class = solution_files[0].stem
                run_result = subprocess.run(
                    ["java", main_class],
                    capture_output=True,
                    text=True,
                    cwd=challenge_dir,
                    timeout=5
                )
                
                # Clean up .class files
                for class_file in challenge_dir.glob("*.class"):
                    class_file.unlink()
                
                if run_result.returncode == 0:
                    passed += 1
                    results.append({
                        'name': challenge_name,
                        'status': 'PASS'
                    })
                else:
                    failed += 1
                    results.append({
                        'name': challenge_name,
                        'status': 'FAIL',
                        'reason': 'Runtime error'
                    })
            
            elapsed_time = time.time() - start_time
            total = passed + failed
            
            return {
                'summary': {
                    'passed': passed,
                    'failed': failed,
                    'total': total
                },
                'elapsed_time': elapsed_time,
                'tests': results
            }
            
        except Exception as e:
            print(f"Error running Java tests: {e}")
            return None
    
    def _parse_pytest_output(self, stdout, stderr):
        """Parse pytest text output when JSON report is not available"""
        lines = stdout.split('\n')
        passed = 0
        failed = 0
        
        for line in lines:
            if 'passed' in line.lower():
                # Extract number of passed tests
                parts = line.split()
                for i, part in enumerate(parts):
                    if 'passed' in part and i > 0:
                        try:
                            passed = int(parts[i-1])
                        except:
                            pass
            if 'failed' in line.lower():
                parts = line.split()
                for i, part in enumerate(parts):
                    if 'failed' in part and i > 0:
                        try:
                            failed = int(parts[i-1])
                        except:
                            pass
        
        total = passed + failed
        return {
            'summary': {
                'passed': passed,
                'failed': failed,
                'total': total
            },
            'tests': []
        }
    
    def calculate_grade(self, test_results):
        """Calculate grade based on test results"""
        if not test_results or 'summary' not in test_results:
            return 0, "No tests run"
        
        summary = test_results['summary']
        total = summary.get('total', 0)
        passed = summary.get('passed', 0)
        
        if total == 0:
            return 0, "No tests found"
        
        percentage = (passed / total) * 100
        
        # Grade classification
        if percentage == 100:
            grade = "A+ (Perfect!)"
        elif percentage >= 90:
            grade = "A"
        elif percentage >= 80:
            grade = "B"
        elif percentage >= 70:
            grade = "C"
        elif percentage >= 60:
            grade = "D"
        else:
            grade = "F"
        
        return percentage, grade
    
    def generate_report(self, language, test_results, output_file=None):
        """Generate a detailed grade report"""
        if not test_results:
            print("No test results to report")
            return
        
        percentage, grade = self.calculate_grade(test_results)
        summary = test_results.get('summary', {})
        
        elapsed = test_results.get('elapsed_time', 0)
        
        report = []
        report.append("=" * 70)
        report.append(f"CODING CHALLENGE GRADE REPORT - {language.upper()}")
        report.append("=" * 70)
        report.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Execution Time: {elapsed:.3f} seconds")
        report.append("")
        report.append("SUMMARY:")
        report.append(f"  Total Tests: {summary.get('total', 0)}")
        report.append(f"  Passed: {summary.get('passed', 0)}")
        report.append(f"  Failed: {summary.get('failed', 0)}")
        report.append(f"  Score: {percentage:.1f}%")
        report.append(f"  Grade: {grade}")
        report.append("")
        
        # Detailed results
        if 'tests' in test_results and test_results['tests']:
            report.append("DETAILED RESULTS:")
            report.append("-" * 70)
            for test in test_results['tests']:
                status = "✓ PASS" if test.get('outcome') == 'passed' else "✗ FAIL"
                test_name = test.get('nodeid', 'Unknown test')
                report.append(f"  {status}: {test_name}")
        
        report.append("=" * 70)
        
        report_text = "\n".join(report)
        
        # Print to console
        print(report_text)
        
        # Save to file if specified
        if output_file:
            with open(output_file, 'w') as f:
                f.write(report_text)
            print(f"\nReport saved to: {output_file}")
        
        return report_text
    
    def run_all_languages(self, level="beginner"):
        """Run tests for all languages"""
        results = {}
        
        print("\n" + "=" * 70)
        print(f"Running {level.upper()} level tests for ALL languages...")
        print("=" * 70 + "\n")
        
        # Python tests
        print("Testing Python challenges...")
        python_results = self.run_python_tests(level=level)
        if python_results:
            results['python'] = python_results
            self.generate_report("Python", python_results)
            print()
        
        # C tests
        print("Testing C challenges...")
        c_results = self.run_c_tests(level=level)
        if c_results:
            results['c'] = c_results
            self.generate_report("C", c_results)
            print()
        
        # Java tests
        print("Testing Java challenges...")
        java_results = self.run_java_tests(level=level)
        if java_results:
            results['java'] = java_results
            self.generate_report("Java", java_results)
        
        # Overall summary
        print("\n" + "=" * 70)
        print("OVERALL SUMMARY")
        print("=" * 70)
        for lang, result in results.items():
            summary = result.get('summary', {})
            total = summary.get('total', 0)
            passed = summary.get('passed', 0)
            if total > 0:
                percentage = (passed / total) * 100
                print(f"{lang.upper():10} {passed}/{total} passed ({percentage:.0f}%)")
        print("=" * 70)
        
        return results


def main():
    parser = argparse.ArgumentParser(description="Automated grading system for coding challenges")
    parser.add_argument("--level", default="beginner", help="Difficulty level (beginner, intermediate, advanced, master)")
    parser.add_argument("--language", help="Specific language to test (python, java, c)")
    parser.add_argument("--challenge", help="Specific challenge to test (e.g., 'beginner/python/01_hello_world')")
    parser.add_argument("--output", help="Output file for the report")
    
    args = parser.parse_args()
    
    # Get the root directory (parent of grading directory)
    script_dir = Path(__file__).parent
    root_dir = script_dir.parent
    
    grader = GradingSystem(root_dir)
    
    if args.challenge:
        # Test specific challenge
        print(f"Testing challenge: {args.challenge}")
        parts = args.challenge.split('/')
        if 'python' in parts:
            results = grader.run_python_tests(challenge=args.challenge)
            grader.generate_report("Python", results, args.output)
    elif args.language:
        # Test specific language
        lang = args.language.lower()
        if lang == "python":
            results = grader.run_python_tests(level=args.level)
            grader.generate_report("Python", results, args.output)
        elif lang == "c":
            results = grader.run_c_tests(level=args.level)
            grader.generate_report("C", results, args.output)
        elif lang == "java":
            results = grader.run_java_tests(level=args.level)
            grader.generate_report("Java", results, args.output)
        else:
            print(f"Language '{args.language}' not recognized. Use: python, c, or java")
    else:
        # Test all languages
        grader.run_all_languages(level=args.level)


if __name__ == "__main__":
    main()
