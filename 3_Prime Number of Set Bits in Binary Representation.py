class Solution:
    def checkPrimesetbits(self,number):
        i=bin(number)
        c=0
        for x in i:
            if x=='1':
                c=c+1
        # Prime check
        if c < 2:
            return False

        for y in range(2, int(c**0.5) + 1):
            if c % y == 0:
                return False

        return True

    def countPrimeSetBits(self, left: int, right: int) -> int:
        c=0
        for x in range(left,right+1):
            x=self.checkPrimesetbits(x)
            if x==True:
                c=c+1
        return c


        
