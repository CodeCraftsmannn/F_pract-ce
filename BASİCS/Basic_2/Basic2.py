# 1
def find_min_max(lst):
    min_val = lst[0]
    max_val = lst[0]

    for x in lst:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x

    return min_val, max_val


# 2
def unique_letters(s):
    result = ""
    for ch in s:
        if ch not in result:
            result = result + ch
    return result


# 3
def reverse_list(lst):
    new_list = []
    i = len(lst) - 1
    while i >= 0:
        new_list.append(lst[i])
        i = i - 1
    return new_list


# 4
def revert_dict(d):
    new_d = {}
    for k in d:
        v = d[k]
        new_d[v] = k
    return new_d


# 5
def my_dict_update(d1, d2):
    for k in d2:
        d1[k] = d2[k]
    return d1


# 6
def strings_longer_than_5(lst):
    result = []
    for s in lst:
        if len(s) > 5 and s not in result:
            result.append(s)
    return result


# 7
def most_frequent_letter(text):
    counts = {}

    for ch in text:
        if ch.isalpha():
            ch = ch.lower()
            if ch not in counts:
                counts[ch] = 1
            else:
                counts[ch] = counts[ch] + 1

    max_char = None
    max_count = 0

    for k in counts:
        if counts[k] > max_count:
            max_count = counts[k]
            max_char = k

    return max_char


# 8
def group_anagrams(words):
    groups = {}

    for w in words:
        key = "".join(sorted(w))
        if key not in groups:
            groups[key] = [w]
        else:
            groups[key].append(w)

    result = []
    for k in groups:
        result.append(groups[k])

    return result


# 9
def factorial_sum(n):
    memo = {0: 1, 1: 1}

    def fact(x):
        if x in memo:
            return memo[x]
        memo[x] = x * fact(x - 1)
        return memo[x]

    total = 0
    i = 1
    while i <= n:
        total = total + fact(i)
        i = i + 1

    return total


# 10
def check_vowels_in_columns(matrix):
    vowels = "aeiouAEIOU"
    n = len(matrix)

    for col in range(n):
        count = 0
        for row in range(n):
            if len(matrix[row][col]) > 0 and matrix[row][col][0] in vowels:
                count = count + 1
        if count > 2:
            return False

    return True
