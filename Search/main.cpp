#include <iostream>

using namespace std;

class illegalSize{};
template <class elemType>
class staticSearch
{
private:
    elemType *data;
    int len;
public:
    staticSearch(elemType a[], int n);
    int Search(const elemType &x) const;
    int BSearch(const elemType &x) const;
    ~staticSearch{delete []data;}
};

template <class elemType>
staticSearch<elemType>::staticSearch(elemType a[], int n)
{
    len = n;
    data = new elemType[n+1];
    if (!data) throw illegalSize();
    for (int i = 1; i < n+1; i++)data[i] = a[i-1];
}

template <class elemType>
int staticSearch<elemType>::Search(const elemType &x) const
{
    int i;
    data[0] = x;
    for (i = len; data[i]!=x; i--);
    return i;
}

template <class elemType>
int staticSearch<elemType>::BSearch(const elemType &x) const
{
    int mid, low, high;
    low = 1;
    high = len;
    while(low <= high)
    {
        mid = (low + high)/2;
        if (x == data[mid]) break;
        else
        {
            if (x < data[mid]) high = mid - 1;
            else low = mid +1;
        }
    }
    if (low <= high) return mid;
    return 0;
}

int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
