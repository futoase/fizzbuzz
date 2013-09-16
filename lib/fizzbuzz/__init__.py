__name__ = "PyFizzBuzz"
__version__ = "0.0.1"
__description__ = "FizzBuzz cli tool"
__author__ = "Keiji Matsuzaki"
__author_email__ = "futoase@gmail.com"
__license__ = "MIT License"
__url__ = "https://github.com/futoase/fizzbuzz"
__classifiers__ = [
  "Programming Language :: Python :: 3.2",
  "Programming Language :: Python :: 3.3",
  "License :: OSI Approved :: MIT License"
]

def fizzbuzz(n=100):
  for i in range(1, n+1):
    yield (('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0)) or str(i))
