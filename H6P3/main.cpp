#include <iostream>

using namespace std;

int CheckNum = 0;

template<class elemType>
class Link;

template <class elemType>
class Node
{
    friend class Link<elemType>;
private:
    elemType data;
    Node *next;
public:
    Node(){next = nullptr;};
    Node(const elemType &e, Node* n = nullptr)
    {
        data = e;
        next = n;
    };
};

template <class elemType>
class Link
{
private:
    Node<elemType> *head;
    //elemType stopFlag;

public:
    Link();
    void InsertNode(elemType &e);
    void CheckNode(elemType x);
    void PrintLink();
};

template <class elemType>
Link<elemType>::Link()
{
    head = nullptr;
}

template <class elemType>
void Link<elemType>::InsertNode(elemType &e)
{
    Node<elemType>*p = head;
    if (p == nullptr)
    {
        head = new Node<elemType>(e);
    }
    else
    {
        while(p->next != nullptr)
        {
            p = p->next;
        }
        p->next = new Node<elemType>(e);
    }
    return;
}

template <class elemType>
void Link<elemType>::CheckNode(elemType x)
{
    //cout << "begin check" << endl;
    Node<elemType>*prev = head, *current = head;
    while(prev != nullptr && prev->data != x)
    {
        //cout << prev->data << " " << current->data << endl;
        current = prev;
        prev = prev->next;
        CheckNum += 1;
    }
    //cout << "end iteration" << endl;
    if (prev == nullptr)
    {
        //cout << "can not find" << endl;
        return;
    }
    else
    {

        //cout << "move" << endl;
        CheckNum += 1;
        if (prev != head)
        {
            current->next = prev->next;
            prev->next = head;
            head = prev;
        }
    }
}

template <class elemType>
void Link<elemType>::PrintLink()
{
    Node<elemType>* p = head;
    while(p!= nullptr)
    {
        cout << p->data << " ";
        p = p->next;
    }
    cout << endl;
    return;
}



int main()
{
    Link<int>* MyLink = new Link<int>();
    int m, n, tmp;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        MyLink->InsertNode(tmp);
    }
    //cout << "end" << endl;
    //MyLink->PrintLink();
    cin >> m;
    for (int i = 0; i < m; i++)
    {
        cin >> tmp;
        MyLink->CheckNode(tmp);
        //MyLink->PrintLink();
    }
    cout << CheckNum << endl;

    return 0;
}
