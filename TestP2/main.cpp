#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int nodeNum, nullnum;
    cin >> nodeNum;
    //cout << nodeNum;
    /*
    string content;
    getline(cin, content);
    for (int i = 0; i < nodeNum; i++)
    {
        getline(cin, content);
        if (content == "null")
        {
            nullnum += 1;
        }
        else
        {
            nullnum = 0;
        }
        //cout << i << endl;
    }
    //cout << nullnum << endl;
    nodeNum -= nullnum;
    */
    if (nodeNum == 0)
    {
        cout << 0 << endl;
    }
    //cout << nodeNum / 2;
    cout << int(log2(nodeNum)+1) << endl;
    return 0;
}
