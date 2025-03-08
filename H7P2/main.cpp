#include <iostream>

using namespace std;

int AlphaNum, WordNum;
char alpha[100];
string word[1000];

int CompareAlpha(char a, char b)
{
    for (int i = 0; i < AlphaNum; i++){
        if (alpha[i] == a && a == b){
            return 0;
        }
        else if (alpha[i] == a && alpha[i] != b){
            return -1;
        }
        else if (alpha[i] == b && alpha[i] != a){
            return 1;
        }
    }
    cout << "alpha compare error" << endl;
    return -2;
}
int CompareWord(string a, string b)
{
    int len = min(a.size(), b.size());
    for (int i = 0; i < len; i++){
        if (CompareAlpha(a[i], b[i]) == -1){
            return -1;
        }
        else if (CompareAlpha(a[i], b[i]) == 1){
            return 1;
        }
    }
    if (a.size() < b.size()){
        return -1;
    }
    else if (a.size() > b.size()){
        return 1;
    }
    else{
        return 0;
    }
}

void MyMerge(string a[], int low, int mid, int high)
{
    int i,j,k;
    string *c;
    c = new string[high-low+1];
    i = low;
    j = mid+1;
    k=0;
    while((i<=mid)&&(j<=high))
    {
        //if (a[i] <= a[j])
        if (CompareWord(a[i], a[j]) != 1)
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

void mergeSort(string a[], int low, int high)
{
    int mid;
    if (low >= high) return;
    mid = (low + high) /2;
    mergeSort(a, low, mid);
    mergeSort(a, mid+1, high);
    MyMerge(a, low, mid, high);
}

void mergeSort1(string a[], int n)
{
    mergeSort(a, 0, n-1);
}



int main()
{
    //int AlphaNum, WordNum;
    cin >> AlphaNum >> WordNum;
    string temp;
    //char alpha[AlphaNum];
    //string word[WordNum];
    for (int i = 0; i < AlphaNum; i++){
        cin >> alpha[i];
    }
    getline(cin, temp);
    for (int i = 0; i < WordNum; i++){
        getline(cin, word[i]);
    }
    mergeSort1(word, WordNum);
    for (int i = 0; i < WordNum; i++){
        cout << word[i] << endl;
    }

    return 0;
}
