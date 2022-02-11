"""
Calculation of prime numbers
"""

PRIMES_TO_TEN = [2, 3, 5, 7]


def calculate_primes(start=0, stop=100):
    """
    Calculates all primes from start to end
    :param start: The number to start from
    :param stop: The number to end
    :return: The primes between start and end
    """
    primes = []
    for number in range(start, stop + 1):
        if number in PRIMES_TO_TEN:
            primes.append(number)
            continue
        elif number is 1:
            continue

        is_prime = True
        for divisor in PRIMES_TO_TEN:
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)

    return primes
