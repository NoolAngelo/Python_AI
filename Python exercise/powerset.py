from itertools import chain, combinations

def power_set(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

# Example usage
set_example = {3, 8, 9, 2}
for subset in power_set(set_example):
    print(subset)
