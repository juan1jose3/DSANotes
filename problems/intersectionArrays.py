def intersection(nums1:list[int],nums2:list[int]):
    setNums1 = set(nums1)
    setNums2 = set(nums2)

    ans = []
    for i in setNums1:
        if i in setNums2:
            ans.append(i)
    return ans




print(intersection([4,9,5],[9,4,9,8,4]))