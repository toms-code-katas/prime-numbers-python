"""
Calculation of prime numbers
"""

PRIMES_TO_TEN = [2, 3, 5, 7]


class InvalidRangeException(Exception):
    pass


def calculate_primes(start=0, stop=100):
    """
    Calculates all primes from start to end
    :param start: The number to start from
    :param stop: The number to end
    :return: The primes between start and end
    """

    if start < 0 or stop < 0:
        raise InvalidRangeException()

    primes = []
    for number in range(start, stop + 1):
        if number in PRIMES_TO_TEN:
            primes.append(number)
        elif number == 1:
            continue

        is_prime = True
        for divisor in PRIMES_TO_TEN:
            if number % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)

    return primes
