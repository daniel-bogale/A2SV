n = int(input())
s = input()

from collections import Counter

letter_counts = Counter(s)

num_zeros = letter_counts['z'] 
num_ones = letter_counts['n']   

result = ['1'] * num_ones + ['0'] * num_zeros
print(' '.join(result))
