def roman_to_decimal(roman_numeral):
  val = 0
  cur = 0
  prev = 0
  for i in roman_numeral:
    st = i
    if st == 'I':
      cur = 1
      if prev < cur:
        val += (cur - (2*prev))
        prev = cur
      else:
        val += cur
        prev = cur
    elif st == 'V':
      cur = 5
      if prev < cur:
        val += (cur - (2*prev))
        prev = cur
      else:
        val += cur
        prev = cur
    elif st == 'X':
      cur = 10
      if prev < cur:
        val += (cur - (2*prev))
        prev = cur
      else:
        val += cur
        prev = cur
    elif st == 'L':
      cur = 50
      if prev < cur:
        val += (cur - (2*prev))
        prev = cur
      else:
        val += cur
        prev = cur
    elif st == 'C':
      cur = 100
      if prev < cur:
        val += (cur - (2*prev))
        prev = cur
      else:
        val += cur
        prev = cur
    elif st == 'D':
      cur = 500
      if prev < cur:
        val += (cur - (2*prev))
        prev = cur
      else:
        val += cur
        prev = cur
    elif st == 'M':
      cur = 1000
      if prev < cur:
        val += (cur - (2*prev))
        prev = cur
      else:
        val += cur
        prev = cur
  return val

print(roman_to_decimal("IL"))
