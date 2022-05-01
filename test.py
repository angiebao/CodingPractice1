scores = [1,3,5,10,15]
ages = [1,2,3,4,5]

l = {x: y for x, y in sorted(zip(ages, scores), key=lambda pair: pair[0])}