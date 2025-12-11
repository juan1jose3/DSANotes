def strStr(haystack: str , needle:str):
    start = 0
    ocurrence = ""

    """
        this technique is called Sliding Window Technique / Fixed-Size Sliding Window

        we use it whenever you need to examine every possible contiguous block (substring) of a fixed length inside a larger sequence.

        example usage:
            len(haystack) = 5
            len(needle)   = 2

            last_valid_i = 5 - 2 = 3 we give more space to the needle to compare


        when do we use it:
            whenever you're sliding a window and you want to avoid going out of bounds

            Whenever you compare a substring of size len(needle) inside a bigger string, you MUST stop early so your window doesn’t pass the end.

            “I stop when there isn't enough space left for the needle.”




            Why we use len(haystack) - len(needle) + 1

            We want to slide a window of size len(needle) over haystack.
            To avoid going out of bounds, the last valid starting index is:

                last_i = len(haystack) - len(needle)




            Example:

                haystack = "abcde"   → length = 5
                needle   = "de"      → length = 2


                Possible windows:

                i = 0 → "ab"

                i = 1 → "bc"

                i = 2 → "cd"

                i = 3 → "de" ← last valid start

                i = 4 ← “e” (not enough characters for window length 2)



            now about if haystack[i + j] == needle[j]:
                
                start = i
                ocurrence += haystack[i+j]


            i = is where the window starts
            j = allows us to move inside the window 



            Visual example that proves it

                Let’s visualize "hello" with the needle "ll":

                haystack = h  e  l  l  o
                index:    0  1  2  3  4


                Needle = "ll"

                🔹 Case: i = 2 (window starts at index 2)

                Window = "ll" (indices 2 and 3)

                Now try j = 0,1:
                j = 0 → i + j = 2 + 0 = 2
                haystack[2] = 'l'
                needle[0]   = 'l'

                j = 1 → i + j = 2 + 1 = 3
                haystack[3] = 'l'
                needle[1]   = 'l'


                Everything matches → window is correct.



            haystack[i + j]


            we loop j from 0 len(needle)-1, we get the characters inside the window:
    """

    for i in range(len(haystack) - len(needle) + 1):
        
        ocurrence = ""
        for j in range(len(needle)):
           
            if haystack[i + j] == needle[j]:
                
                start = i
                ocurrence += haystack[i+j]


            else:
                start = 0
                break
        if ocurrence == needle:
            return start
            
    
    if ocurrence != needle:
        return -1

    return start
            

            
        


            

       
    


print(strStr("sadbutsad","sad"))

