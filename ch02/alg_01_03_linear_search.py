#!/usr/bin/env python

import argparse


def linear_search(items, value):
  for i in xrange(0, len(items)):
    if value == items[i]:
      return i
  return None


def main():
  commands = argparse.ArgumentParser(description = 'Insertion sort.')
  commands.add_argument(
      'integers', metavar = 'N', type = int, nargs = '+', help = 'Integers to search.')
  commands.add_argument(
      '--value', metavar = 'v', type = int, help = 'Value to find.')
  arguments = commands.parse_args()
  print linear_search(arguments.integers, arguments.value)


if '__main__' == __name__:
  main()
