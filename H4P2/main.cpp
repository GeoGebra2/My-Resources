#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

struct Node
{
    int data = -1;
    //int left = -1;
    //int right = -1;
    int pathTree = -1;
    int pathNum = -1;
    int haveChecked = 0;
};

void AddPath(vector<vector<Node>>&Forest, int start, int ending, int TreeNum)
{
    //bool haveFind = false;
    //cout << "start: " << start << " end: " << ending << endl;
    int startTree = -1, startNum = -1, endTree = -1, endNum = -1;
    for (int i = 0; i < TreeNum; i++)
    {
        for (int j = 0; j < Forest[i].size(); j++)
        {
            //cout << Forest[i][j].data << endl;
            if (Forest[i][j].data == start)
            {

                startTree = i;
                startNum = j;
            }
            if (Forest[i][j].data == ending)
            {
                endTree = i;
                endNum = j;
            }
            if (startNum != -1 && endNum != -1)
            {
                break;
            }
        }
        if (startNum != -1 && endNum != -1)
        {
            break;
        }
    }
    //cout << startTree << " " << startNum << " " << endTree << " " << endNum << endl;
    Forest[startTree][startNum].pathTree = endTree;
    Forest[startTree][startNum].pathNum = endNum;
    /*
    for (int i = 0; i < TreeNum; i++)
    {
        for (int j = 0; j < Forest[i].size(); j++)
        {
            cout << "Tree: " << i << " num: " << j << " data: " << Forest[i][j].data
            << " have path to: " << Forest[i][j].pathTree << " " << Forest[i][j].pathNum << endl;
        }
    }*/
}

bool CanReach(vector<vector<Node>>&Forest, int target, int StartTree, int StartNum)
{
    //cout << "here is: " << StartTree << StartNum << endl;
    if (StartTree == -1 || StartNum == -1 || Forest[StartTree][StartNum].haveChecked == 1)
    {
        //cout << "none" << endl;
        return false;
    }
    else if (Forest[StartTree][StartNum].data == target)
    {
        //cout << "get" << endl;
        return true;
    }
    else if (StartNum+1 >= (Forest[StartTree].size() + 1) / 2)
    {
        //cout << "leaf" << endl;
        Forest[StartTree][StartNum].haveChecked = 1;
        return CanReach(Forest, target, Forest[StartTree][StartNum].pathTree, Forest[StartTree][StartNum].pathNum);
    }
    else
    {
        //cout << "recurse" << endl;
        Forest[StartTree][StartNum].haveChecked = 1;
        return CanReach(Forest, target, StartTree, 2*StartNum + 1)
        || CanReach(Forest, target, StartTree, 2*StartNum + 2)
        || CanReach(Forest, target, Forest[StartTree][StartNum].pathTree, Forest[StartTree][StartNum].pathNum);

    }

}

void ClearChecked(vector<vector<Node>>&Forest, int TreeNum)
{
    for (int i = 0; i < TreeNum; i++)
    {
        for (int j = 0; j < Forest[i].size(); j++)
        {
            Forest[i][j].haveChecked = 0;
        }
    }
    return;
}

int main()
{
    int TreeNum;
    cin >> TreeNum;
    vector<vector<Node>> Forest(TreeNum);
    for (int i = 0; i < TreeNum; i++)
    {
        int levelNum;
        cin >> levelNum;
        vector<Node> tempTree(pow(2, levelNum)-1);
        for (int j = 0; j < pow(2, levelNum) - 1; j++)
        {
            cin >>tempTree[j].data;
        }
        Forest[i] = tempTree;
    }

    int pathNum;
    cin >> pathNum;
    for (int i = 0; i < pathNum; i++)
    {
        int start, ending;
        cin >> start >> ending;
        AddPath(Forest, start, ending, TreeNum);
    }
/*
    for (int i = 0; i < TreeNum; i++)
    {
        for (int j = 0; j < Forest[i].size(); j++)
        {
            cout << "Tree: " << i << " num: " << j << " data: " << Forest[i][j].data
            << " have path to: " << Forest[i][j].pathTree << " " << Forest[i][j].pathNum << endl;
        }
    }*/

    int CheckNum;
    cin >> CheckNum;
    for (int i = 0; i < CheckNum; i++)
    {
        int target;
        cin >> target;
        if (CanReach(Forest, target, 0, 0))
        {
            cout << "Yes" << endl;
        }
        else
        {
            cout << "No" <<endl;
        }
        ClearChecked(Forest, TreeNum);
    }
    return 0;
}
