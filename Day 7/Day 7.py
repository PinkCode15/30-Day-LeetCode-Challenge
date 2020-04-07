class Solution:
    def countElements(self, arr: List[int]) -> int:
        arrDict = {}
        counter = 0
        
        for x in arr:
            if x not in arrDict:
                arrDict[x] = 1
            else:
                arrDict[x] += 1

        for x in arrDict:
            if x+1 in arrDict:
                counter += arrDict[x]

        return counter