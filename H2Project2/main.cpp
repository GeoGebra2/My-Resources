#include <iostream>

using namespace std;

class ChildList;
class ChildNode
{
    friend class ChildList;
private:
    ChildNode *next;
    int index;
    int RoundTime;
public:
    ChildNode() : next(nullptr), index(0), RoundTime(0) {};
    ChildNode(int s, int m, ChildNode *N = nullptr)
        : next(N), index(s), RoundTime(m) {};
    int GetIndex();
    int GetRoundTime();
    void SetIndex(int s);
    void SetRoundTime(int s);
};

class ChildList
{
private:
    ChildNode *head;
public:
    ChildList();
    void insertNode(int in, int ro);
    void PrintList();
};

int ChildNode::GetIndex()
{
    return index;
}

int ChildNode::GetRoundTime()
{
    return RoundTime;
}

void ChildNode::SetIndex(int s)
{
    index = s;
    return;
}

void ChildNode::SetRoundTime(int s)
{
    RoundTime = s;
    return;
}

ChildList::ChildList()
{
    head = nullptr;
}

void ChildList::insertNode(int in, int ro)
{
    if (!head)
    {
        head = new ChildNode(in, ro);
        return;
    }
    ChildNode* ptr = head;
    ChildNode* present = head;
    ChildNode* tmp;

    if (ro < head->RoundTime)
    {
        tmp = new ChildNode(in, ro);
        tmp->next = head;
        head = tmp;
        return;
    }


    while(ptr)
    {
        if (ro < ptr->RoundTime)
        {
            break;
        }
        present = ptr;
        ptr = ptr->next;
    }
    if (!ptr)
    {
        tmp = new ChildNode(in, ro);
        present->next = tmp;
        return;
    }
    else
    {
        tmp = new ChildNode(in, ro);
        present->next = tmp;
        tmp->next = ptr;
    }
    return;
}

void ChildList::PrintList()
{
    ChildNode* p = head;
    while(p)
    {
        cout << p->GetIndex() << " ";
        p = p->next;
    }
    return;
}

int main()
{
    int ChildrenNum, MostTime;

    ChildList* line = new ChildList();
    cin >> ChildrenNum;
    cin >> MostTime;
    int ChildrenTime[ChildrenNum];

    for (int i = 0; i < ChildrenNum; i++)
    {
        int tem;
        cin >> tem;
        if (tem % MostTime == 0)
        {
            tem = tem / MostTime;
        }
        else{
            tem = tem / MostTime + 1;
        }
        ChildrenTime[i] = tem;
    }


    for (int i = 0; i < ChildrenNum; i++)
    {
        line->insertNode(i, ChildrenTime[i]);
    }

    line->PrintList();


    return 0;
}
