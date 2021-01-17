# leetcode add string
"1-2-3+4-5"
def calculate(self, exp):
    exps = exp.split("+")
    ""
    res = 0
    for exp in exps:
        new_exp = exp.split('-')
        num = int(new_exp[0])
        for i in range(1,len(new_exp)):
            num -= int(new_exp[i])
        res += num
    return res

