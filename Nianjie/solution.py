class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        if l == 0:
            return 0
        
        left_max = [height[0]]
        for i in range(l-1):
            left_max.append(max(left_max[i], height[i+1]))
        
        right_max = [height[l-1]]
        for i in range(l-2, -1, -1):
            right_max = [max(right_max[0], height[i])] + right_max
            
        result = 0
        for i in range(l):
            result += (min(left_max[i], right_max[i]) - height[i])
        
        return result
