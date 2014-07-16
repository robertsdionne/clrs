#!/usr/bin/env python

import argparse
import time


def binary_search(items, value, p, r):
  q = (p + r) / 2
  if p > r:
    return None
  if value == items[q]:
    return q
  elif value < items[q]:
    return binary_search(items, value, p, q - 1)
  else:
    return binary_search(items, value, q + 1, r)


def main():
  commands = argparse.ArgumentParser(description = 'Insertion sort.')
  commands.add_argument(
      'integers', metavar = 'N', type = int, nargs = '+', help = 'Integers to search.')
  commands.add_argument(
      '--value', metavar = 'v', type = int, help = 'Value to find.')
  arguments = commands.parse_args()
  print binary_search(arguments.integers, arguments.value, 0, len(arguments.integers) - 1)


if '__main__' == __name__:
  main()
