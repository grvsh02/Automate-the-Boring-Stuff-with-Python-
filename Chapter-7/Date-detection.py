import re

#dd/mm/yyyy

dateRegex = re.compile(
r'^((0[1-9]|1[0-9]|2[0-8])[\/](02))|((0[1-9]|1[0-9]|2[0-9]|3[0-1])[\/](01|0[3-9]|1[0-2]))[\/](1\d\d\d|2\d\d\d)$'
)

s = input()
result = dateRegex.search(s)
print(result)