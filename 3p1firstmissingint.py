def first_missing_positive_integer(integers):
  max = 1
  for i in integers:
    if i > max:
      max = i
  if max == 1:
    return max
  for j in range(1, max):
    if j in integers:
      continue
    else:
      return j
  return max + 1
  
  
print(first_missing_positive_integer([1, 2, 0]))