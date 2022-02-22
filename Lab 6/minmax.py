import math 
  
def minmax (curDepth, nodeIndex, maxTurn, scores, targetDepth): 
  
    if (curDepth == targetDepth):  #Target Depth reached
        return scores[nodeIndex]
      
    if (maxTurn): 
        return max(minmax(curDepth+1, nodeIndex*2, False, scores, targetDepth), minmax(curDepth+1, nodeIndex*2+1, False, scores, targetDepth)) 
    else: 
        return min(minmax(curDepth+1, nodeIndex*2, True, scores, targetDepth), minmax(curDepth+1, nodeIndex*2+1, True, scores, targetDepth)) 
      
# Driver code 

print("Enter set of values - ")
n=input()
val = list(map(int,n.split()))
  
treeDepth = math.log(len(val), 2) 
  
print("\n\nThe optimal value is - ",minmax(0, 0, True, val, treeDepth)) 
