#!/usr/bin/env python

import argparse
import insertion_sort
import merge_sort


def merge_insertion_sort(k, items, p, r):
  if k > r - p:
    insertion_sort.insertion_sort(items, p, r)
  else:
    q = (p + r) / 2
    merge_insertion_sort(k, items, p, q)
    merge_insertion_sort(k, items, q + 1, r)
    merge_sort.merge(items, p, q, r)


def main():
  commands = argparse.ArgumentParser(description = 'Merge sort.')
  commands.add_argument(
      'integers', metavar = 'N', type = int, nargs = '+', help = 'Integers to sort.')
  commands.add_argument(
    '--k', type = int, default = 16, help = 'Threshold for invoking insertion sort.')
  arguments = commands.parse_args()
  print arguments.integers
  merge_insertion_sort(arguments.k, arguments.integers, 0, len(arguments.integers) - 1)
  print arguments.integers


if '__main__' == __name__:
  main()
