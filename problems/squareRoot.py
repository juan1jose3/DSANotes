def mySqrt(x:int):

    
    start = 0
    end = x
    ans = 0
    while end >= start:
        middle = (start + end) // 2

        if middle * middle <= x:
           ans = middle
           start = middle + 1  
        
        elif middle * middle > x:
            end = middle - 1
        

    return ans

print(mySqrt(4))


"""
 The Goal of the Problem

We want the largest integer k such that:

k * k ≤ x


NOT just any k that works — specifically the largest one.

That’s the key.

 What does it mean when mid * mid <= x?

It means:

mid is a valid answer

But maybe there’s a bigger number that also works

Example: x = 20

Try mid = 3
3² = 9 → valid
BUT maybe 4 also works → try bigger.

Try mid = 4
4² = 16 → valid
BUT maybe 5 also works → try bigger.

Try mid = 5
5² = 25 → too big → return to smaller side

So whenever mid² ≤ x:

mid could be the answer, but
we don’t know if there is a better (bigger) valid root yet.

That’s why we don’t return immediately.

Instead, we:

save mid as a candidate

ans = mid


move right to search for a bigger valid root

start = mid + 1

"""