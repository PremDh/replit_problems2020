def excel_column_to_number(column):
  lgth = len(column) - 1
  pos = 0
  while lgth >= 0:
    for char in column:
      ch = ord(char) - ord('A') + 1
      pos += (26 ** lgth) * ch
      lgth -= 1
  return pos