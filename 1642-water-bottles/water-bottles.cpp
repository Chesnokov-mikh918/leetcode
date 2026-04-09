class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int rest = 0;
        int num_start;
        int count = numBottles;
        while ((numBottles + rest) >= numExchange) {
            num_start = numBottles;
            numBottles /= numExchange;
            rest += (num_start - (numBottles * numExchange));
            if ((rest / numExchange) != 0) {
                numBottles += (rest / numExchange);
                rest -= ((rest / numExchange) * numExchange);
            }
            count += numBottles;
        }
        return count;
    }
};