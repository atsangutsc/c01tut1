def factorial(n):
  if n == 1:
    return  0
  else:
    return n * factorial(n - 1)

if __name__ == "__main__":
  for i in range(1, 11):
    print factorial(i)

  print("I don't know what I'm doing.")
