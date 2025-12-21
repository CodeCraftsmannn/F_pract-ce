# 1
class chain_sequences:
    def __init__(self, *sequences):
        self.sequences = sequences
        self.seq_index = 0
        self.item_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.seq_index < len(self.sequences):
            current = self.sequences[self.seq_index]
            if self.item_index < len(current):
                val = current[self.item_index]
                self.item_index += 1
                return val
            else:
                self.seq_index += 1
                self.item_index = 0
        raise StopIteration


# 2
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        val = self.data[self.index]
        self.index += 1
        return val


# 3
class zip_sequences:
    def __init__(self, *sequences):
        self.sequences = sequences
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = []
        for seq in self.sequences:
            if self.index >= len(seq):
                raise StopIteration
            result.append(seq[self.index])
        self.index += 1
        return result


# 4
def generate_primes(n):
    for num in range(1, n):
        if num < 2:
            yield num
            continue

        is_prime = True
        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            yield num


# 5
def generate_combinations(sequence, k):
    if k == 0:
        yield ()
        return
    if len(sequence) < k:
        return

    for i in range(len(sequence)):
        first = sequence[i]
        rest = sequence[i + 1:]
        for comb in generate_combinations(rest, k - 1):
            yield (first,) + comb


# 6
def flatten_iterate(data):
    for x in data:
        if type(x) == list:
            for y in flatten_iterate(x):
                yield y
        else:
            yield x
