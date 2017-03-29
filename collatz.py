#!/usr/local/bin/python3
import sys, getopt, math
from colorize_num import colorize_num

def track(list, item, color=False):
  if item in list:
    if color:
      print(colorize_num(item), '→ Loop detected!')
    else:
      print(str(item), '→ Loop detected!')
    sys.exit()
  list.append(item)
  if len(list) > 100:
    list.pop(0)

def check_collatz(n, tree=False, clean=False, color=False, negative=False, quiet=False):
  steps        = 0
  last_hundred = [n]
  if not(quiet):
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
  try:
    while n > 1:
      while n % 2 == 0:
        if (((n & (n - 1)) == 0) and n != 0):
          power = int(math.log(n, 2))
          if not(quiet):
            print('Power of 2:', n, '('+str(power)+')')
          return steps + power
        n = n // 2
        track(last_hundred, n, color=color)
        steps += 1
        if not(quiet):
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
        track(last_hundred, n, color=color)
        steps += 1
        if not(quiet):
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
  except KeyboardInterrupt:
    if not(quiet):
      print('\033[0m' + 'Exiting.')
    sys.exit(0)

def main(argv):
  try:
    opts, args = getopt.getopt(argv, "n:tcpxq", ["number", "clean", "tree", "color", "negative", "quiet"])
  except getopt.GetoptError as e:
    print('Invalid option:', e)
    sys.exit(1)

  n        = 1
  tree     = False
  clean    = False
  color    = False
  negative = False
  quiet    = False

  for opt, arg in opts:
    if (opt == '-n') or (opt[2:] == 'number'):
      n = int(arg)
      original_n = int(n)
    elif (opt == '-t') or (opt[2:] == 'tree'):
      tree = True
    elif (opt == '-c') or (opt[2:] == 'clean'):
      clean = True
    elif (opt == '-p') or (opt[2:] == 'color'):
      color = True
    elif (opt == '-x') or (opt[2:] == 'negative'):
      negative = True
    elif (opt == '-q') or (opt[2:] == 'quiet'):
      quiet = True

  steps = check_collatz(n, tree=tree, clean=clean, color=color, negative=negative, quiet=quiet)

  if not(quiet):
    print('Reached 1.')
  if negative:
    print('collatz[neg](' + str(original_n) + ') =', steps)
  else:
    print('collatz(' + str(original_n) + ') =', steps)

if __name__ == "__main__":
  main(sys.argv[1:])
