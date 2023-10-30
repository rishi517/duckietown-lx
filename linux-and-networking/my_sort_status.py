import sys

lines = sys.stdin.readlines()

stripped = [f.strip() for f in lines]

sys.stderr.write("\n".join(sorted(stripped, reverse=True)))