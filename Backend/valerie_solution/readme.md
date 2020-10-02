# Backend Questions for Magic

These are responses to the backend interview question for Magic.

## Part 4

### Description:
Flatten array of arbitrarily nested arrays of integers into flat array of integers

Ex [[1,2,[3]],4] -> [1,2,3,4]

### To run:

python flatten_array.py


Runs the following test cases:

- assert flatten_array([[1, 2, [3]], 4]) == [1, 2, 3, 4]
- assert flatten_array([[[]]]) == []
- assert flatten_array([]) == []
- assert flatten_array([67, [0, 7, 9], [444, 0, 3], 4, 6, [8], 9]) == [67, 0, 7, 9, 444, 0, 3, 4, 6, 8, 9]
- assert flatten_array([-1, [99], [-99, [0, 7], -5]]) == [-1, 99, -99, 0, 7, -5]


## Part 5

[Question & Description](https://github.com/magiclabs/email_screening_question/tree/master/Backend) 

### Main (Solution)

Solutions to all three questions are returned in a dictionary.

Keyword arguments:

  - --start_date/ -s (required, date range start, float format, ex. 2000.123)
  - --end_date/ -e (required, date range end, float format, ex. 2000.123)
  - --debug (optional, to print debug info)
  - --test_data (optional, uses small number of tests rows in place of data.csv, for development)

Example input for date range 2000.123 through 2000.345:

  - python main.py -s 2000.123 -e 2000.345


### Test

If you do not have pytest installed:
  - pip install pytest


  - pytest main_test.py
