def pycollatz(n):
    """Return the length of the Collatz series for n"""
    slen = 1
    while(n > 1):
        slen+=1
        if (n%2 == 1):
            n = 3*n+1
        else:
            n = n//2
    return slen
import time
from collatz import collatz

n = 10000

dts = []
lens = []
for i in range(1,n+1):
    t0 = time.time()
    a= pycollatz(i)
    dt = time.time()-t0
    dts.append(dt)
    lens.append(a)

dts2 = []
lens2 = []
for i in range(1,n+1):
    t0 = time.time()
    a= collatz(i)
    dt = time.time()-t0
    dts2.append(dt)
    lens2.append(a)




import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(dts,label='Native Python')
plt.plot(dts2, label='Cython')
plt.title('Sequence-length Computation Time')
plt.xlabel('Starting Number')
plt.ylabel('Seconds')
plt.legend(loc='upper right')
plt.savefig('collatz_timing.png')
