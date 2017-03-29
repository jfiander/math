#!/usr/local/bin/python3
import sys, getopt, math, re

def pretty_collatz(string):
  output = ""
  for line in string.split("\n"):
    output = output + re.sub(r'0+\d$', '', line) + "\n"
  return output

if __name__ == "__main__":
  pretty_collatz(sys.argv[1:])
