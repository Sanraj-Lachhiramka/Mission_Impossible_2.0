// Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.


class Solution {
public:
    bool hasAlternatingBits(int n) {
        int prev=n%2;
        n=n/2;
        while(n>0){
            int curr=n%2;
            if (curr==prev){
                return false;
            }
            n=n/2;
            prev=curr;
        }
        return true;
    }
};
