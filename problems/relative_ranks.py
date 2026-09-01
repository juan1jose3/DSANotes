def findRelativeRanks(scores):
    reversed_scores = sorted(scores, reverse=True)
    ans = []
    for i in range(len(scores)):
        for j in range(len(reversed_scores)):
            if scores[i] == reversed_scores[j]:
                if j == 0:
                    ans.append("Gold Medal")
                elif j == 1:
                    ans.append("Silver Medal")
                elif j == 2:
                    ans.append("Bronze Medal")
                else:
                    ans.append(str(j+1))    

    return ans 




    


score_list = [10,3,8,9,4]

print(findRelativeRanks(score_list))