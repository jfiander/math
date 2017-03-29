#!/usr/local/bin/python3
import sys, getopt, math

def colorize_num(n):
  reset     = r'\033[0m'
  underline = r'\033[4m'
  red       = r'\033[31m'
  green     = r'\033[32m'
  yellow    = r'\033[33m'
  blue      = r'\033[34m'
  magenta   = r'\033[35m'
  cyan      = r'\033[36m'
  gray      = r'\033[37m'
  b_red     = r'\033[91m'
  b_green   = r'\033[92m'
  b_yellow  = r'\033[93m'
  output    = ""
  if int(n) < 0:
    negative = True
  else:
    negative = False
  num_list  = list(str(n))
  for num in num_list:
    if num == '1':
      output = output + red + num
    elif num == '2':
      output = output + green + num
    elif num == '3':
      output = output + yellow + num
    elif num == '4':
      output = output + blue + num
    elif num == '5':
      output = output + magenta + num
    elif num == '6':
      output = output + cyan + num
    elif num == '7':
      output = output + b_red + num
    elif num == '8':
      output = output + b_green + num
    elif num == '9':
      output = output + b_yellow + num
    elif num == '0':
      output = output + gray + num
  output = output + reset
  if negative:
    output = "-" + output
  return output.encode('utf-8').decode('unicode_escape')

def check_collatz(n, tree=False, clean=False, color=False, negative=False):
  steps = 0
  if clean:
    if color:
      print(colorize_num(n))
    else:
      print(n)
  else:
    if color:
      print('0 :', colorize_num(n))
    else:
      print('0 :', n)
  while n > 1:
    while n % 2 == 0:
      if (((n & (n - 1)) == 0) and n != 0):
        power = int(math.log(n, 2))
        print('Power of 2:', n, '('+str(power)+')')
        return steps + power
      n = n // 2
      steps += 1
      if tree:
        if clean:
          if color:
            print(colorize_num(n))
          else:
            print(n)
        else:
          if color:
            print(steps, ':', colorize_num(n))
          else:
            print(steps, ':', n)
    if n > 1:
      if negative:
        n = (n * 3) - 1
      else:
        n = (n * 3) + 1
      steps += 1
      if tree:
        if clean:
          if color:
            print(colorize_num(n))
          else:
            print(n)
        else:
          if color:
            print(steps, ':', colorize_num(n))
          else:
            print(steps, ':', n)

def main(argv):
  try:
    opts, args = getopt.getopt(argv, "n:tcpx", ["color", "negative"])
  except getopt.GetoptError as e:
    print('Invalid option:', e)
    sys.exit(1)

  n        = 1
  tree     = False
  clean    = False
  color    = False
  negative = False

  for opt, arg in opts:
    if (opt == '-n') or (opt[2:] == 'number'):
      n = int(arg)
    elif (opt == '-t') or (opt[2:] == 'tree'):
      tree = True
    elif (opt == '-c') or (opt[2:] == 'clean'):
      clean = True
    elif (opt == '-p') or (opt[2:] == 'color'):
      color = True
    elif (opt == '-x') or (opt[2:] == 'negative'):
      negative = True

  steps = check_collatz(n, tree=tree, clean=clean, color=color, negative=negative)

  print('Steps to reach 1:', steps)

if __name__ == "__main__":
  main(sys.argv[1:])
