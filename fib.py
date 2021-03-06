#!/usr/local/bin/python3
import sys, getopt, math, random

def fibonacci(argv):
  n         = 1
  verbose   = False
  magnitude = False

  if type(argv) is list:
    argument_is_int = False
  else:
    argument_is_int = True
    n = int(argv)

  if not(argument_is_int):
    try:
      opts, args = getopt.getopt(argv, "n:mv")
    except getopt.GetoptError as e:
      print('Invalid option:', e)
      sys.exit(1)

    for opt, arg in opts:
      if opt == '-n':
        n = int(arg)
      elif opt == '-v':
        verbose = True
      elif opt == '-m':
        magnitude = True

  fibonacci = [0, 1]

  if n >= 2:
    for i in range(2, n):
      fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
      if verbose:
        print(str(fibonacci[i-2]) + " + " + str(fibonacci[i-1]) + " = " + str(fibonacci[i]))
  fibonacci[-1]
  if magnitude:
    if verbose:
      print("Magnitude:", math.floor(math.log(fibonacci[-1])))
    else:
      print(math.floor(math.log(fibonacci[-1])))
  else:
    if verbose:
      print("n:", n)
      print("count:", len(fibonacci))
      print('')
      print(fibonacci)
      print('')
      print("fib(" + str(n) + ") = " + str(fibonacci[-1]))
    else:
      return fibonacci[-1]

def fibonacci_chain(cap = "random"):
  steps  = 1
  output = ""
  if cap == "random":
    cap = random.randrange(10, 50)
  while steps < (cap + 1):
    steps += 1
    output = output + str(fibonacci(steps))
  return output

if __name__ == "__main__":
  if sys.argv[1] == "chain":
    if sys.argv[2:] == []:
      print(fibonacci_chain())
    else:
      print(fibonacci_chain(int(sys.argv[2])))
  else:
    print(fibonacci(sys.argv[1:]))
