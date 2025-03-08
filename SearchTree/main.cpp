#include <iostream>
#include <stack>
#include <Queue>

using namespace std;

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
    bool NodeSearch(const elemType &x, Node<elemType> *t) const;
    void NodeInsert(const elemType &x, Node<elemType> *&t);
    void NodeRemove(const elemType &x, Node<elemType> *&t);
public:
    binarySearchTree(){root = nullptr;}
    bool NodeSearch(const elemType &x) const;
    void NodeInsert(const elemType &x);
    void NodeRemove(const elemType &x);
    void levelTravese() const;
};

template <class elemType>
bool binarySearchTree<elemType>::NodeSearch(const elemType &x, Node<elemType> *t)const
{
    if (!t) {return false;}
    if (x == t->data) return true;
    if (x < t->data)
        return NodeSearch(x, t->left);
    else
        return NodeSearch(x, t->right);
}

template <class elemType>
bool binarySearchTree<elemType>::NodeSearch(const elemType &x) const
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
}

template <class elemType>
void binarySearchTree<elemType>::NodeInsert(const elemType &x, Node<elemType> *&t)
{
    if (!t) {t = new Node<elemType>(x); return;}
    if (x == t->data) return;
    if (x < t->data) NodeInsert(x, t->left);
    else NodeInsert(x, t->right);
}

template <class elemType>
void binarySearchTree<elemType>::NodeInsert(const elemType &x)
{
    Node<elemType> *p;
    if (!root)
    {
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

template <class elemType>
void binarySearchTree<elemType>::NodeRemove(const elemType &x, Node<elemType> *&t)
{
    if (!t) return;
    if (x < t->data)
    {
        NodeRemove(x, t->left);
    }
    else
    {
        if (x > t->data){
            NodeRemove(x, t->right);
        }
        else
        {
            if (!t->left && !t->right)
            {
                delete t;
                t = nullptr;
                return;
            }
            if (!t->left || !t->right)
            {
                Node<elemType> *tmp;
                tmp = t;
                t = (t->left)? t->left: t->right;
                delete tmp;
                return;
            }
            Node<elemType> *p;
            p = t->right;
            while(p->left){
                p = p->left;
            }
            t->data = p->data;
            NodeRemove(p->data, t->right);
        }
    }
}

int main()
{

    return 0;
}
