#include <iostream>
#include <stack>

using namespace std;
/*
int target;
int count_num;

template <class elemType>
class binarySearchTree;

template <class elemType>
class Node
{
    friend class binarySearchTree<elemType>;

private:
    elemType data;
    Node *left, *right;

public:
    Node(){left = nullptr; right = nullptr;}
    Node(const elemType &x, Node *l = nullptr, Node *r = nullptr)
    {
        data = x;
        left = l;
        right = r;
    }
};

template <class elemType>
class binarySearchTree
{
private:
    Node<elemType> *root;
    //bool NodeSearch(const elemType &x, Node<elemType> *t) const;
    //void NodeInsert(const elemType &x, Node<elemType> *&t);
    void InOrder(Node<elemType> *t);
    //void NodeRemove(const elemType &x, Node<elemType> *&t);
public:
    binarySearchTree(){root = nullptr;}
    bool NodeSearch(const elemType &x);
    void NodeInsert(elemType x);
    void InOrder();
    //void NodeRemove(const elemType &x);
    //void levelTravese() const;
};*/
/*
template <class elemType>
bool binarySearchTree<elemType>::NodeSearch(const elemType &x, Node<elemType> *t)const
{
    if (!t) {return false;}
    if (x == t->data) return true;
    if (x < t->data)
        return NodeSearch(x, t->left);
    else
        return NodeSearch(x, t->right);
}*/
/*
template <class elemType>
bool binarySearchTree<elemType>::NodeSearch(const elemType &x)
{
    if (!root) return false;
    Node<elemType> *p;
    p = root;
    while (p)
    {
        if (x == p->data) return true;
        if (x < p->data) p = p->left;
        else p = p->right;
    }
    return false;
}*/
/*
template <class elemType>
void binarySearchTree<elemType>::NodeInsert(const elemType &x, Node<elemType> *&t)
{
    if (!t) {t = new Node<elemType>(x); return;}
    if (x == t->data) return;
    if (x < t->data) NodeInsert(x, t->left);
    else NodeInsert(x, t->right);
}*/
/*
template <class elemType>
void binarySearchTree<elemType>::NodeInsert(elemType x)
{
    Node<elemType> *p;
    if (!root)
    {
//cout << x << endl;
        root = new Node<elemType>(x);
        return;
    }
    p = root;
    while (p)
    {
        if (x == p->data) return;
        if (x < p->data)
        {
            if (!p->left)
            {
                p->left = new Node<elemType>(x);
                return;
            }
            p = p->left;
        }
        else
        {
            if (!p->right)
            {
                p->right = new Node<elemType>(x);
                return;
            }
            p = p->right;
        }
    }
}

template <class elemType>
void binarySearchTree<elemType>::InOrder(Node<elemType> *t)
{
    if (!t){return;}
    InOrder(t->left, s);
    if (count_num == target){

    }
    InOrder(t->right, s);
}

template <class elemType>
void binarySearchTree<elemType>::InOrder()
{
    InOrder(root, s);
}*/
/*
template <class elemType>
void binarySearchTree<elemType>::NodeInsert(const elemType &x)
{
    Node<elemType> *p, *tmp, *parent = nullptr;
    int flag;
    p = root;
    while (p)
    {
        if (x == p->data) return;
        parent = p;
        if (x < p->data){flag = 0; p = p->left;}
        else {flag = 1; p = p->right;}
    }

    tmp = new Node<elemType>(x);
    if (!parent){root = tmp; return;}
    if (flag == 0)parent->left = tmp;
    else parent->right = tmp;
}*/

int main()
{
    /*
    binarySearchTree<int>* tree;
    tree = new binarySearchTree<int>();
    //stack<int> orderNum;
    //int result;
    for (int i = 0; i < 7; i++)
    {
        int temp;
        cin >> temp;
        //cout << "insert" << endl;
        tree->NodeInsert(temp);
        //cout << "insert end" << endl;
    }
    //int target;
    cin >> target;
    tree->InOrder();
    //for (int i = 0; i < target; i++)
    //{
        //result = orderNum.top();
        //orderNum.pop();
    //}
    //cout << result << endl;
    return 0;*/
    int numbers[7];
    int target;
    for (int i = 0; i < 7; i++)
    {
        cin >> numbers[i];
    }
    cin >> target;

    switch (target)
    {
        case 1: cout << numbers[6] << endl; break;
        case 2: cout << numbers[2] << endl; break;
        case 3: cout << numbers[5] << endl; break;
        case 4: cout << numbers[0] << endl; break;
        case 5: cout << numbers[4] << endl; break;
        case 6: cout << numbers[1] << endl; break;
        case 7: cout << numbers[3] << endl; break;

    }
}
