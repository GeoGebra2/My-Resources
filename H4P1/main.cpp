#include <iostream>
#include <vector>

using namespace std;

struct Fish
{
    int fishNum = 0;
    int flag = 0;
};

int GetMostFish(vector<vector<Fish>>&pool, int height, int width,int x, int y)
{
    //cout << "come to " << x << " " << y << " " << pool[x][y].fishNum << endl;
    if (pool[x][y].fishNum == 0 || pool[x][y].flag == 1)
    {
        return 0;
    }
    //cout << "add " << x << " " << y << endl;
    pool[x][y].flag = 1;
    return pool[x][y].fishNum + GetMostFish(pool, height, width, x+1, y)+GetMostFish(pool, height, width, x, y+1)+GetMostFish(pool, height, width, x, y-1) + GetMostFish(pool, height, width, x-1, y);

}

int main()
{
    int height, width;
    cin >> height >> width;
    vector<vector<Fish>> pool(height+2, vector<Fish>(width+2));
    for (int i = 1; i < height+1; i++)
    {
        for (int j = 1; j < width+1; j++)
        {
            cin >> pool[i][j].fishNum;
        }
    }
/*
    for (int i = 0; i < height+2; i++)
    {
        for (int j = 0; j < width+2; j++)
        {
            cout << pool[i][j].fishNum <<" ";
        }
        cout << endl;
    }*/
    int MaxNum = 0;
    int tempNum = 0;
    for (int i = 1; i < height+1; i++)
    {
        for (int j = 1; j < width+1; j++)
        {
            tempNum = GetMostFish(pool, height, width, i, j);
            //cout << "get " << tempNum << endl;
            if (tempNum > MaxNum)
            {
                MaxNum = tempNum;
            }
        }
    }
    cout << MaxNum << endl;

    return 0;
}
