def isIsomorphic(s, t):
    chr_map = {}
    seen = set()
    for i in range(len(s)):
        if s[i] not in chr_map and t[i] not in seen:
                chr_map[s[i]] = t[i]
                seen.add(t[i])

    new_str = ""
    for j in s:
        if j in chr_map:
            new_str += chr_map[j]
    return new_str == t
    

print(isIsomorphic("paper" , "title"))