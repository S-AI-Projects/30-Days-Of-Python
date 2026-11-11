# R27-T020: Even-number squares

Build a dictionary mapping each even integer in an input list to its square. The
list-comprehension filter excludes odd integers, and the input list is unchanged.

```python
[-2, -1, 0, 1, 2]  # {-2: 4, 0: 0, 2: 4}
[-3, -1, 1, 3]     # {}
```

Run the example with `python3 example.py`. From the repository root, run its
tests with:

```sh
python3 -m unittest discover -s 13_Day_List_comprehension/applied-labs/r27-t020 -p "test_*.py"
```

The test for the even-number mapping is specifically sensitive to the filter:
changing `number % 2 == 0` to `number % 2 != 0` makes it fail.
