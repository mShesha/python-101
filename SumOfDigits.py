print("First ever python code here!")

# Sum of digits using recursion

def sumDigits(n):
    assert n>=0 and int(n)==n, "Positive integers only!"
    if(n ==0):
        return 0
    else:
        return int(n%10) + sumDigits(n/10)

print(sumDigits(35))
