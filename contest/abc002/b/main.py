import re
s = input()
print(re.sub(r'[aiueo]', "", s))