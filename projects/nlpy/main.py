import re


def stem(word):
    return re.sub(r'(s|ing)$', '', word)


print(stem('working'))
print(stem('works'))
