#include <iostream>

using namespace std;

template <class elemType>
class binaryAVLSearchTree<class elemType>

template <class elemType>
class AVLNode
{
    friend class binaryAVLSearchTree<elemType>;
private:
    elemType data;
    Node *left, *right;
public:
    AVLNode(){left = nullptr; right = nullptr; height = 0;}
    AVLNode(const elemType &x, Node *l = nullptr, Node *r = nullptr)
    {
        data = x;
        left = l;
        right = r;
        height = 1;
    }
};

template <class elemType>
class binaryAVLSearchTree
{
private:
    AVLNode<elemType> *root;
    int height(AVLNode<elemType>*t) const;
    void LL(AVLNode<elemType>*&t);
    void LR(AVLNode<elemType>*&t);
    void RL(AVLNode<elemType>*&t);
    void RR(AVLNode<elemType>*&t);
    bool NodeSearch(const elemType &x, AVLNode<elemType> *&t) const;
    void NodeInsert(const elemType &x, AVLNode<elemType> *&t);
    void NodeRemove(const elemType &x, AVLNode<elemType> *&t);
public:
    binarySearchTree(){root = nullptr;}
    bool NodeSearch(const elemType &x) const;
    void NodeInsert(const elemType &x);
    void NodeRemove(const elemType &x);
    void levelTravese() const;
};

int binaryAVLSearchTree<elemType>::height(AVLNode<elemType>*t) const
{
    if (!t) return 0;
    return t->height;
}

template <class elemType>
void binaryAVLSearchTree<elemType>::NodeInsert(const elemType &x, AVLNode<elemType> *&t)
{
    if (!t) t = new AVLNode<elemType>(x);
    else if (x == t->data) {return;}
    else if (x < t->data)
    {
        NodeInsert(x, t->left);
        if (height(t->left)- height(t->right) == 2)
            if (x < (t-left)->data) LL(t);
            else LR(t);
    }
    else if (t->data < x)
    {
        NodeInsert(x, t->right);
        if (height(t->left) - height(t->right) == -2)
            if (x > (t->right)->data)
                RR(t);
            else
                RL(t);
    }
    t->height = max(height(t->left), height(t->right)) + 1;
}

template <class elemType>
void binaryAVLSearchTree<elemType>::LL(AVLNode<elemType>*&t)
{
    AVLNode<elemType>*newRoot = t->left;
    t->left = newRoot->right;
    newRoot->right = t;
    t->height = max(height(t->left), height(t->right)) + 1;
    newRoot->height = max(height(newRoot->left), height(t->right)) + 1;
    t = newRoot;
}

template <class elemType>
void binaryAVLSearchTree<elemType>::RR(AVLNode<elemType>*&t)
{
    AVLNode<elemType>*newRoot = t->right;
    t->right = newRoot->left;
    newRoot->left = t;
    t->height = max(height(t->left), height(t->right)) + 1;
    newRoot->height = max(height(newRoot->left), height(t->right)) + 1;
    t = newRoot;
}


int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
