#include <iostream>
#include <stack>
#include <queue>

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
};

template <class elemType>
class BTree
{
private:
    Node<elemType> *root;
    elemType stopFlag;

    int Size(Node<elemType>*t);
    int Height(Node<elemType>*t);
    void DelTree(Node<elemType>*t);
    void PreOrder(Node<elemType> *t);
    void InOrder(Node<elemType> *t);
    void PostOrder(Node<elemType> *t);
    int priOver(const char ch1, const char ch2);

public:
    BTree(){root = nullptr;}
    void createTree(const elemType &flag);
    bool isEmpty(){return (root = nullptr);}
    Node<elemType>*GetRoot(){return root;}
    int Size();
    int Height();
    void DelTree();
    void PreOrder();
    void InOrder();
    void PostOrder();
    void LevelOrder();
    Node<elemType>* buildTree(elemType pre[], int pl, int pr, elemType mid[], int ml, int mr);
    void buildExpTree(const char *exp);
    int calExpTree();
};

template <class elemType>
void BTree<elemType>::createTree(const elemType &flag)
{
    queue<Node<elemType>*> que;
    elemType e, el, er;
    Node<elemType> *p, *pl, *pr;

    stopFlag = flag;
    cout << "Please input the root: "; cin >> e;
    if (e = flag){root = nullptr;return;}
    p = new Node<elemType>(e);
    root = p;
    que.push(p);
    while (!que.empty())
    {
        p = que.front();
        que.pop();
        cout << "Please input the left child and the right child of" << p->data << "using " << flag << "as no child: ";
        cin >> el >> er;
        if (el!=flag)
        {
            pl = new Node<elemType>(el);
            p->left = pl;
            que.push(pl);
        }
        if (er!=flag)
        {
            pr = new Node<elemType>(er);
            p->right = pr;
            que.push(pr);
        }
    }
}

template <class elemType>
int BTree<elemType>::Size()
{
    return Size(root);
}

template <class elemType>
int BTree<elemType>::Size(Node<elemType>*t)
{
    if (!t){return 0;}
    return 1 + Size(t->left) + Size(t->right);
}

template <class elemType>
int BTree<elemType>::Height()
{
    return Height(root);
}

