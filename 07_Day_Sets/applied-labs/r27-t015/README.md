# Applied lab: compare two student groups

This added activity practices set intersection, difference, and union without
changing or extending the lesson's original numbered exercises.

The local `students.json` fixture is the storage input: group A contains Ana
and Bo; group B contains Bo and Cy. The example injects a storage reader, then
prints deterministic results:

- Both groups (intersection): `{"Bo"}`
- Only the first group (A - B): `{"Ana"}`
- Either group (union): `{"Ana", "Bo", "Cy"}`

Run the example and tests from the repository root:

```sh
python3 07_Day_Sets/applied-labs/r27-t015/example.py
python3 -m unittest discover -s 07_Day_Sets/applied-labs/r27-t015 -p "test_*.py"
```

The tests inject local storage and confirm that two independent reads of the
fixture produce the same complete result.
