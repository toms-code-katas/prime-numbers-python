from behave import then, when
from primes.calculate_primes import calculate_primes, InvalidRangeException


@when('i calculate the prime numbers between {start} and {end}')
def step_when_calculate_prime_numbers_between(context, start, end):
    try:
        context.actual_calculated_primes = calculate_primes(int(start), int(end))
    except InvalidRangeException as e:
        context.exception = e


@then(u'the calculated prime numbers should be {calculated_primes}')
def step_then_calculated_prime_numbers_should_be(context, calculated_primes):
    if calculated_primes == "Exception":
        assert isinstance(context.exception, InvalidRangeException)
    else:
        expected_calculated_primes = list(map(int, calculated_primes.split(",")))
        assert expected_calculated_primes == context.actual_calculated_primes