template <class elemType>
int BTree<elemType>::Height(Node<elemType>*t)
{
    int hl, hr;
    if(!t){return 0;}
    hl = Height(t->left);
    hr = Height(t->right);

    if (hl>=hr){return hl+1};
    else{return hr+1};
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

template <class elemType>
void BTree<elemType>::PreOrder(Node<elemType>*t)
{

    if (!t) {return;}
    cout << t->data;
    PreOrder(t->left);
    PreOrder(t->right);

}

template <class elemType>
void BTree<elemType>::PreOrder()
{
    if (!root) {return;}
    Node<elemType> *p;
    stack<Node<elemType>*> s;
    s.push(root);
    while (!s.empty())
    {
        p = s.top();
        s.pop();
        cout << p->data;
        if (p->right)
        {
            s.push(p->right);
        }
        if (p->left)
        {
            s.push(p->left);
        }
        cout << endl;
    }
}

template <class elemType>
void BTree<elemType>::InOrder(Node<elemType>*t)
{
    if (!t){return;}
    InOrder(t->left);
    cout << t->data;
    InOrder(t->right);
}

template <class elemType>
void BTree<elemType>::InOrder()
{
    if (!root){return;}

    stack<Node<elemType>*>s1;
    stack<int>s2;
    Node<elemType>*p;
    int flag;
    int zero = 0, one = 1;
    p = root;
    s1.push(p);
    s2.push(zero);
    while(!s1.empty())
    {
        flag = s2.top();
        s2.pop();
        p = s1.top();
        if (flag == 1)
        {
            s1.pop();
            cout << p->data;
            if (!p->right){continue;}
            s1.push(p->right);
            s2.push(zero);
        }
        else{
            s2.push(one);
            if (p->left)
            {
                s1.push(p->left);
                s2.push(zero);
            }
        }
    }
    cout << endl;
}

template <class elemType>
void BTree<elemType>::PostOrder(Node<elemType> *t)
{
    if (!t){return;}
    PostOrder(t->left);
    PostOrder(t->right);
    cout << t->data;
}

template <class elemType>
void BTree<elemType>::PostOrder()
{
    if (!root) {return;}
    Node<elemType>*p;
    stack<Node<elemType>*>s1;
    stack<int> s2;
    int zero = 0, one = 1, two = 2;
    int flag;
    s1.push(root);
    s2.push(zero);
    while(!s1.isEmpty())
    {
        flag = s2.top();
        s2.pop();
        p = s1.top();
        switch(flag)
        {
            case 2: s1.pop();
                    cout << p->data;
                    break;
            case 1: s2.push(two);
                    if (p->right)
                    {
                        s1.push(p->right);
                        s2.push(zero);
                    }
                    break;
            case 0: s2.push(one);
                    if (p->left)
                    {
                        s1.push(p->left);
                        s2.push(zero);
                    }
                    break;
        };
    }
}

template <class elemType>
void BTree<elemType>::LevelOrder()
{
    queue<Node<elemType>*>que;
    if (!root){return;}

    que.push(root);
    while (!que.empty())
    {
        p = que.front();
        que.pop();
        cout << p->data;
        if (p->left){que.push(p->left);}
        if (p->right){que.push(p->right);}
    }
    cout << endl;
}

template <class elemType>
Node<elemType>* BTree<elemType>::buildTree(elemType pre[], int pl, int pr, elemType mid[], int ml, int mr)
{
    //pre数组存储了前序遍历序列，pl为序列左边界下标，pr为序列右边界下标。
    //min数组存储了中序遍历序列，ml为序列左边界下标，mr为序列右边界下标。
    Node<elemType> *p, *leftRoot, *rightRoot;
    int i, pos, num;
    int lpl, lml, lmr; //左子树中前序的左右边界、中序的左右边界
    int rpl, rpr, rml, rmr;//右子树中前序的左右边界、中序的左右边界
    if (pl>pr){return nullptr};
    p = new Node<elemType>(pre[pl]);
    if (!root) {root = p;}

    for (i = ml; i < mr; i++)
    {
        if (mid[i] == pre[pl])
        {
            break;
        }
    }
    pos = i;
    num = pos-ml;
    lpl = pl+1;
    lpr = pl+num;
    lml = ml;
    lmr = pos - 1;
    leftRoot = buildTree(pre, lpl, lpr,mid,lml,lmr);

    rpl = pl+num+1;
    rpr = pr;
    rml = pos+1;
    rmr = mr;
    rightRoot = buildTree(pre, rpl, rpr,mid,rml,rmr);
    p->left = leftRoot;
    p->right = rightRoot;
    return p;
}

template <class elemType>
int BTree<elemType>::priOVer(const char ch1, const char ch2)
{
    switch (ch1)
    {
        case '(':return 1; break;
        case ')':if (ch2 != '(')return -1;
                else return 0;
                break;
        case '*':
        case '/': if ((ch2 == '*') || (ch2 == '/')) return -1;
                    else return 1;
        case '+':
        case '-':
            if ((ch2 == '#')||(ch2 == '(')) return 1;
            else return -1;
    };
}

template <class elemType>
void BTree<elemType>::buildExpTree(const char *exp)
{
    stack<char> opStack;
    stack<Node<elemType>*> subTStack;

    Node<elemType>*p, *left, *right;
    char myHash = '#', ch;

    opStack.push(myHash);
    while (*exp)
    {
        if ((*exp >= '0') && (*exp<='9'))
        {
            p = new Node<elemType>(*exp);
            subTStack.push(p);
        }
        else{
            ch = opStack.top();
            while(priOver(*exp, ch) == -1)
            {
                opStack.pop();
                right = subTStack.top();
                subTStack.pop();
                left = subTStack.top();
                subTStack.pop();
                p = new Node<elemType>(ch, left, right);
                subTStack.push(p);
                ch = opStack.top();
            }
            if (priOver(*exp, ch) == 0)
                opStack.pop();
            else
                opStack.push(*exp);
        }
        exp++;
    }
    ch = opStack.top();
    while (ch != '#')
    {
        opStack.pop();
        right = subTStack.top();
        subTStack.pop();
        left = subTStack.top();
        subTStack.pop();
        p = new Node<elemType>(ch, left, right);
        subTStack.push(p);
        ch = opStack.top();
    }
    root = subTStack.top();
    subTStack.pop();
}

template <class elemType>
int BTree<elemType>::calExpTree()
{
    if (!root) {return 0;}

    Node<elemType> *p;
    stack<Node<elemType>*> s1;
    stack<int> s2;
    stack<int>numStack;

    int zero = 0, one = 1, two = 2;
    int flag, num, num1, num2;

    s1.push(root);
    s2.push(zero);
    while (!s1.empty())
    {
        flag = s2.top();
        s2.pop();
        p = s1.top();
        switch(flag)
        {
        case 2:
            s1.pop();
            if ((p->data >= '0') && (p->data <= '9'))
            {
                num = p->data - '0';
                numStack.push(num);
            }
            else
            {
                num2 = numStack.top();
                numStack.pop();
                num1 = numStack.top();
                numStack.pop();
                switch (p->data)
                {
                    case '+':num = num1 + num2; break;
                    case '-':num = num1 - num2; break;
                    case '*':num = num1*num2; break;
                    case '/':num = num1/num2; break;
                }
                numStack.push(num);
            }
            break;
        case 1:s2.push(two);
                if (p->right)
                {
                    s1.push(p->right);
                    s2.push(zero);
                }
                break;
        case 0:s2.push(one);
                if (p->left)
                {
                    s1.push(p->left);
                    s2.push(zero);
                }
                break;
        }
    }
    num = numStack.top();
    return num;
}
int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
