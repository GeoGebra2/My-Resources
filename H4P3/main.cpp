#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
using namespace std;

template <class elemType>
struct HuffmanNode
{
    //elemType data;
    int weight;
    int parent;
    int left, right;
    int level = 0;
};

template <class elemType>
int minIndex(HuffmanNode<elemType>Bt[], int k, int m)
{
    int i, mini, minWeight = 9999;

    for (i = m-1; i>k; i--)
    {
        if ((Bt[i].parent == 0)&&(Bt[i].weight < minWeight))
        {
            mini = i;
            minWeight = Bt[mini].weight;
        }
    }
    return mini;
}

template <class elemType>
int Calculate(HuffmanNode<elemType>BBTree[], int root, int length)
{
    if (BBTree[root].left == 0 && BBTree[root].right == 0)
    {
        return BBTree[root].weight*length;
    }
    else
    {
        return Calculate(BBTree, BBTree[root].left, length+1) + Calculate(BBTree, BBTree[root].right, length+1);
    }
}

int main()
{
    int WordNum;
    cin >> WordNum;
    //int data[WordNum];
    int weight[WordNum];
    for (int i = 0; i < WordNum; i++)
    {
        cin >> weight[i];
    }
    HuffmanNode<int> *BBTree;
    int first_min, second_min;
    int m = WordNum*2;
    int i, j;
    BBTree = new HuffmanNode<int>[m];
    for (j = 0; j < WordNum; j++)
    {
        i = m-1-j;
        //BBTree[i].data = a[j];
        BBTree[i].weight = weight[j];
        BBTree[i].parent = 0;
        BBTree[i].left = 0;
        BBTree[i].right = 0;
    }
    i = WordNum-1;
    while(i!=0)
    {
        first_min = minIndex(BBTree,i,m);
        BBTree[first_min].parent = i;
        second_min = minIndex(BBTree, i, m);
        BBTree[second_min].parent = i;
        BBTree[i].weight = BBTree[first_min].weight + BBTree[second_min].weight;
        BBTree[i].parent = 0;
        BBTree[i].left = first_min;
        BBTree[i].right = second_min;
        i--;
    }
    cout << Calculate(BBTree, 1, 0) << endl;
    return 0;
}
