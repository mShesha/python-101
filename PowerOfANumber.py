# power of a given number

def p(num,power,result=1):
    assert power>=0 and int(power) == power ,'Error: the exponent cannot be negative or floating value!'
    if power==0 :
        return result
    else:
        return p(num,power-1,num*result)

print(p(3,3))