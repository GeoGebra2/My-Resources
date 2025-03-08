#include <iostream>

using namespace std;

bool isUgly(int x)
{
    //int temp = x;
    if (x == 1)
    {
        return true;
    }
    while(x % 2 == 0)
    {
        x /= 2;
    }
    while(x % 3 == 0)
    {
        x /= 3;
    }
    while( x % 5 == 0)
    {
        x /= 5;
    }
    return x == 1;

}

int main()
{
    int target;
    cin >> target;
    int index = 0, number = 1;
    while(index < target)
    {
        if (isUgly(number))
        {
            //cout << number << " " << index << endl;
            index++;
        }
        number++;
    }
    cout << number-1 << endl;
    return 0;
}
