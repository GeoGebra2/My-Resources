#include <iostream>
#include <stack>
#include <queue>
#include <list>
#include <cmath>
using namespace std;

struct TestPair
{
    int a;
    int b;
};

class BTree;

class Node
{
    friend class BTree;
public:
    int data, left, right, parent;
    int flag;
    int level;
    Node(){data = -1;left = -1;right = -1;parent = -1;flag = 0;level = 1;};
    Node(const int &e, int L = -1, int R = -1, int P = -1, int l = 1)
    {
        data = e;
        left = L;
        right = R;
        parent = P;
        flag = 0;
        level = l;
    };
};

class BTree
{
private:
    Node tree[1000];
    void PreOrder(int t);
    //int CheckMate(Node<elemType>*t, elemType a, elemType b);
    //void DelTree();
public:
    BTree(){};
    void PreOrder();
    void createTree();
    void DelTree();
    int CheckMate(int a, int b);
    int GetIndex(int a);
};

void BTree::createTree()
{
    //Node<elemType> *p, *pl, *pr;
    int i = 0, j = 0;
    //cout << "start" << endl;
    while (true)
    {
        //cout << "round: " << j << endl;
        int temp;
        cin >> temp;
        if (j == 0)
        {
            //p = new Node<elemType>(temp);
            //root = p;
            tree[0].data = temp;
            i = 0;
            j++;
        }
        else
        {
            //cout << "else" << endl;
            if (temp == -1){tree[i].flag++;}
            else
            {
                if (tree[i].flag == 0)
                {
                    //pl = new Node<elemType>(temp, nullptr, nullptr, p, (p->level + 1));
                    //p->left = pl;
                    //p->flag++;
                    //p = pl;
                    //cout << "here" << endl;
                    tree[j].data = temp;
                    tree[j].parent = i;
                    tree[j].level = tree[i].level + 1;
                    tree[i].left = j;
                    tree[i].flag++;
                    i = j;
                    j++;
                }
                else if (tree[i].flag == 1)
                {
                    //pr = new Node<elemType>(temp, nullptr, nullptr, p, (p->level + 1));
                    //p->right = pr;
                    //p->flag++;
                    //p = pr;
                    //cout << "right"  << endl;
                    tree[j].data = temp;
                    tree[j].parent = i;
                    tree[j].level = tree[i].level + 1;
                    tree[i].right = j;
                    tree[i].flag++;
                    i = j;
                    j++;
                }
                else
                {
                    cout << "wrong" << endl;
                    break;
                }

            }
            while (tree[i].flag == 2 && tree[i].parent != -1)
            {
                i = tree[i].parent;
            }
            if (i == 0 && tree[0].flag == 2)
            {
                break;
            }
            /*
            for (int k = 0; k < 1000; k++)
            {
                if (tree[k].data != -1)
                {
                    cout << tree[k].data << " " << tree[k].flag << endl;
                }
                else
                {
                    break;
                }
            }*/
        }
    }

}

void BTree::PreOrder(int i)
{

    if (tree[i].data == -1) {return;}
    cout << tree[i].data << " ";
    PreOrder(tree[i].left);
    PreOrder(tree[i].right);

}

int BTree::GetIndex(int a)
{
    for (int j = 0; j < 1000; j++)
    {
        if (tree[j].data != -1)
        {
            if (tree[j].data == a)
            {
                return j;
            }
        }
        else
        {
            break;
        }
    }
    return -1;
}

void BTree::PreOrder()
{
    for (int i = 0; i < 1000; i++)
    {
        if (tree[i].data != -1)
        {
            cout << "data: " << tree[i].data << " left: " << tree[i].left << " right: " << tree[i].right << " parent: " << tree[i].parent << "level: " << tree[i].level << endl;
        }
    }
}

int BTree::CheckMate(int a, int b)
{
    if ((tree[a].level == tree[b].level) &&(tree[a].parent != tree[b].parent))
    {
        return 1;
    }
    else return 0;
}
/*
void BTree::DelTree()
{
    delete tree[];
}*/
/*
template <class elemType>
void BTree<elemType>::DelTree(Node<elemType>*t)
{
    if (!t) {return;}
    DelTree(t->left);
    DelTree(t->right);
    delete t;
}*/


int main()
{
    int TestNum;
    cin >> TestNum;
    TestPair numbers[TestNum];
    //Node<int>* p;
    for (int i = 0; i < TestNum; i++)
    {
        cin >> numbers[i].a;
        cin >> numbers[i].b;
    }
    //cout << "start creat" << endl;
    BTree MyTree;
    MyTree.createTree();
    //cout << "finish" << endl;
    //MyTree.PreOrder();

    for (int i = 0; i < TestNum; i++)
    {
        int aIndex = -1, bIndex = -1;
        aIndex = MyTree.GetIndex(numbers[i].a);
        bIndex = MyTree.GetIndex(numbers[i].b);

        if (aIndex == -1 || bIndex == -1)
        {
            cout << 0 << endl;
            return 0;
        }
        cout << MyTree.CheckMate(aIndex, bIndex) << endl;

    }
    //cout <<sizeof(numbers) << endl;
    //cout << sizeof(tree) << endl;
    //tree->DelTree();

    return 0;
}
