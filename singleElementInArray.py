class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            # Ensure mid is even so we can compare with mid+1
            if mid % 2 == 1:
                mid -= 1
            
            if nums[mid] == nums[mid + 1]:
                # The pair is intact, single element is to the right
                left = mid + 2
            else:
                # The pair is broken, single element is here or to the left
                right = mid
        
        return nums[left]
    
if __name__ == "__main__":
    # Input array with all elements appearing twice except one
    arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]

    # Create an object of Solution class
    obj = Solution()

    # Call the function and store the result
    ans = obj.singleNonDuplicate(arr)

    # Print the result
    print("The single element is:", ans)