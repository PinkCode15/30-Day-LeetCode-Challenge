class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        result = []
        
        for x in range(len(strs)):
            sortString = ''.join(sorted(strs[x]))
            if sortString in anagramDict:
                anagramDict[sortString].append(strs[x])
            else:
                anagramDict[sortString] = [strs[x]]
        
        for y in anagramDict.values():
            result.append(y)
            
        return result

# Another solution
        anagramDict = {}
        result = []
        sortString = []
        
        for x in strs:
            sortString.append(''.join(sorted(x)))
            
        for x in range(len(sortString)):
            if sortString[x] in anagramDict:
                anagramDict[sortString[x]].append(strs[x])
            else:
                anagramDict[sortString[x]] = [strs[x]]
        
        for y in anagramDict.values():
            result.append(y)
            
        return result
            