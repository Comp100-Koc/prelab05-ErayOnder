def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    a = a[2:]
    b = b[2:]

    max_len = max(len(a), len(b))
    a = "0" * (max_len - len(a)) + a
    b = "0" * (max_len - len(b)) + b

    carry = 0
    result = ""
    for i in range(max_len - 1, -1, -1):
        total = carry
        if a[i] == "1":
            total += 1
        if b[i] == "1":
            total += 1
        if total == 0:
            result = "0" + result
            carry = 0
        elif total == 1:
            result = "1" + result
            carry = 0
        elif total == 2:
            result = "0" + result
            carry = 1
        else:
            result = "1" + result
            carry = 1

    if carry:
        result = "1" + result

    while len(result) > 1 and result[0] == "0":
        result = result[1:]

    return "0b" + result
