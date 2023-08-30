
#include <iostream>
#include <vector>
#include <climits>

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int mProfit = 0;
        int minPrice = INT_MAX;
        for (int i = 0; i < prices.size(); i++) {
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            }
            else if (prices[i] - minPrice > mProfit) {
                mProfit = prices[i] - minPrice;
            }
        }
        return mProfit;
    }
};

int main() {
    Solution s;
    std::vector<int> prices = {7,1,5,3,6,4};
    std::cout << s.maxProfit(prices) << std::endl;
    return 0;
}
