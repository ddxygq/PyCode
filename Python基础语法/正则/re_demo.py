import re

p = re.compile('[a-z]+')

print(p.pattern)
result = p.match("abc123abc")

print(result.group())
