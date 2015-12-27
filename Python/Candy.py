"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.

Children with a higher rating get more candies than their neighbors.

What is the minimum candies you must give?

Example
Given ratings = [1, 2], return 3.

Given ratings = [1, 1, 1], return 3.

Given ratings = [1, 2, 2], return 4. ([1,2,1]).
"""

class Solution:
    # @param {int[]} ratings Children's ratings
    # @return {int} the minimum candies you must give
    def candy(self, ratings):
        # Write your code here
        candy = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                candy[i] = candy[i - 1] + 1
        for i in reversed(range(1, len(ratings))):
            if ratings[i - 1] > ratings[i] and candy[i - 1] <= candy[i]:
                candy[i - 1] = candy[i] + 1
        return sum(candy)
