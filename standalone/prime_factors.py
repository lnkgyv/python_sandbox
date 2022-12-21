# Get prime factors of the given number.
# Number is set from argv of script.

import sys

if (len(sys.argv) < 2):
    print("Usage:", sys.argv[0], "<number>")
    sys.exit(None)

if (not sys.argv[1].isnumeric()):
    print("Only number must be passed as argument!")

# is number is prime
def is_prime(number):
    prime = 1

    for num in range(2, number):
        if (number % num == 0):
            prime = 0
            break

    return prime

# form list of prime numbers from 1 to number
def get_primes(number):
    primes = []
    for num in range(1, number+1):
        if (is_prime(num)):
            primes.append(num)

    return primes

# get prime factors
def get_factors(number):
    print(number, ": ", end='')

    if (number <= 3):
        print(number)

        return

    primes = get_primes(number)

    while (not number in primes):
        for idx in range(1, len(primes)):
            if (number % primes[idx] == 0):
                number //= primes[idx]
                print(primes[idx], ' ', end='')
                break
    print(int(number))

primes = get_factors(int(sys.argv[1]))
