#!/usr/bin/env python3
"""
Watch Mode Auto-Grader
Monitors solution files for changes and automatically runs tests
"""

import os
import sys
import time
import subprocess
from pathlib import Path
from datetime import datetime
import hashlib


class WatchGrader:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        self.file_hashes = {}
        self.watch_patterns = [
            'beginner/python/**/solution.py',
            'beginner/c/**/solution.c',
            'beginner/java/**/Solution.java'
        ]
        
    def calculate_hash(self, file_path):
        """Calculate MD5 hash of file contents"""
        try:
            with open(file_path, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()
        except:
            return None
    
    def get_watched_files(self):
        """Get all files matching watch patterns"""
        watched_files = []
        
        for pattern in self.watch_patterns:
            for file_path in self.root_dir.glob(pattern):
                if file_path.is_file():
                    watched_files.append(file_path)
        
        return watched_files
    
    def grade_python_challenge(self, solution_file):
        """Grade a Python challenge"""
        challenge_name = solution_file.parent.name
        test_file = self.root_dir / "tests" / "python" / f"test_{challenge_name}.py"
        
        if not test_file.exists():
            print(f"⚠️  No test file found for {challenge_name}")
            return
        
        print(f"\n{'='*70}")
        print(f"Testing Python: {challenge_name}")
        print(f"Time: {datetime.now().strftime('%H:%M:%S')}")
        print(f"{'='*70}")
        
        result = subprocess.run(
            ['pytest', str(test_file), '-v', '--tb=short'],
            capture_output=True,
            text=True,
            cwd=self.root_dir
        )
        
        print(result.stdout)
        if result.returncode == 0:
            print(f"✅ All tests passed for {challenge_name}!")
        else:
            print(f"❌ Some tests failed for {challenge_name}")
        print(f"{'='*70}\n")
    
    def grade_c_challenge(self, solution_file):
        """Grade a C challenge"""
        challenge_name = solution_file.parent.name
        challenge_dir = solution_file.parent
        
        print(f"\n{'='*70}")
        print(f"Testing C: {challenge_name}")
        print(f"Time: {datetime.now().strftime('%H:%M:%S')}")
        print(f"{'='*70}")
        
        # Compile
        output_file = challenge_dir / "solution_test"
        compile_result = subprocess.run(
            ['gcc', str(solution_file), '-o', str(output_file)],
            capture_output=True,
            text=True
        )
        
        if compile_result.returncode != 0:
            print("❌ Compilation failed:")
            print(compile_result.stderr)
            print(f"{'='*70}\n")
            return
        
        print("✅ Compilation successful")
        
        # Run
        run_result = subprocess.run(
            [str(output_file)],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        print("\nOutput:")
        print(run_result.stdout)
        
        # Clean up
        if output_file.exists():
            output_file.unlink()
        
        if run_result.returncode == 0:
            print(f"✅ Program executed successfully")
        else:
            print(f"❌ Program exited with error code {run_result.returncode}")
        
        print(f"{'='*70}\n")
    
    def grade_java_challenge(self, solution_file):
        """Grade a Java challenge"""
        challenge_name = solution_file.parent.name
        challenge_dir = solution_file.parent
        
        print(f"\n{'='*70}")
        print(f"Testing Java: {challenge_name}")
        print(f"Time: {datetime.now().strftime('%H:%M:%S')}")
        print(f"{'='*70}")
        
        # Compile
        compile_result = subprocess.run(
            ['javac', str(solution_file)],
            capture_output=True,
            text=True,
            cwd=challenge_dir
        )
        
        if compile_result.returncode != 0:
            print("❌ Compilation failed:")
            print(compile_result.stderr)
            print(f"{'='*70}\n")
            return
        
        print("✅ Compilation successful")
        
        # Run
        class_name = solution_file.stem
        run_result = subprocess.run(
            ['java', class_name],
            capture_output=True,
            text=True,
            cwd=challenge_dir,
            timeout=5
        )
        
        print("\nOutput:")
        print(run_result.stdout)
        
        # Clean up .class files
        for class_file in challenge_dir.glob("*.class"):
            class_file.unlink()
        
        if run_result.returncode == 0:
            print(f"✅ Program executed successfully")
        else:
            print(f"❌ Program exited with error code {run_result.returncode}")
        
        print(f"{'='*70}\n")
    
    def grade_file(self, file_path):
        """Grade a solution file based on its type"""
        try:
            if file_path.name == 'solution.py':
                self.grade_python_challenge(file_path)
            elif file_path.name == 'solution.c':
                self.grade_c_challenge(file_path)
            elif file_path.name == 'Solution.java':
                self.grade_java_challenge(file_path)
        except Exception as e:
            print(f"Error grading {file_path}: {e}")
    
    def check_for_changes(self):
        """Check watched files for changes"""
        watched_files = self.get_watched_files()
        changes_detected = []
        
        for file_path in watched_files:
            current_hash = self.calculate_hash(file_path)
            
            if current_hash is None:
                continue
            
            # Check if file is new or modified
            if file_path not in self.file_hashes:
                # New file
                self.file_hashes[file_path] = current_hash
                # Don't grade on startup, only on changes
            elif self.file_hashes[file_path] != current_hash:
                # Modified file
                self.file_hashes[file_path] = current_hash
                changes_detected.append(file_path)
        
        return changes_detected
    
    def watch(self, interval=2):
        """Watch for file changes and auto-grade"""
        print("="*70)
        print("          WATCH MODE AUTO-GRADER - STARTED")
        print("="*70)
        print(f"\nMonitoring solution files for changes...")
        print(f"Check interval: {interval} seconds")
        print(f"Press Ctrl+C to stop\n")
        
        # Initialize file hashes
        for file_path in self.get_watched_files():
            self.file_hashes[file_path] = self.calculate_hash(file_path)
        
        print(f"Watching {len(self.file_hashes)} solution files")
        print("="*70 + "\n")
        
        try:
            while True:
                changed_files = self.check_for_changes()
                
                for file_path in changed_files:
                    print(f"🔄 Change detected: {file_path.relative_to(self.root_dir)}")
                    self.grade_file(file_path)
                
                time.sleep(interval)
                
        except KeyboardInterrupt:
            print("\n" + "="*70)
            print("          WATCH MODE AUTO-GRADER - STOPPED")
            print("="*70)


def main():
    # Get the root directory
    script_dir = Path(__file__).parent
    root_dir = script_dir.parent
    
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(
        description="Watch solution files and automatically grade changes"
    )
    parser.add_argument(
        '--interval',
        type=int,
        default=2,
        help='Check interval in seconds (default: 2)'
    )
    
    args = parser.parse_args()
    
    # Start watching
    watcher = WatchGrader(root_dir)
    watcher.watch(interval=args.interval)


if __name__ == "__main__":
    main()
