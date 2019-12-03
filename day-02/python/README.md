# Day 02 Python Solution #

## Running the tests ##

For day 2, let's add some unit tests to this business!
Using python's `unittest` module, this is very easy.

To run the tests, just call `python3 intcode_lib_test.py`

These tests run through the test cases supplied in the README for part 1 of today's challenge.

There is an additional test for `extract_answer`, a function added for part 2.
This function carries out multiplying the noun by 100 and adding the verb.

## Solving part 1 ##

We just need to get the value in the first position.
The file `part1.py` has the solution for this.

Invoke it with `python3 part1.py` and you should be good to go!

## Solving part 2 ##

Since the range to search over is small, naively iterate through it until a match is found.
Use the `extract_answer` function from `intcode_lib.py` to simplify the code a bit, and add some coverage.

Run the solution for part 2 with `python3 part2.py`
