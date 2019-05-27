"""Поиск подстроки в строке элеметарный"""

def search_substring(s, sub):
    for i in range(0, len(s) - len(sub) + 1):
        if s[i:i+len(sub)] == sub:
            return i
    return -1

print(search_substring("qwerty", "qwerty"))