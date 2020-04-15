def collatz(n):
    """Returns the length of the Collatz series for n"""
    slen = 1
    while(n > 1):
        slen+=1
        if (n%2 == 1):
            n = 3*n+1
        else:
            n = n//2
    return slen


