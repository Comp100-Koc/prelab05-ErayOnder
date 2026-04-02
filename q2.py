def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    changed = True
    while changed:
        changed = False
        result = ""
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i] == s[i + 1]:
                changed = True
                i += 2
            else:
                result += s[i]
                i += 1
        s = result
    return s
