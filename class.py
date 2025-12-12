#1-----------------------------------------------------------------------------------

# Custom iterator that walks through multiple sequences one after another
#first_task
class SequenceMerger:
    def __init__(self, *items):
        self.data = items
        self.main_index = 0
        self.sub_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.main_index < len(self.data):
            current_list = self.data[self.main_index]

            if self.sub_index < len(current_list):
                element = current_list[self.sub_index]
                self.sub_index += 1
                return element
            else:
                self.main_index += 1
                self.sub_index = 0

        raise StopIteration


# Usage example
if __name__ == "__main__":
    merged = SequenceMerger([10, 11, 12], [50], [99, 100])
    for num in merged:
        print(num)



#2-----------------------------------------------------------------------------------
# Custom iterator that zips multiple lists together element by element
#second task
class MultiZip:
    def __init__(self, *arrays):
        self.arrays = arrays
        self.pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Stop if any sequence is shorter than the current index
        for lst in self.arrays:
            if self.pos >= len(lst):
                raise StopIteration

        combined = [lst[self.pos] for lst in self.arrays]
        self.pos += 1
        return combined


# Example usage
z = MultiZip([9, 8, 7], ["x", "y"], [100, 200, 300])
for group in z:
    print(group)

#3-----------------------------------------------------------------------------------

# Generator that yields all prime numbers below a given limit

def prime_stream(limit):
    if limit <= 2:
        return
    yield 2

    for number in range(3, limit, 2):
        prime_flag = True
        # Check divisors only up to sqrt of number
        for step in range(3, int(number ** 0.5) + 1, 2):
            if number % step == 0:
                prime_flag = False
                break
        if prime_flag:
            yield number


# Testing function for prime_stream
def check_prime_stream():
    # Values <= 2 produce no primes
    assert list(prime_stream(0)) == []
    assert list(prime_stream(2)) == []

    # Small range checks
    assert list(prime_stream(4)) == [2, 3]
    assert list(prime_stream(6)) == [2, 3, 5]

    # Medium range
    assert list(prime_stream(15)) == [2, 3, 5, 7, 11, 13]
    assert list(prime_stream(40)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    # Edge / final prime below the limit
    result = list(prime_stream(100))
    assert result[-1] == 97

    print("All tests completed successfully!")


# Run tests
check_prime_stream()



#4-----------------------------------------------------------------------------------

# Function that produces all combinations of size 'r' from a given list

def pick_combos(items, r):
    if r == 0:
        yield tuple()
        return

    if not items or r > len(items):
        return

    for idx in range(len(items)):
        chosen = items[idx]
        rest = items[idx + 1:]

        for sub in pick_combos(rest, r - 1):
            yield (chosen,) + sub


# Tests for pick_combos
def check_pick_combos():
    # Basic scenarios
    assert list(pick_combos([4, 5, 6], 2)) == [(4, 5), (4, 6), (5, 6)]

    # r = 1
    assert list(pick_combos(["a", "b", "c"], 1)) == [("a",), ("b",), ("c",)]

    # r equals size
    assert list(pick_combos(["x", "y", "z"], 3)) == [("x", "y", "z")]

    # r too large
    assert list(pick_combos([1], 3)) == []

    # empty list
    assert list(pick_combos([], 2)) == []

    # r = 0
    assert list(pick_combos(["q", "w", "e"], 0)) == [()]

    # single item tests
    assert list(pick_combos([99], 1)) == [(99,)]
    assert list(pick_combos([99], 2)) == []

    # exactly length 2
    assert list(pick_combos([7, 8], 2)) == [(7, 8)]

    print("All combination tests succeeded!")


check_pick_combos()



#5-----------------------------------------------------------------------------------
# Implement multi-dimensional array iterator (without additional list creation)



def flatten_iterate(arr):
    for item in arr:
        if isinstance(item, list):
            yield from flatten_iterate(item)
        else:
            yield item



nums = [4, [5], 3, [2]]
print(list(flatten_iterate(nums)))


