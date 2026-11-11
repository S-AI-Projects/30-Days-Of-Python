# Shipping-cost conditionals

This added activity practices `if`/`elif` conditionals. It returns shipping
cost `10` below `50`, `5` from `50` to below `100`, and `0` from `100` onward;
negative totals raise `ValueError`.

| Total input | Expected shipping cost |
| ---: | ---: |
| 49.99 | 10 |
| 50 | 5 |
| 99.99 | 5 |
| 100 | 0 |
| -1 | `ValueError` |

Run the example with `python3 09_Day_Conditionals/applied-labs/r27-t019/example.py`.
The scale check evaluates 4, 40, and 400 local totals once each and reports
the operation count; it uses no timing threshold. Run the tests with:

```sh
python3 -m unittest discover -s 09_Day_Conditionals/applied-labs/r27-t019 -p "test_*.py"
```
