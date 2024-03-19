from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

    def count_of_airplanes(self, airplanes: List[Interval]) -> int:
        # write your code here
        arr = []
        for airplane in airplanes:
            arr.append((airplane.start, 1))
            arr.append((airplane.end, -1))

        arr.sort()
        count, maxCount = 0, 0

        for idx, cost in arr:
            count += cost
            maxCount = max(count, maxCount)

        return maxCount