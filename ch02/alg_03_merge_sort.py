#!/usr/bin/env python

import argparse


def merge(items, p, q, r):
  n1 = q - p + 1
  n2 = r - q
  left = []
  right = []
  for i in xrange(0, n1):
    left.append(items[p + i])
  for j in xrange(0, n2):
    right.append(items[q + j + 1])
  left.append(float("inf"))
  right.append(float("inf"))
  i = j = 0
  for k in xrange(p, r + 1):
    if left[i] <= right[j]:
      items[k] = left[i]
      i += 1
    else:
      items[k] = right[j]
      j += 1


def merge_sort(items, p, r):
  if p < r:
    q = (p + r) / 2
    merge_sort(items, p, q)
    merge_sort(items, q + 1, r)
    merge(items, p, q, r)


def main():
  commands = argparse.ArgumentParser(description = 'Merge sort.')
  commands.add_argument(
      'integers', metavar = 'N', type = int, nargs = '+', help = 'Integers to sort.')
  arguments = commands.parse_args()
  print arguments.integers
  merge_sort(arguments.integers, 0, len(arguments.integers) - 1)
  print arguments.integers


if '__main__' == __name__:
  main()
