Feature: Calculate prime numbers

  @calculate-primes
  Scenario Outline: Calculate primes
      When i calculate the prime numbers between <start> and <end>
      Then the result should be <calculated-primes>

      Examples:
      | start | end  | calculated-primes |
      |  0    |  10  | 2,3,5,7           |