class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        스택쌓기 처럼 구현하려고 했으나 실패
        ㅇ 풀이법
        1) 투 포인터 (투 포인터를 쓰는 문제 풀이가 자주 등장한다.)
        2) 스택
        '''
        # 1) 투 포인터 - 288ms
#         if not height:
#             return 0
        
#         volume = 0
#         left, right = 0, len(height)-1   # 포인터 지정
        
#         left_max, right_max = height[left], height[right]
        
#         while left < right:
#             left_max = max(height[left], left_max)
#             right_max = max(height[right], right_max)
            
#             if left_max <= right_max:
#                 volume += left_max - height[left]
#                 left += 1 # 오른쪽으로 이동
#             else:
#                 volume += right_max - height[right]
#                 right -= 1 # 왼쪽으로 이동
        
#         return volume

        # 2) 스택 - 305ms
        stack = []
        volume = 0
        
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack):
                    break
            
                dist = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
            
                volume += dist * waters
            
            stack.append(i)
        return volume
            
            
            
            
            
            
            