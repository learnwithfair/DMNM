# Write a Python program to find a real root of the function x^3-2x-5=0 in the range 1<x<3
# using false position method

# Python program for implementation  of false position Method for solving equations
# An example function whose solution is determined using false position Method.
MAX_ITER = 1000000

# The function is x^3 - 2x - 5 = 0
def func( x ):
  return (x * x * x - 2 * x -5)

# Prints root of func(x) with error of EPSILON
def regulaFalsi( a , b):
  if func(a) * func(b) >= 0:
    print("You have not assumed right a and b")
    return
  c = a
  for i in range(MAX_ITER):
    c = (a * func(b) - b * func(a))/ (func(b) - func(a))
    if func(c) == 0:
      break
    # Decide the side to repeat the steps
    if func(c) * func(a) < 0:
      b = c
    else:
      a = c
  # printing result
  print("The value of root is : " , '%.4f' %c)

# Driver code
# Initial values assumed
a =-200
b = 300
# calling function
regulaFalsi(a, b)
