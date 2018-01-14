from math import log

n = 10001

def primes(n):
	primes = []
	sieve = [True] * (n + 1)
	for p in range(2, n + 1):
		if sieve[p]:
			primes.append(p)
			for i in range(p * p, n + 1, p):
				sieve[i] = False
	return primes

def nth_prime(n):
	max = int(n*(log(n) + log(log(n))))
	return(primes(max)[n+2])

print(nth_prime(10001))
