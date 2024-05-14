# Write a Python program to find the value of y when x=10 from following table using Lagrange’s interpolation formula for unequal intervals……………………..….. 33 - 35
# x:	5	6	9	11
# y:	12	13	14	16


# Created class
class Data:
  # Initialized Constructor
  def __init__(self, x, y):
    self.x = x
    self.y = y

def interpolate(f: list, xi: int, n: int) -> float:
  result = 0.0
  for i in range(n):
    term = f[i].y
    for j in range(n):
      if j != i:
        term = term * (xi - f[j].x) / (f[i].x - f[j].x)
    result += term

  return result

if __name__ == "__main__":
  f = [Data(5, 12), Data(6, 13), Data(9, 14), Data(11, 16)]
  # printing result
  print("Value of f(10) is :", interpolate(f, 10, len(f)))
