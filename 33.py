"""Проверка равенства строк"""

def equal_simple(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

print(equal_simple("asdfghjkl;'", "asrfghjkl;'"))