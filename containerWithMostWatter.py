def maxArea(height:list[int]):
    start = 0
    end = len(height) - 1
    maxArea = 0

    while start != end:
        width = end - start
        minHeight = min(height[start],height[end])

        area = width * minHeight

        if area > maxArea:
            maxArea = area
        

        if height[start] < height[end]:
            start += 1
        else:
            end -= 1

    return maxArea

    




print(maxArea([1,8,6,2,5,4,8,3,7]))