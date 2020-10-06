def fizzbuzz(n):
    for i in range(1, n+1):
      if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
        continue
      if i % 3 == 0:
        print("fizz")
        continue
      if i % 5 == 0:
        print("buzz")
        continue
      else:
        print(i)

# Please do not modify the code below this line.
# When you run your code, you will need to enter 
# an input in the terminal below, where the prompt appears

test_case = int(input("Please enter an input number:"))
fizzbuzz(test_case)