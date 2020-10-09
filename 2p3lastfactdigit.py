def last_factorial_digit(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  ldigit = result % 10
  return ldigit