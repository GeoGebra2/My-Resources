#include <iostream>

using namespace std;
class FreeList;
class MemoryBlock
{
    friend class FreeList;
private:
    MemoryBlock *next;
    int start;
    int memorySize;
public:
    MemoryBlock() : next(nullptr), start(0), memorySize(0) {};
    MemoryBlock(int s, int m, MemoryBlock *N = nullptr)
        : next(N), start(s), memorySize(m) {};
    int GetStart();
    int GetSize();
    void SetStart(int s);
    void SetSize(int s);
};

class FreeList
{
private:
    MemoryBlock *head;
public:
    FreeList(int s, int t);
    void Allocate(int request_size);
    void Release(int sstart, int ssize);
    void AddMemory(int s, int t);
    void PrintList();
    ~FreeList();
};

int MemoryBlock::GetStart()
{
    return start;
}

int MemoryBlock::GetSize()
{
    return memorySize;
}

void MemoryBlock::SetStart(int s)
{
    start = s;
    return;
}

void MemoryBlock::SetSize(int s)
{
    memorySize = s;
    return;
}

FreeList::FreeList(int s, int t)
{
    head = new MemoryBlock(s, t, nullptr);
}

void FreeList::Allocate(int request_size)
{
    if (request_size <= 0)
    {
        return;
    }
    MemoryBlock *p = head;
    MemoryBlock *tmp = head;
    while(p)
    {
        if (p->GetSize() >= request_size)
        {
            break;
        }
        tmp = p;
        p = p->next;
    }
    if (!p)
    {
        return;
    }

    if (p->GetSize() == request_size)
    {
        if (p == head && p->next == nullptr)
        {
            head = nullptr;
            delete p;
            return;
        }
        else if (p == head)
        {
            head = p->next;
            delete p;
            return;
        }
        tmp->next = p->next;
        delete p;
        return;
    }
    else
    {
        p->memorySize = p->GetSize() - request_size;
        p->start = p->GetStart() + request_size;
        return;
    }
}

void FreeList::Release(int sstart, int ssize)
{
    MemoryBlock *p = head;
    MemoryBlock *tmp;

    if (!head)
    {
        head = new MemoryBlock(sstart, ssize, nullptr);
        return;
    }

    if (sstart < p->GetStart())
    {
        if (sstart + ssize >= p->GetStart())
        {
            p->start = sstart;
            p->memorySize = p->GetStart() + p->GetSize() - sstart;
        }
        else
        {
            tmp = new MemoryBlock(sstart, ssize, p);
            head = tmp;
        }

    }
    else
    {
        while(p->next)
        {
            if (p->GetStart() < sstart && p->next->GetStart() > sstart)
            {
                break;
            }
            p = p->next;
        }
        if (!p->next)
        {
            if (p->GetStart() + p->GetSize() >= sstart)
            {
                p->memorySize = ssize + sstart - p->GetStart();
            }
            else
            {
                tmp = new MemoryBlock(sstart, ssize, nullptr);
                p->next = tmp;
            }
        }
        else{
            if (sstart + ssize >= p->next->GetStart())
            {
                //cout << "here" << endl;
                p->next->memorySize = p->next->GetStart() + p->next->GetSize() - sstart;
                p->next->start = sstart;
                //cout << sstart << endl;
                //cout << p->next->GetStart() << endl;
                //cout << p->next->GetSize() << endl;
                //cout << p->next->GetStart() + p->next->GetSize() - sstart;

                //cout << p->next->GetSize() << endl;
                if (p->GetStart() + p->GetSize() >= sstart)
                {
                    p->memorySize = p->next->GetStart() + p->next->GetSize() - p->GetStart();
                    //cout << p->GetSize() << endl;
                    tmp = p->next;
                    p->next = tmp->next;
                    delete tmp;
                }
            }
            else
            {
                if (p->GetStart() + p->GetSize() >= sstart)
                {
                    p->memorySize = ssize + sstart - p->GetStart();
                }
                else
                {
                    tmp = new MemoryBlock(sstart, ssize, p->next);
                    p->next = tmp;
                }

            }
        }
    }
    return;
}



void FreeList::PrintList()
{
    MemoryBlock *p = head;
    while(p)
    {
        cout << "(" << p->GetStart() << "," << p->GetSize() << ") ";
        p = p->next;
    }
    return;
}

FreeList::~FreeList()
{
    MemoryBlock *current = head;
    while(current != nullptr)
    {
        MemoryBlock *next = current->next;
        delete current;
        current = next;
    }
}

int main()
{
    int BlockNumber = 0, OperateNum = 0;
    cin >> BlockNumber;
    int start[BlockNumber], sizee[BlockNumber];

    for (int i = 0; i < BlockNumber; i++)
    {
        cin >> start[i];
    }
    for (int i = 0; i < BlockNumber; i++)
    {
        cin >> sizee[i];
    }
    FreeList* MemoryList = new FreeList(start[0], sizee[0]);
    for (int i = 1; i < BlockNumber; i++)
    {
        MemoryList->Release(start[i], sizee[i]);
    }
        //MemoryList->PrintList();


    cin >> OperateNum;
    for (int i = 0; i < OperateNum; i++)
    {
        int order;
        cin >> order;
        if (order == 1)
        {
            int request_size;
            cin >> request_size;
            MemoryList->Allocate(request_size);
        }
        else if (order == 2)
        {
            int s, t;
            cin >> s >> t;
            MemoryList->Release(s, t);
        }
        //cout << "print " << endl;
        //MemoryList->PrintList();
    }
    MemoryList->PrintList();
    return 0;
}
