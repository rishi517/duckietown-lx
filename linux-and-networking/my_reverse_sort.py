import sys

lines = sys.stdin.readlines()

sorted_lines = sorted(lines, reverse=True)

for line in sorted_lines:
    print(line, end='')