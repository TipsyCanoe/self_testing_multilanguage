#!/usr/bin/env python3
"""
Progress Tracker for Coding Challenges
Displays your progress across all levels and languages
"""

import os
import json
from pathlib import Path
from datetime import datetime


class ProgressTracker:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        self.progress_file = self.root_dir / "grading" / "progress.json"
        self.load_progress()
    
    def load_progress(self):
        """Load progress from file"""
        if self.progress_file.exists():
            with open(self.progress_file, 'r') as f:
                self.progress = json.load(f)
        else:
            self.progress = {
                'beginner': {'c': {}, 'java': {}, 'python': {}},
                'intermediate': {'c': {}, 'java': {}, 'python': {}},
                'advanced': {'c': {}, 'java': {}, 'python': {}},
                'master': {'c': {}, 'java': {}, 'python': {}}
            }
    
    def save_progress(self):
        """Save progress to file"""
        self.progress_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.progress_file, 'w') as f:
            json.dump(self.progress, f, indent=2)
    
    def update_challenge(self, level, language, challenge_name, passed, total, grade):
        """Update progress for a specific challenge"""
        if level not in self.progress:
            self.progress[level] = {}
        if language not in self.progress[level]:
            self.progress[level][language] = {}
        
        self.progress[level][language][challenge_name] = {
            'passed': passed,
            'total': total,
            'percentage': (passed / total * 100) if total > 0 else 0,
            'grade': grade,
            'timestamp': datetime.now().isoformat()
        }
        self.save_progress()
    
    def get_summary(self):
        """Get overall progress summary"""
        summary = {}
        
        for level in self.progress:
            summary[level] = {}
            for language in self.progress[level]:
                challenges = self.progress[level][language]
                if challenges:
                    total_challenges = len(challenges)
                    completed = sum(1 for c in challenges.values() if c['percentage'] == 100)
                    avg_score = sum(c['percentage'] for c in challenges.values()) / total_challenges
                    
                    summary[level][language] = {
                        'total': total_challenges,
                        'completed': completed,
                        'avg_score': avg_score
                    }
        
        return summary
    
    def display_progress(self):
        """Display progress in a nice format"""
        print("\n" + "=" * 70)
        print("CODING CHALLENGE PROGRESS TRACKER")
        print("=" * 70 + "\n")
        
        summary = self.get_summary()
        
        for level in ['beginner', 'intermediate', 'advanced', 'master']:
            if level in summary and any(summary[level].values()):
                print(f"\n{level.upper()} Level:")
                print("-" * 70)
                
                for language in ['python', 'java', 'c']:
                    if language in summary[level]:
                        stats = summary[level][language]
                        print(f"  {language.capitalize():10s}: "
                              f"{stats['completed']}/{stats['total']} completed | "
                              f"Average Score: {stats['avg_score']:.1f}%")
        
        # Recent activity
        print("\n" + "=" * 70)
        print("RECENT ACTIVITY:")
        print("-" * 70)
        
        recent = []
        for level in self.progress:
            for language in self.progress[level]:
                for challenge, data in self.progress[level][language].items():
                    recent.append({
                        'level': level,
                        'language': language,
                        'challenge': challenge,
                        'grade': data['grade'],
                        'score': data['percentage'],
                        'timestamp': data['timestamp']
                    })
        
        # Sort by timestamp (most recent first)
        recent.sort(key=lambda x: x['timestamp'], reverse=True)
        
        for i, item in enumerate(recent[:10]):  # Show last 10
            print(f"  {item['timestamp'][:19]} | "
                  f"{item['level']:12s} | "
                  f"{item['language']:7s} | "
                  f"{item['challenge']:20s} | "
                  f"Grade: {item['grade']:3s} ({item['score']:.0f}%)")
        
        print("\n" + "=" * 70)


def main():
    script_dir = Path(__file__).parent
    root_dir = script_dir.parent
    
    tracker = ProgressTracker(root_dir)
    tracker.display_progress()


if __name__ == "__main__":
    main()
