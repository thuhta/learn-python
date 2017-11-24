s = int(input("input your number: "))
def fac_num(s):
    if s <0:
        print ("s must be a positive number, input your number again")
    elif s==0:
        return 1
    else:
        return s*fac_num(s-1)
print fac_num(s)




