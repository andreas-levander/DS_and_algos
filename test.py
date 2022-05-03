def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1

    return result

print(parity(3))

def test():
    dic1 = {"lol": 1, "xd": 2}
    dic2 = {"xd": 3,"lol": 1}
    print(dic1 == dic2)
    for key, value in dic1.items():
        print(key, value)

test()