#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    int n, maxFreq = 0;
    unordered_map<int, int> freqMap;
    cin >> n;
    for(int i = 0; i < n; i++) {
        int num;
        cin >> num;
        freqMap[num]++;
        maxFreq = max(maxFreq, freqMap[num]);
    }
    cout << maxFreq << endl;
    return 0;
}
