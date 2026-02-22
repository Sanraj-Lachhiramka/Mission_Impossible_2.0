class Solution:
    def binaryGap(self, n: int) -> int:
        x=bin(n)
        m=0
        for y in range(0,len(x)):
            c=0
            if x[y]=="1":
                for z in range(y+1,len(x)):
                    if x[z]=="1":
                        c=z-y
                        break
            if m<c:
                m=c
        return m
