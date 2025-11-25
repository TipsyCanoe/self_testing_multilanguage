# Jupyter Notebooks for Coding Challenges

This directory contains interactive Jupyter notebooks for working through coding challenges.

## Available Notebooks

### `beginner_python_challenges.ipynb`
Interactive notebook with all 10 beginner Python challenges. Features:
- Self-contained challenges with test cases
- Execution time tracking for each solution
- Instant feedback (✓/✗) on your implementation
- No need to switch between files
- Perfect for learning and experimentation

## How to Use

### 1. Start Jupyter
```bash
# From the project root
jupyter notebook notebooks/
```

Or in VS Code:
- Open the `.ipynb` file
- Select Python kernel
- Click "Run All" or run cells individually

### 2. Work Through Challenges
1. Read the challenge description
2. Replace `pass` with your implementation
3. Run the cell to test your solution
4. See instant results with execution time
5. Move to the next challenge when tests pass

### 3. Track Your Time
Each challenge cell includes timing - see how fast you can solve each one!

```python
✓ All tests passed! (0.15ms)
```

## Advantages of Notebooks

- **Immediate feedback**: Run and test without switching files
- **Iterative development**: Easily modify and re-run solutions
- **Visual learning**: See results inline with markdown explanations
- **Time tracking**: Monitor how long each solution takes
- **Self-contained**: All tests embedded in the notebook

## Tips

- **Save frequently**: Ctrl+S or Cmd+S to save your work
- **Run in order**: Execute cells from top to bottom
- **Restart kernel**: If something breaks, restart and run all cells
- **Compare solutions**: Check `example.py` files for reference implementations

## Next Steps

After completing the beginner notebook:
- Run the full test suite: `python grading/grade_all.py --language python`
- Check your progress: `python grading/view_progress.py`
- Move to intermediate challenges when ready!

## Creating More Notebooks

Want notebooks for other languages (C, Java) or difficulty levels? Request them!
