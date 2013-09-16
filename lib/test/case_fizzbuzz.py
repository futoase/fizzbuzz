# -*- coding:utf-8 -*-

import os
import sys

LIB_DIR = os.path.realpath('../')

if not LIB_DIR in sys.path:
  sys.path.insert(0, LIB_DIR)

from fizzbuzz import fizzbuzz

describe "FizzBuzz target toone variable":

  it "should be last valiable is 'FizzBuzz' when given 45":
    assert list(fizzbuzz(45))[-1] == "FizzBuzz"

  it "should be last valiable is 'Fizz' when given 3":
    assert list(fizzbuzz(3))[-1] == "Fizz"

  it "should be last valiable is 'Buzz' when given 5":
    assert list(fizzbuzz(5))[-1] == "Buzz"

  it "should be last valiable is 4 when given 4":
    assert list(fizzbuzz(4))[-1] == "4"

describe "FizzBuzz check of result.":

  let result = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
  it "should be the same list is when given 15":

    assert self.result == list(fizzbuzz(15))
