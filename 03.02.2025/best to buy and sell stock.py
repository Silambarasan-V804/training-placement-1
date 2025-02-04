class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Initialize variables for the minimum price and maximum profit
        min_price = float('inf')  # Set initial minimum price to infinity
        max_profit = 0           # Set initial maximum profit to 0

        # Iterate through the list of prices
        for price in prices:
            # Update the minimum price encountered so far
            min_price = min(min_price, price)
            # Calculate the profit if selling at the current price
            profit = price - min_price
            # Update the maximum profit if the current profit is higher
            max_profit = max(max_profit, profit)
        
        return max_profit
