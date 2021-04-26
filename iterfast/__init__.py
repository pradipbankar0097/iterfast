import math
import numpy
def getprimes(upto=1000000):
    if upto<2:
        return numpy.ndarray(0)
    primes=numpy.arange(3,upto+1,2)
    isprime=numpy.ones(int((upto-1)/2),dtype=bool)
    for factor in primes[:int(math.sqrt(upto))]:
        if isprime[int((factor-2)/2)]:
            isprime[int((factor*3-2)/2)::int(factor)]=0
    return numpy.insert(primes[isprime],0,2).copy()
