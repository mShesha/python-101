# recursive function to convert decimal to binary

def decimaltobinary(decimal,binary=''):
    assert int(decimal) == decimal, 'the number should be an integer'
    if decimal==0: return binary
    else: return decimaltobinary(int(decimal/2),str(decimal%2)+binary)

print(decimaltobinary(13))