Question:
https://leetcode.com/problems/non-overlapping-intervals/description/

Sorting by end time is crucial for this problem because it enables the greedy algorithm to make optimal choices by minimizing overlaps. Here's why sorting by end time is better than sorting by start time in this case:

1. End Time Sorting Ensures Maximum Non-Overlapping Intervals
When sorted by end time, the algorithm can make a greedy choice:

Always pick the interval that ends earliest and does not overlap with the previously selected interval.
This leaves the most room for subsequent intervals to fit, minimizing removals.

3. Why Start Time Fails for Overlapping Minimization
Sorting by start time doesn't prioritize intervals that end early. Instead:

It focuses on intervals that start early but may last too long, overlapping with multiple others.
As a result, intervals with longer durations can block opportunities for fitting smaller, non-overlapping intervals.
