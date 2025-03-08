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

template<class elemType>
class BTree;

template <class elemType>
class Node
{
    friend class BTree<elemType>;
public:
    elemType data;
    Node *left, *right, *parent;
    int flag;
    int level;
    Node(){left = nullptr;right = nullptr;parent = nullptr;flag = 0;level = 1;};
    Node(const elemType &e, Node* L = nullptr, Node *R = nullptr, Node *P = nullptr, int l = 1)
    {
        data = e;
        left = L;
        right = R;
        parent = P;
        flag = 0;
        level = l;
    };
    elemType GetData(){return data;}
};

template <class elemType>
class BTree
{
private:
    Node<elemType> *root;
    void PreOrder(Node<elemType> *t);
    int CheckMate(Node<elemType>*t, elemType a, elemType b);
    void DelTree(Node<elemType>*t);
public:
    BTree(){root = nullptr;}
    void createTree();
    Node<elemType>* GetRoot(){return root;}
    int CheckMate(elemType a, elemType b);
    void PreOrder();
    void LevelOrder();
    void DelTree();
};

template <class elemType>
void BTree<elemType>::createTree()
{
    Node<elemType> *p, *pl, *pr;
    //bool notFull = true;
    while (true)
    {
        elemType temp;
        cin >> temp;
        if (root == nullptr)
        {
            p = new Node<elemType>(temp);
            root = p;
        }
        else
        {
            //cout << "data: " << p->data << " flag: " << p->flag << endl;
            if (temp == -1){p->flag++;}
            else
            {
                if (p->flag == 0)
                {
                    pl = new Node<elemType>(temp, nullptr, nullptr, p, (p->level + 1));
                    p->left = pl;
                    p->flag++;
                    p = pl;
                }
                else if (p->flag == 1)
                {
                    pr = new Node<elemType>(temp, nullptr, nullptr, p, (p->level + 1));
                    p->right = pr;
                    p->flag++;
                    p = pr;
                }
                else
                {
                    cout << "wrong" << endl;
                    break;
                }

            }
            while (p->flag == 2 && p->parent != nullptr)
            {
                //cout << "before back, data: " << p->data << " flag: " << p->flag << endl;
                p = p->parent;
                //cout << "go back, data: " << p->data << " flag: " << p->flag << endl;
            }
            if (p == root && p->flag == 2)
            {
                break;
            }
        }
    }

}

template <class elemType>
void BTree<elemType>::PreOrder(Node<elemType>*t)
{

    if (!t) {return;}
    cout << t->data << " ";
    PreOrder(t->left);
    PreOrder(t->right);

}

template <class elemType>
void BTree<elemType>::PreOrder()
{
    PreOrder(root);
    cout << endl;
}

template <class elemType>
void BTree<elemType>::DelTree()
{
    DelTree(root);
    root = nullptr;
}

template <class elemType>
void BTree<elemType>::DelTree(Node<elemType>*t)
{
    if (!t) {return;}
    DelTree(t->left);
    DelTree(t->right);
    delete t;
}


int main()
{
    int TestNum;
    cin >> TestNum;
    TestPair numbers[TestNum];
    //queue<Node<int>*> que;
    //list<Node<int>*> ls;
    //typename list<Node<int>*>::iterator itr;
    Node<int>* p;
    //int preTree[1000];
    for (int i = 0; i < TestNum; i++)
    {
        cin >> numbers[i].a;
        cin >> numbers[i].b;
    }
    /*
    for (int i = 0; i < TestNum; i++)
    {
        cout << numbers[i].a;
        cout << numbers[i].b << endl;
    }*/
    BTree<int> *tree;
    tree = new BTree<int>();
    tree->createTree();
    //tree->PreOrder();

    /*
    for (itr = ls.begin();itr != ls.end(); itr++)
    {
        cout << (*itr)->GetData() << endl;
    }*/
    for (int i = 0; i < TestNum; i++)
    {
        //cout << numbers[i].a << " " << numbers[i].b << endl;
        int aIndex = 0, bIndex = 0, index = 1;
        queue<Node<int>*> que;
        Node<int> *ap, *bp;
        p = tree->GetRoot();
        if (p != nullptr)
        {
            que.push(p);
            while(!que.empty())
            {
                p = que.front();
                que.pop();
                if (p->data == numbers[i].a)
                {
                    ap = p;
                    aIndex = index;
                }
                if (p->data == numbers[i].b)
                {
                    bIndex = index;
                    bp = p;
                }
                if (p->left){que.push(p->left);}
                if (p->right){que.push(p->right);}
                index++;
                if (aIndex != 0 && bIndex!=0)
                {
                    break;
                }
            }
        }
        if (aIndex == 0 || bIndex == 0)
        {
            cout << 0 << endl;
            return 0;
        }
        //cout << "a: " << aIndex << " b: " << bIndex << endl;
        //cout << "log2: " << int(log2(3)) << endl;
        if ((ap->level == bp->level) && (ap->parent != bp->parent))
        {
            cout << 1 << endl;
        }
        else
        {
            cout << 0 << endl;
        }

    }
    //cout <<sizeof(numbers) << endl;
    //cout << sizeof(tree) << endl;
    tree->DelTree();

    return 0;
}
