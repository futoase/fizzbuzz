# -*- coding:utf-8 -*-

import os
import sys

LIB_DIR = os.path.realpath('../')

if not LIB_DIR in sys.path:
  sys.path.insert(0, LIB_DIR)

from fizzbuzz import BizzBuzz

describe "BizzBuzz target toone variable":

  let bizzbuzz = BizzBuzz()

  it "should be last valiable is 'BizzBuzz' when given 45":
    assert list(self.bizzbuzz(45))[-1] == "BizzBuzz"

  it "should be last valiable is 'Bizz' when given 3":
    assert list(self.bizzbuzz(3))[-1] == "Bizz"

  it "should be last valiable is 'Buzz' when given 5":
    assert list(self.bizzbuzz(5))[-1] == "Buzz"

  it "should be last valiable is 4 when given 4":
    assert list(self.bizzbuzz(4))[-1] == "4"

describe "BizzBuzz check of result.":

  let bizzbuzz = BizzBuzz()

  let result = ['1', '2', 'Bizz', '4', 'Buzz', 'Bizz', '7', '8', 'Bizz', 'Buzz', '11', 'Bizz', '13', '14', 'BizzBuzz']
  it "should be the same list is when given 15":

    assert self.result == list(self.bizzbuzz(15))
