#include <iostream>
#include <iostream>
#include <stack>
#include <queue>
#include <list>

using namespace std;

template<class elemType>
class BTree;

template <class elemType>
class Node
{
    friend class BTree<elemType>;
private:
    elemType data;
    Node *left, *right;
    int leftFlag;
    int rightFlag;
public:
    Node(){left = nullptr;right = nullptr;leftFlag = 0; rightFlag = 0;};
    Node(const elemType &e, Node* L = nullptr, Node *R = nullptr)
    {
        data = e;
        left = L;
        right = R;
        leftFlag = 0;
        rightFlag = 0;
    };
    elemType GetData(){return data;}
};

template <class elemType>
class BTree
{
private:
    Node<elemType> *root;
    //elemType stopFlag;
    void PostOrder(Node<elemType> *t);
    void Mirror(Node<elemType> *t);

public:
    BTree(){root = nullptr;}
    void createTree(int rowNum);
    void PostOrder();
    void Mirror();
};

template <class elemType>
void BTree<elemType>::createTree(int rowNum)
{
    list<Node<elemType>*> ls;
    typename list<Node<elemType>*>::iterator itr;
    elemType e, el, er;
    Node<elemType> *p, *pl, *pr;

    for (int i = 0; i < rowNum; i++)
    {
        cin >> e >> el >> er;
        if (root == nullptr)
        {
            p = new Node<elemType>(e);
            root = p;
            if (el != -1)
            {
                pl = new Node<elemType>(el);
                p->left = pl;
                ls.push_back(pl);
            }
            if (er != -1)
            {
                pr = new Node<elemType>(er);
                p->right = pr;
                ls.push_back(pr);
            }
        }
        else
        {
            for (itr = ls.begin();itr != ls.end(); itr++)
            {

                if ((*itr)->GetData() == e)
                {
                    p = *itr;
                    if (el != -1)
                    {
                        pl = new Node<elemType>(el);
                        p->left = pl;
                        ls.push_back(pl);
                    }
                    if (er != -1)
                    {
                        pr = new Node<elemType>(er);
                        p->right = pr;
                        ls.push_back(pr);
                    }
                    ls.erase(itr);
                    break;
                }
            }
        }
    }
}

template <class elemType>
void BTree<elemType>::PostOrder(Node<elemType> *t)
{
    if (!t){return;}
    PostOrder(t->left);
    PostOrder(t->right);
    cout << t->data << " ";
}

template <class elemType>
void BTree<elemType>::PostOrder()
{
    PostOrder(root);
}

template <class elemType>
void BTree<elemType>::Mirror(Node<elemType> *t)
{
    Node<elemType> *pl, *pr;
    if (!t) {return;}
    if (t->left || (t->right))
    {
        pl = t->left;
        pr = t->right;
        t->left = pr;
        t->right = pl;
    }
    Mirror(t->left);
    Mirror(t->right);
    return;
}

template <class elemType>
void BTree<elemType>::Mirror()
{
    Mirror(root);
}

using namespace std;

int main()
{
    BTree<int>* tree;
    tree = new BTree<int>();
    int rowNum;
    cin >> rowNum;
    tree->createTree(rowNum);
    tree->Mirror();
    tree->PostOrder();
    return 0;
}
