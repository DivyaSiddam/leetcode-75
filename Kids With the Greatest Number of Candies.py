#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        # Find out the greatest number of candies among all the kids.
        maxCandies = max(candies)
        # For each kid, check if they will have greatest number of candies
        # among all the kids.
        result = []
        for i in range(len(candies)):            
            result.append(candies[i] + extraCandies >= maxCandies)
        return result
