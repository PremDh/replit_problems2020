def power_of_three(n):
  if n == 3:
    return True
  if n == 1:
    return True
  while n > 3:
    n /= 3
    if n == 3:
      return True
    if n < 3:
      break
    else:
      continue
  return False
  