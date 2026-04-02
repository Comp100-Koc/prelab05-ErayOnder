def is_palindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True


def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    best = ""
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            sub = s[i:j]
            if len(sub) > len(best) and is_palindrome(sub):
                best = sub
    return best
