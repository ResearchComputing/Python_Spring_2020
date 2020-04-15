import numpy
import ex1
import time
import matplotlib.pyplot as plt
print (ex1.dotprod.__doc__)

def my_dot_prod(a,b):
    c = numpy.zeros(1,dtype='float64')
    n = len(a)
    for i in range(n):
        c += a[i]*b[i]
    return c

nmax = 2048 #maximum size of array to test
ntest = 5 # number of tests to run for each n

dt_python = []
dt_f2py = []

check2 = numpy.zeros(1,dtype='float64')
for n in range(1,nmax+1):
    a = numpy.arange(1,n+1,dtype='float64') # 'd'
    b = numpy.arange(1,n+1,dtype='float64') # 'd'
    t0 = time.time()

    for i in range(ntest):
	#Try each of these 3 possiblities and compare results
        #check = my_dot_prod(a,b)
        check = numpy.sum(a*b)
        #check = numpy.dot(a,b)

    t1 = time.time()
    dt = (t1-t0)/float(ntest)
    dt_python.append(dt)

for n in range(1,nmax+1):
    a = numpy.arange(1,n+1,dtype='float64') # 'd'
    b = numpy.arange(1,n+1,dtype='float64') # 'd'
    t0 = time.time()
    for i in range(ntest):
        ex1.dotprod(a,b,check2)
    t1 = time.time()
    dt = (t1-t0)/float(ntest)
    dt_f2py.append(dt)

#Print the answer from each method
print('Check:', check, check2)
plt.figure(1)

plt.plot(dt_python,label='Native Python')
plt.plot(dt_f2py, label='F2PY')
plt.xlim([128,nmax])
plt.yscale('log')
plt.xlabel('Array Size')
plt.ylabel('Time (s)')
plt.title('Dot Product Time')
plt.legend(loc='upper left')

plt.savefig('f2py_serial.png')
