class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        result = len(points)
        points.sort()
        prev_element = points[0]
        for i in range(1,len(points)):
            current_element = points[i]
            if current_element[0] <= prev_element[1]:
                result -=1
                prev_element = [current_element[0], min(current_element[1], prev_element[1])]
            else:
                prev_element = current_element
        return result