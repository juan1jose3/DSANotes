from collections import Counter
# find better approach
def intersect(nums1: list[int], nums2: list[int]):
    common = []
    dict1 = Counter(nums1)
    dict2 = Counter(nums2)
    
    
    for key, value in dict1.items():
        if key in dict2:
            dict2_values = dict2[key]
            values_to_insert = 0
            if dict2_values <= value:
                values_to_insert = dict2_values
            elif value <= dict2_values:
                values_to_insert = value
            for i in range(values_to_insert):
                common.append(key)
                
    
    return common
        
    


print(intersect([1,2,2,1], [2]))