def sumOfDigitsTailRecursion(n,sumDigits=0):
    if(n==0):
        return sumDigits
    else:
        return sumOfDigitsTailRecursion(int(n/10),sumDigits+int(n%10))

print(sumOfDigitsTailRecursion(356))