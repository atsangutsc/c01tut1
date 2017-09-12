def factorial(n):
  if n == 1:
    return  n
  else:
    return n * factorial(n - 1)

if __name__ == "__main__":
  for i in range(1, 11):
    print factorial(i)

  print "the factorial of %s is %s" % (i,  factorial(i))
