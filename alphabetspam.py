s = input()
white = s.count('_') / len(s)
print(white)
lower = len([c for c in s if c.islower()]) / len(s)
print(lower)
upper = len([c for c in s if c.isupper()]) / len(s)
print(upper)
print(1 - white - lower - upper)
