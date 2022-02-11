from behave import then, when


@when('i calculate the prime numbers between {start} and {end}')
def step_when_calculate_prime_numbers_between(context, start, end):
    raise NotImplementedError("i calculate the prime numbers between {start} and {end}")


@then(u'the calculated prime numbers should be {calculated_primes}')
def step_then_calculated_prime_numbers_should_be(context, calculated_primes):
    raise NotImplementedError("the calculated prime numbers should be {calculated_primes}")
