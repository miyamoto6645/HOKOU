a,b = input(),input()

#再帰関数
def gcd_r(a,b):
    if b == 0:
        return a
    else:
        return gcd_r(b, a%b)
print gcd_r(a,b)
