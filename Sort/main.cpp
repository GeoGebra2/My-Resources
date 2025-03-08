#include <iostream>

using namespace std;

template <class elemType>
void bubbleSort(elemType a[], int n)
{
    int i, j;
    bool change = true;
    elemType tmp;
    for (j = n-1; j > 0 && change; j--)
    {
        change = false;
        for (i = 0; i < j; i++)
        {
            if (a[i] > a[i+1])
            {
                tmp = a[i];
                a[i] = a[i+1];
                a[i+1] = tmp;
                change = true;
            }
        }
    }
}

template <class elemType>
void Myinsert(elemType a[], int n, const elemType &x)
{
    int i;
    for (i = n-1;i>=0;i--)
    {
        if (a[i] <= x) break;
        else a[i+1] = a[i];
    }
    a[i+1] = x;
}

template <class elemType>
void insertSort(elemType a[], int n)
{
    int i;
    elemType tmp;
    for (i = 1; i < n; i++)
    {
        tmp = a[i];
        Myinsert(a,i,tmp);
    }
}

template <class elemType>
void shellSort(elemType a[], int n)
{
    int step, i, j;
    elemType tmp;
    for (step = n/2; step > 0; step /= 2)
    {
        for (i = step; i < n; i++)
        {
            tmp = a[i];
            j = i;
            while((j-step >= 0)&&(tmp < a[j-step]))
            {
                a[j] = a[j-step];
                j-=step;
            }
            a[j] = tmp;
        }
    }
}

template <class elemType>
void MyMerge(elemType a[], int low, int mid, int high)
{
    int i,j,k;
    elemType *c;
    c = new elemType[high-low+1];
    i = low;
    j = mid+1;
    k=0;
    while((i<=mid)&&(j<=high))
    {
        if (a[i] <= a[j])
        {
            c[k] = a[i];
            i = i+1;
        }
        else
        {
            c[k] = a[j];j++;
        }
        k++;
    }
    while(i<=mid)
    {
        c[k] = a[i]; i++; k++;
    }
    while(j <=high)
    {
        c[k] = a[j]; j++; k++;
    }
    for (i = 0; i < high-low+1;i++)
    {
        a[i+low] = c[i];
    }
    delete []c;
}

template <class elemType>void mergeSort(elemType a[], int n)
{
    mergeSort(a, 0, n-1);
}

template <class elemType>void mergeSort(elemType a[], int low, int high)
{
    int mid;
    if (low >= high) return;
    mid = (low + high) /2;
    mergeSort(a, low, mid);
    mergeSort(a, mid+1, high);
    MyMerge(a, low, mid, high);
}

template <class elemType>
void quickSort(elemType a[], int start, int ends)
{
    int i,j,hole;
    elemType temp;
    if (ends <= start) return;
    temp = a[start];
    hole = start;
    i = start;
    j = ends;
    while(i<j)
    {
        while((j>i)&&(a[j] >= temp)) j--;
        if (j==i) break;
        a[hole] = a[j];
        hole = j;
        while((i<j) && a[i] < temp) i++;
        if (j==i) break;
        a[hole] = a[i];
        hole = i;
    }
    a[hole] = temp;
    quickSort(a,start,hole-1);
    quickSort(a,hole+1,ends);
}

template <class elemType>
void quickSort(elemType a[], int n)
{
    quickSort(a,0,n-1);
}

template <class elemType>
void selectSort(elemType a[], int n)
{
    int i, j, minIndex;
    elemType temp;
    for (i = 0; i<n;i++)
    {
        minIndex = i;
        for (j = i+1; j<n;j++)
        {
            if (a[j] < a[minIndex])
            {
                minIndex = j;
            }
        }
        if (minIndex == i) continue;
        temp = a[i];
        a[i] = a[minIndex];
        a[minIndex] = temp;
    }
}

template <class elemType>
void adjust(elemType a[], int n, int i)
{
    int maxChild;
    elemType temp;
    while(true)
    {
        maxChild = 2*i+1;
        if (maxChild >n-1) return;
        if (maxChild+1 <= n-1)
        {
            if (a[maxChild+1] >= a[maxChild]) maxChild++;
        }
        if (a[i] > a[maxChild]) return;
        temp = a[i];
        a[i] = a[maxChild];
        a[maxChild] = temp;
        i = maxChild;
    }
}

template <class elemType>
void heapSort(elemType a[], int n)
{
    int i,j;
    elemType temp;
    for (i = (n/2-1); i>= 0; i--)
    {
        adjust(a,n,i);
    }
    for (j =n-1;j>=1;j--)
    {
        temp = a[0];
        a[0] = a[j];
        a[j] = temp;
        adjust(a,j,0);
    }
}
int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
