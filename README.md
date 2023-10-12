# asgmt-3-programming-and-data-analysis-2023

> Assignment 3: Programming and Data Analysis 2023.

Define functions in `asgmt-three.py` with given names and templates then run `test-runner.py`.

## 01. Define a function `sort_list_with_ascending_order()` which sorts a given list with ascending order.

```python
def sort_list_with_ascending_order(x: list) -> list:
    """
    >>> sort_list_with_ascending_order([2, 5, 3])
    [2, 3, 5]
    >>> sort_list_with_ascending_order([2, 5, 3, 11, 7])
    [2, 3, 5, 7, 11]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 02. Define a function `sort_list_with_descending_order()` which sorts a given list with descending order.

```python
def sort_list_with_descending_order(x: list) -> list:
    """
    >>> sort_list_with_descending_order([2, 5, 3])
    [5, 3, 2]
    >>> sort_list_with_descending_order([2, 5, 3, 11, 7])
    [11, 7, 5, 3, 2]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 03. Define a function `return_integer_with_fizz_buzz_rule()` which returns a given integer with Fizz Buzz rule.

Source: <https://en.wikipedia.org/wiki/Fizz_buzz>

```python
def return_integer_with_fizz_buzz_rule(x: int):
    """
    >>> return_integer_with_fizz_buzz_rule(3)
    'Fizz'
    >>> return_integer_with_fizz_buzz_rule(5)
    'Buzz'
    >>> return_integer_with_fizz_buzz_rule(15)
    'Fizz Buzz'
    >>> return_integer_with_fizz_buzz_rule(16)
    16
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 04. Define a function `return_first_n_fizz_buzz()` which returns the first `n` Fizz Buzz integer/string as a `list`.

```python
def return_first_n_fizz_buzz(n: int) -> list:
    """
    >>> return_first_n_fizz_buzz(4)
    [1, 2, 'Fizz', 4]
    >>> return_first_n_fizz_buzz(6)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz']
    >>> return_first_n_fizz_buzz(15)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz']
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 05. Define a function `range_fizz_buzz()` which returns a list of Fizz Buzz integer/string given `start`(inclusive) and `stop`(exclusive).

```python
def range_fizz_buzz(start: int, stop: int) -> list:
    """
    >>> range_fizz_buzz(1, 5)
    [1, 2, 'Fizz', 4]
    >>> range_fizz_buzz(3, 5)
    ['Fizz', 4]
    >>> range_fizz_buzz(1, 6)
    [1, 2, 'Fizz', 4, 'Buzz']
    >>> range_fizz_buzz(3, 6)
    ['Fizz', 4, 'Buzz']
    >>> range_fizz_buzz(1, 16)
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz']
    >>> range_fizz_buzz(13, 16)
    [13, 14, 'Fizz Buzz']
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 06. Define a function `retrieve_middle_elements()` which returns the middle elements of a given list. If there are two middle elements, return both of them in a tuple.

```python
def retrieve_middle_elements(x: list):
    """
    >>> retrieve_middle_elements([2, 3, 5])
    3
    >>> retrieve_middle_elements([2, 3, 5, 7])
    (3, 5)
    >>> retrieve_middle_elements([2, 3, 5, 7, 11])
    5
    >>> retrieve_middle_elements([2, 3, 5, 7, 11, 13])
    (5, 7)
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 07. Define a function `median()` which returns the median value of a given unsorted list. The median value can be calculated as the average of middle elements after sorting the given list in ascending order.

Source: <https://en.wikipedia.org/wiki/Median>

```python
def median(x: list):
    """
    >>> median([2, 3, 5, 7, 11])
    5
    >>> median([2, 3, 5, 7, 11, 13])
    6.0
    >>> median([11, 13, 17, 2, 3, 5, 7])
    7
    >>> median([7, 11, 13, 17, 19, 2, 3, 5])
    9.0
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 08. Define a function `collect_divisors()` which returns all positive divisors of a given integer.

Source: <https://en.wikipedia.org/wiki/Divisor>

```python
def collect_divisors(x: int) -> list:
    """
    >>> collect_divisors(1)
    [1]
    >>> collect_divisors(2)
    [1, 2]
    >>> collect_divisors(3)
    [1, 3]
    >>> collect_divisors(4)
    [1, 2, 4]
    >>> collect_divisors(5)
    [1, 5]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 09. Define a function `is_prime()` which returns whether `x` is a prime number or not.

Source: <https://en.wikipedia.org/wiki/Prime_number>

```python
def is_prime(x: int) -> bool:
    """
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 10. Define a function `filter_primes_within_range()` which returns prime numbers within given `a` and `b` where a < b. Include `a` but exclude `b` in function output if they are prime numbers.

```python
def filter_primes_within_range(a: int, b: int) -> list:
    """
    >>> filter_primes_within_range(1, 5)
    [2, 3]
    >>> filter_primes_within_range(6, 10)
    [7]
    >>> filter_primes_within_range(11, 15)
    [11, 13]
    >>> filter_primes_within_range(16, 20)
    [17, 19]
    >>> filter_primes_within_range(21, 25)
    [23]
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```