# 1
def max_of_three(a, b, c):
    biggest = a
    if b > biggest:
        biggest = b
    if c > biggest:
        biggest = c
    return biggest


# 2
def sum_of_digits(n):
    if n < 0:
        n = -n
    total = 0
    for i in str(n):
        total = total + int(i)
    return total


# 3
def multiplication_table(n):
    i = 1
    while i <= 10:
        print(n, "x", i, "=", n * i)
        i = i + 1


# 4
def is_valid_time(time_str):
    parts = time_str.split(":")
    if len(parts) != 3:
        return False

    h = int(parts[0])
    m = int(parts[1])
    s = int(parts[2])

    if h < 0 or h > 23:
        return False
    if m < 0 or m > 59:
        return False
    if s < 0 or s > 59:
        return False

    return True


# 5
def is_point_inside_circle(radius, x, y):
    dist = x*x + y*y
    if dist <= radius*radius:
        return True
    else:
        return False


# 6
def binary_to_decimal(binary_str):
    result = 0
    power = 0
    for digit in binary_str[::-1]:
        if digit == '1':
            result = result + (2 ** power)
        power = power + 1
    return result


# 7
def decimal_to_binary(n):
    if n == 0:
        return "0"

    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary


# 8
def expanded_form(n):
    s = str(n)
    length = len(s)
    result = ""

    for i in range(length):
        if s[i] != '0':
            result = result + s[i] + "0" * (length - i - 1) + " + "

    return result[:-3]


# 9
def levenshtein_distance(a, b):
    dp = []

    for i in range(len(a) + 1):
        row = []
        for j in range(len(b) + 1):
            row.append(0)
        dp.append(row)

    for i in range(len(a) + 1):
        dp[i][0] = i
    for j in range(len(b) + 1):
        dp[0][j] = j

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                cost = 0
            else:
                cost = 1

            dp[i][j] = min(
                dp[i-1][j] + 1,
                dp[i][j-1] + 1,
                dp[i-1][j-1] + cost
            )

    return dp[len(a)][len(b)]
