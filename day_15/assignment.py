def combinationSum3(k, n):
    results = []

    def backtrack(start, path, target):
        if len(path) == k and target == 0:
            results.append(path[:])  # Store a valid combination
            return
        for i in range(start, 10):  # Numbers from 1 to 9
            if target - i < 0:  # Stop if the sum exceeds n
                break
            path.append(i)
            backtrack(i + 1, path, target - i)  # Recurse with next numbers
            path.pop()  # Backtrack

    backtrack(1, [], n)
    return results

# Example usage
print(combinationSum3(3, 6))  # Output: [[1, 2, 4]]