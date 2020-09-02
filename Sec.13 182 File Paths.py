#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 182. File Paths
# https://docs.python.org/3/library/pathlib.html


from pathlib import Path

p = Path('.')
print(p)

print(p.resolve())

abs_path = p.resolve()

print(abs_path.parts)
