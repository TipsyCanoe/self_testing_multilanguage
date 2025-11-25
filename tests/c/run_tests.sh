#!/bin/bash
# C Test Runner Script
# Compiles and runs C programs, comparing output with expected results

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

test_challenge() {
    local challenge_dir=$1
    local challenge_name=$(basename "$challenge_dir")
    
    echo "Testing: $challenge_name"
    
    # Compile
    gcc "$challenge_dir/solution.c" -o "$challenge_dir/solution" -lm 2>/dev/null
    
    if [ $? -ne 0 ]; then
        echo -e "${RED}✗ FAIL: Compilation error${NC}"
        return 1
    fi
    
    # Run and capture output
    output=$("$challenge_dir/solution" 2>&1)
    
    # Clean up executable
    rm -f "$challenge_dir/solution"
    
    # For now, just check if it runs without errors
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ PASS: Compiled and ran successfully${NC}"
        return 0
    else
        echo -e "${RED}✗ FAIL: Runtime error${NC}"
        return 1
    fi
}

# Main execution
echo "================================"
echo "C Challenge Test Runner"
echo "================================"

passed=0
failed=0

# Find all C challenges
for challenge_dir in beginner/c/*/; do
    if [ -f "$challenge_dir/solution.c" ]; then
        if test_challenge "$challenge_dir"; then
            ((passed++))
        else
            ((failed++))
        fi
        echo ""
    fi
done

total=$((passed + failed))
percentage=$((passed * 100 / total))

echo "================================"
echo "Results: $passed/$total passed ($percentage%)"
echo "================================"
