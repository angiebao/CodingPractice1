import functools

@functools.lru_cache(maxsize=None)
def f(n):
    if n ==1:
        return 1
    if n==2:
        return 1
    return f(n-1)-f(n-2)

print(f(99))
sum = 0
for i in range(3,100):
    sum += i

print(sum)