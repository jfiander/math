#!/usr/local/bin/python3
import sys

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
  print(output.encode('utf-8').decode('unicode_escape'))

if __name__ == "__main__":
  colorize_num("".join(sys.argv[1:]))
