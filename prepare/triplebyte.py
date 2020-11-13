def format(num, sep = ','):
    parts = []
    while num:
        num, mod = divmod(num, 1000)
        parts.append(f'{mod:03}')
    return sep.join(reversed(parts)) or '0'

print( format(1000))
print(format(100000))
print(format(0))
print(format(100))