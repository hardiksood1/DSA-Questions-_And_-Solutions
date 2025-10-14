# Wildcard Matching using Dynamic Programming

def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    
    # Create DP table of size (m+1) x (n+1)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Empty string matches empty pattern
    dp[0][0] = True
    
    # Only '*' can match empty string
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            else:
                dp[i][j] = False
    
    return dp[m][n]

# ----------------------------
# Example Usage / Test Cases
# ----------------------------
if __name__ == "__main__":
    print("Wildcard Matching Test Cases:\n")
    
    test_cases = [
        ("aa", "a"),        # False
        ("aa", "*"),        # True
        ("cb", "?a"),       # False
        ("adceb", "*a*b"),  # True
        ("acdcb", "a*c?b")  # False
    ]
    
    for s, p in test_cases:
        result = isMatch(s, p)
        print(f"isMatch('{s}', '{p}') = {result}")
    
    # Optional: User Input
    print("\nTry your own input:")
    s_input = input("Enter string s: ")
    p_input = input("Enter pattern p: ")
    print(f"Result: {isMatch(s_input, p_input)}")


# output
# Wildcard Matching Test Cases:

# isMatch('aa', 'a') = False       
# isMatch('aa', '*') = True        
# isMatch('cb', '?a') = False      
# isMatch('adceb', '*a*b') = True  
# isMatch('acdcb', 'a*c?b') = False

# Try your own input:
# Enter string s: hardik
# Enter pattern p: abc
# Result: False