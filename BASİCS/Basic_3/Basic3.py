# 1
is_divisible_by_5 = lambda x: x % 5 == 0


# 2
def print_n_to_1(n):
    if n == 0:
        return
    print(n)
    print_n_to_1(n - 1)


# 3
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)


# 4
def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    seq = fibonacci(n - 1)
    seq.append(seq[-1] + seq[-2])
    return seq


# 5
def flatten_list(lst):
    result = []
    for x in lst:
        if type(x) == list:
            result = result + flatten_list(x)
        else:
            result.append(x)
    return result


# 6
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


# 7
def safe_get(lst, index):
    try:
        return lst[index]
    except:
        return None


# 8
def retry(exception, times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < times:
                try:
                    return func(*args, **kwargs)
                except exception:
                    attempts = attempts + 1
            return None
        return wrapper
    return decorator


# 9
sum_of_digits = lambda n: sum(int(x) for x in str(abs(n)))
