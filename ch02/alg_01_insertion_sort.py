#!/usr/bin/env python

import argparse


def insertion_sort(items, p, r):
  for j in xrange(p + 1, r + 1):
    key = items[j]
    i = j
    while i > p and items[i - 1] > key:
      items[i] = items[i - 1]
      i = i - 1
    items[i] = key


def main():
  commands = argparse.ArgumentParser(description = 'Insertion sort.')
  commands.add_argument(
      'integers', metavar = 'N', type = int, nargs = '+', help = 'Integers to sort.')
  arguments = commands.parse_args()
  print arguments.integers
  insertion_sort(arguments.integers, 0, len(arguments.integers) - 1)
  print arguments.integers


if '__main__' == __name__:
  main()
