#!/usr/bin/env python

import argparse


def selection_sort(items):
  for j in xrange(0, len(items) - 1):
    min = items[j]
    argmin = j
    for i in xrange(j + 1, len(items)):
      if items[i] < min:
        min = items[i]
        argmin = i
    temp = items[j]
    items[j] = min
    items[argmin] = temp


def main():
  commands = argparse.ArgumentParser(description = 'Selection sort.')
  commands.add_argument(
      'integers', metavar = 'N', type = int, nargs = '+', help = 'Integers to sort.')
  arguments = commands.parse_args()
  print arguments.integers
  selection_sort(arguments.integers)
  print arguments.integers


if '__main__' == __name__:
  main()
