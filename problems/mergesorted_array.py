def merge(nums1:list[int], m:int, nums2:list[int], n:int):
    
    if len(nums1) != m:
      cutList(nums1,m)
    
    if len(nums2) != n:
        cutList(nums2,n)

    for i in nums2:
        nums1.append(i)
    nums1.sort()


    
def cutList(list,size):
    end = len(list) -1
    while end != size-1:
        list.pop()
        end -= 1

        
    



print(merge([1,2,3,0,0,0],3,[2,5,6],3))