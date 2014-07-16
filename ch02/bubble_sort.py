#!/usr/bin/env python

import argparse


def bubble_sort(items, p, r):
  for i in xrange(p, r + 1):
    for j in xrange(r, i, -1):
      if items[j] < items[j - 1]:
        items[j], items[j - 1] = items[j - 1], items[j]


def main():
  commands = argparse.ArgumentParser(description = 'Bubble sort.')
  commands.add_argument(
      'integers', metavar = 'N', type = int, nargs = '+', help = 'Integers to sort.')
  arguments = commands.parse_args()
  print arguments.integers
  bubble_sort(arguments.integers, 0, len(arguments.integers) - 1)
  print arguments.integers


if '__main__' == __name__:
  main()
