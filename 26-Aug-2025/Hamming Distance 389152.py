# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution {
public:
    int hammingDistance(int x, int y) {
        int z = x^y;
        int ones = 0;
        while(z>0){
            if(z&1)
            ones++;
            z>>=1;
        }
return ones;
        
    }
};