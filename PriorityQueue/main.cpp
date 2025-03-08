#include <iostream>

using namespace std;

template <class elemType>
class priorityQueue
{
private:
    elemType *arrays;
    int maxSize, currentLen;
    void adjust(int hole);
public:
    priorityQueue(int sizes=10);
    priorityQueue(elemType a[], int n);
    bool isEmpty();
    bool isFull();
    elemType ReadFront();
    void enQueue(const elemType &x, int priority);
    void deQueue();

};

template<class elemType>
priorityQueue<elemType>::priorityQueue(int sizes)
{
    arrays = new elemType[sizes];
    maxSize = sizes;
    currentLen = 0;
}

template <class elemType>
void priorityQueue<elemType>::adjust(int hole)
{
    int minChild;
    elemType x, temp;
    x = arrays[hole];
    while(true)
    {
        minChild = 2*hole+1;
        if (minChild > currentLen) break;
        if (minChild+1 <= currentLen-1)
        {
            if (arrays[minChild+1] < arrays[minChild])
            {
                minChild++;
            }
        }
        if (x < arrays[minChild]) break;
        arrays[hole] = arrays[minChild];
        hole = minChild;
    }
    arrays[hole] = x;
}



template <class elemType>
priorityQueue<elemType>::priorityQueue(elemType a[], int n)
{
    arrays = new elemType[n+10];
    maxSize = n+10;
    currentLen = n;
    for (int i = 0; i<n; i++) arrays[i] = a[i];
    for (int i = n/2-1; i>=0; i--) adjust(i);
}

template<class elemType>
bool priorityQueue<elemType>::isEmpty()
{
    return currentLen == 0;
}

template<class elemType>
bool priorityQueue<elemType>::isFull()
{
    return currentLen == maxSize;
}

template<class elemType>
elemType priorityQueue<elemType>::ReadFront()
{
    return arrays[0];
}

template <class elemType>
void priorityQueue<elemType>::deQueue()
{
    arrays[0] = arrays[currentLen-1];
    currentLen--;
    adjust(0);
}

template<class elemType>
void priorityQueue<elemType>::enQueue(const elemType &x)
{
    int hole = currentLen;
    for (;hole>0&&a<arrays[(hole-1)/2];hole = (hole-1)/2)
    {
        arrays[hole] = arrays[(hole-1)/2];
    }
    arrays[hole] = x;
}

int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
