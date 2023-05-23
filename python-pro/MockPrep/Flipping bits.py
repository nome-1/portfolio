# 2147483648
def flippingBits(n):
    NEW = []
    a = '{:032b}'.format(n)
    for i, b in enumerate(a):
        if a[i] == "1":
            NEW.append("0")
        else:
            NEW.append("1")
    ans=("".join(NEW))
    return int(ans, 2)


print(flippingBits(2147483647))

#
# for _ in range(input()):
#     s = 2**32 ^ int(raw_input())
#     t = str(bin(s))[2:]
#     t = t.replace('0','2')
#     t = t.replace('1','0')
#     t = t.replace('2','1')
#     print int(t,2)
#
#
#
#
#
#
#