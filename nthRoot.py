class Solution:
    # Function to find N-th root of M using binary search
    def nthRoot(self, n, m):
        # Set left and high for binary search
        left, right = 1, m

        # Start binary search
        while left <= right:
            
            mid = (left + right) // 2

            
            ans = 1
            for _ in range(n):
                ans *= mid
                if ans > m:
                    break

           
            if ans == m:
                return mid

            
            if ans < m:
                left = mid + 1

            
            else:
                right = mid - 1

        # Return -1 if not found
        return -1

obj = Solution()
result = obj.nthRoot(3, 27)