#!/usr/bin/env python

import argparse
import alg_03_merge_sort
import alg_03_05_binary_search


def sum_search(items, value):
  alg_03_merge_sort.merge_sort(items, 0, len(items) - 1)
  for i in xrange(0, len(items)):
    last_item = items[-i-1]
    index = alg_03_05_binary_search.binary_search(items, value - last_item, 0, len(items) - i - 1)
    if None != index:
      return (items[index], last_item)
  return None


def main():
  commands = argparse.ArgumentParser(description = 'Sum search.')
  commands.add_argument(
      'integers', metavar = 'N', type = int, nargs = '+', help = 'Integers to search.')
  commands.add_argument(
      '--value', metavar = 'v', type = int, help = 'Value to find.')
  arguments = commands.parse_args()
  print(sum_search(arguments.integers, arguments.value))


if '__main__' == __name__:
  main()
