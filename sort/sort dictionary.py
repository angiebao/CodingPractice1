d = {'a':1,'c':2,'e':5,'b':2,'d':4}
a = sorted(d.items(), key=lambda x: (x[1], x[0]))
b=  sorted(d.items(), key=lambda x: x[1])
print(a)
print(b)