#!/usr/bin/env python

import argparse


def horners_rule(items, x):
  y = 0
  for i in xrange(0, len(items)):
    y = items[len(items) - i - 1] + x * y
  return y


def main():
  commands = argparse.ArgumentParser(description = 'Horner\'s rule.')
  commands.add_argument(
      'integers', metavar = 'N', type = float, nargs = '+', help = 'Polynomial coefficients.')
  commands.add_argument(
      '--value', metavar = 'x', type = float, help = 'Value of x.')
  arguments = commands.parse_args()
  print horners_rule(arguments.integers, arguments.value)


if '__main__' == __name__:
  main()
