class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while (low <= high):
            mid = (low + high) // 2
            tempContainer = 0
            tempDays = 1

            for item in weights:
                if mid < tempContainer + item:
                    tempContainer = 0
                    tempDays += 1

                tempContainer += item

            if tempDays > days:
                low = mid + 1
            else:
                high = mid - 1

        return low