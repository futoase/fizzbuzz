# -*- coding:utf-8 -*-

from .fizzbuzz_abs import FizzBuzzAbstract

class BizzBuzz(FizzBuzzAbstract):
  def __call__(self, n):
    for i in range(1, n+1):
      yield (('Bizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0)) or str(i))
