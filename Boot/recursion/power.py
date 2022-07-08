
def power(base, exp):
    assert exp >= 0 and int(exp) == int , "Power can't be negative"
    if exp == 0:
        return 1

    if exp == 1:
        return base

    return base * power(base, exp-1)

print(power(-1,4))
print(power(2,4))
print(power(2,-1))