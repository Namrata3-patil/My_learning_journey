from collections import OrderedDict

n = int(input())
word_counts = OrderedDict()

for _ in range(n):
  word = input().strip()
  word_counts[word] = word_counts.get(word, 0) + 1

print(len(word_counts))
print(*(word_counts.values()))

'''
Sample Input

4
bcdef
abcdefg
bcde
bcdef
Sample Output

3
2 1 1
Explanation

There are  distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.
'''
