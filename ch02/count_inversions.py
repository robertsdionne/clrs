#!/usr/bin/env python

import argparse


def merge_while_counting_inversions(items, p, q, r):
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
  inversions = 0
  i = j = 0
  for k in xrange(p, r + 1):
    if left[i] <= right[j]:
      items[k] = left[i]
      i += 1
    else:
      items[k] = right[j]
      j += 1
      inversions += n1 - i
  return inversions


def count_inversions(items, p, r):
  if p < r:
    q = (p + r) / 2
    return (count_inversions(items, p, q) +
        count_inversions(items, q + 1, r) + merge_while_counting_inversions(items, p, q, r))
  else:
    return 0


def main():
  commands = argparse.ArgumentParser(description = 'Merge sort.')
  commands.add_argument(
      'integers', metavar = 'N', type = int, nargs = '+', help = 'Integers to sort.')
  arguments = commands.parse_args()
  print count_inversions(arguments.integers, 0, len(arguments.integers) - 1), "inversions"


if '__main__' == __name__:
  main()
