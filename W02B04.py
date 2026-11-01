import math
import itertools

def no_two_vowels_adjacent(word):
    vowels = set("AEIOUaeiou")
    uniquePerms = set(itertools.permutations(word))
    count = 0

    for perm in uniquePerms:
        adjacent = False
        n = len(perm)
        for i in range(n - 1):
            if perm[i] in vowels and perm[i + 1] in vowels:
                adjacent = True
                break
        if not adjacent:
            count += 1
    return count

print("BANANA:", no_two_vowels_adjacent("BANANA"))
