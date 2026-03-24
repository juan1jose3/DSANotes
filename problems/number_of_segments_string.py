def countSegments(s:str):
    new_str = s.strip()
    if new_str == "":
        return 0
    segments = new_str.split(" ")
    index = len(segments) - 1
    while index:
        if segments[index] == "":
            segments.remove(segments[index])
        index -= 1


    return len(segments)



print(countSegments(", , , ,        a, eaefa"))