class Solution:
    def getsubstrings(self,s):
        substrings=[]
        for x in range(0,len(s)):
            for y in range(x+1,len(s)+1):
                substrings.append(s[x:y])
        return substrings
    
    def get_binary_codes(self,k):
        combinations = list(map(''.join, itertools.product(['0', '1'], repeat=k)))
        return combinations

    def hasAllCodes(self, s: str, k: int) -> bool:
        # substrings=self.getsubstrings(s)
        binary_codes=self.get_binary_codes(k)
        for x in binary_codes:
            if x not in s:
                return False
        return True
        

        
