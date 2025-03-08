#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
    }

    vector<int> sortedNums = nums;
    sort(sortedNums.begin(), sortedNums.end());

    int counts = 0;
    int index = 0, ones_num = 0;
    while(sortedNums[index] == 0){
        if (nums[index] != 0){
            counts++;
            if (nums[index] == 1){
                ones_num++;
            }
        }
        index++;
    }
    while(sortedNums[index] == 1){
        if (nums[index] != 1){
            if (nums[index] == 2){
                counts++;
            }
            else{
                if (ones_num > 0){
                    ones_num--;
                }
                else{
                    counts++;
                }
            }
        }
        index++;
    }

    cout << counts << endl;
    return 0;
}
