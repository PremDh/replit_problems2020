def fast_trailing_zero_factorial(n):
  n = n // 5
  if n >= 5:
    n += 1
  return n

#print("Enter number")
#n = int(input())
#print("The number of trailing zeroes is " + str(fast_trailing_zero_factorial(n)))