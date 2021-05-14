## Problem
Thank you for taking the time out of your day to tackle this problems set with us! We expect the solution to be
written in **Python**, if you choose to use libraries to help you accomplish the task at hand,
we ask that you leave plenty room in your work to showcase your **algorithms**, and **design** skillsets.

We expect each candidate to spend no more than 2 hours on the solution (we'll take your
word for it 😇). As there are multiple parts to the question, do not feel the need to complete it
all, instead please feel free to stop once you've crossed the two hour mark. If you were in
the midst of a question, feel free to leave some pseudocode for how you would've completed it.

You'll find the dataset for the questions in `data.csv` after unzipping `data.csv.zip`. The dataset
represents temperatures reported by specific weather stations (`station_id`) at a particular point
in time (`date`). The first 4 digits of the `date` value represents the year that the temperature was
collected, the second 3 digit portion appearing after the `.` represents a unique point during the
year such that no two days within the year has the same 3 digit representation.


**Part 1**:

Create a function that when called returns the `station_id`, and `date` pair that reported the
lowest temperature. If a tie occurs simply return one pair at random.

**Part 2**:

Create a function that returns the `station_id` that experienced the most amount of temperature
fluctuation across all dates that it reported temperatures for. For example with the following dataset:

    station_id,     date, temperature_c
             1, 2000.001,             5
             1, 2000.123,             0
             1, 2000.456,             5

we are expecting the total fluctuation to be 10 degrees, as opposed to 0 which is the net difference
in temperature between the first and last dates.

**Part 3**:

Create a function that will return the `station_id` that experienced the most amount of temperature
fluctuation for any given range of dates. I.e to get the result of 10 degrees from part 2 above, we
would expect the input dates to be `2000.001` and `2000.456`.

## Evaluation Criteria
We will be evaluating your submission based on the following criteria, in no particular order:

* Readability: Consistent styling, aptly named functions, and variables.
* Coherent Design: Where applicable, sensisble abstractions are employed, functions are well intentioned.
* Test coverage: The solution is tested, and proveably functions correctly.
* Correctness

In other words, the end product should be something that you wouldn't hesitate to hit shippit on and
productionize!
