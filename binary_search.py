from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the indices of the numbers
        index_map = {}
        
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in index_map:
                # Return the indices of the complement and the current number
                return [index_map[complement], i]
            
            # Store the index of the current number in the dictionary
            index_map[num] = i
        
        # Return an empty list if no solution is found (though the problem guarantees one solution)
        return []

# Create an instance of Solution
solution = Solution()

# Test cases
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(solution.twoSum([3, 3], 6))           # Output: [0, 1]
