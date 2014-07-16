#!/usr/bin/env python

import argparse


def decimal_to_binary(decimal):
  binary = []
  while decimal > 0:
    binary.append(decimal % 2)
    decimal /= 2
  return binary


def match_length(a, b):
  arg_min = arg_max = None
  if len(a) > len(b):
    arg_max = a
    arg_min = b
  else:
    arg_max = b
    arg_min = a
  for i in xrange(len(arg_min), len(arg_max)):
    arg_min.append(0)


def binary_to_decimal(binary):
  decimal = 0
  for i in xrange(0, len(binary)):
    decimal += 2**i * binary[i]
  return decimal


def add_binary_ints(a, b):
  assert(len(a) == len(b))
  c = [0] * (len(a) + 1)
  carry = 0
  for i in xrange(0, len(a)):
    sum = a[i] ^ b[i] ^ carry
    carry = a[i] & b[i] | (carry & (a[i] ^ b[i]))
    c[i] = sum
    c[i + 1] = carry
  return c


def main():
  commands = argparse.ArgumentParser(description = 'Binary addition.')
  commands.add_argument('a', type = int, help = 'First integer to add.')
  commands.add_argument('b', type = int, help = 'Second integer to add.')
  arguments = commands.parse_args()
  a = decimal_to_binary(arguments.a)
  b = decimal_to_binary(arguments.b)
  match_length(a, b)
  c = add_binary_ints(a, b)
  print list(reversed(a))
  print list(reversed(b))
  print list(reversed(c))
  print '%s + %s = %s' % (arguments.a, arguments.b, binary_to_decimal(c))


if '__main__' == __name__:
  main()
