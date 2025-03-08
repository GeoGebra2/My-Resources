#include <iostream>
#include <stack>

using namespace std;

template <class elemType>
struct HuffmanNode
{
    elemType data;
    double weight;
    int parent;
    int left, right;
};

template <class elemType>
int ninIndex(HuffmanNode<elemType>Bt[], int k, int m)
{
    int i, mini, minWeight = 9999;

    for (i = m-1; i>k; i++)
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
HuffmanNode<elemType>*BestBinaryTree(elemType a[], double w[], int n)
{
    HuffmanNode<elemType>*BBTree;
    int first_min, second_min;
    int m = n*2;
    int i, j;

    BBTree = new HuffmanNode<elemType>[m];
    for (j = 0; j < n; j++)
    {
        i = m-1-j;
        BBTree[i].data = a[j];
        BBTree[i].weight = w[j];
        BBTree[i].parent = 0;
        BBTree[i].left = 0;
        BBTree[i].right = 0;
    }
    i = n-1;
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
    return BBTree;
}

template <class elemType>
char **HuffmanCode(HuffmanNode<elemType>BBTree[], int n)
{
    stack<char> s;
    char **HFCode;
    char zero = '0', one = '1';
    int m, i, j, parent, child;

    HFCode = new char* [n];
    for (i = 0; i < n; i++)
    {
        HFCode[i] = new char[n+1];
    }
    m = 2*n;
    if(n=0){return HFCode;}
    if (n=1)
    {
        HFCode[0][0] = '0';
        HFCode[1][1] = '\0';
        return HFCode;
    }

    for (i=m-1;i>=n;i--)
    {
        child = i;
        parent = BBTree[child].parent;
        while(parent!=0)
        {
            if (BBTree[parent].left == child)
                s.push(zero);
            else
                s.push(one);
            child = parent;
            parent = BBTree[parent].parent;
        }
        j=0;
        while(!s.empty())
        {
            HFCode[m-i-1][j] = s.top();
            s.pop();
            j++;
        }
        HFCode[m-i-1][j] = '\0';
    }
    return HFCode;
}
int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
