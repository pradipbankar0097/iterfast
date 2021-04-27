"""
iterfast
====

Provides NumPy Arrays
  1. of some commonly used sequences and series 
     eg. A sequence of prime numbers.
  2. in least possible time.
  3. that may take time to achieve manually.

How to use the documentation
----------------------------
Documentation is available in two forms: docstrings provided
with the code, and a loose standing reference guide, available from
`the iterfast homepage <https://https://github.com/pradipbankar0097/iterfast/docs/index.html>`_.

"""

import math
import numpy
def getprimes(upto=1000000):
    """
    Parameters
    ----------
    1. upto : The upper bound for the required sequence of prime numbers.
    
    
    Returns
    -------
    A numpy.ndarray of all prime numbers upto 'upto' inclusive.
    """
    if upto<2:
        return numpy.ndarray(0)
    primes=numpy.arange(3,upto+1,2)
    isprime=numpy.ones(int((upto-1)/2),dtype=bool)
    for factor in primes[:int(math.sqrt(upto))]:
        if isprime[int((factor-2)/2)]:
            isprime[int((factor*3-2)/2)::int(factor)]=0
    return numpy.insert(primes[isprime],0,2).copy()
