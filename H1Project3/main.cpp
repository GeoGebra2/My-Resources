#include <iostream>

using namespace std;

int main()
{
    int Num;
    int Matrix[9][9];
    int ZeroToNine[9];
    int Answer[Num];
    string tmp;

    cin >> Num;
    for (int i = 0; i < Num; i++)
    {
        bool isRight = true;
        for (int j = 0; j < 9; j++)
        {
            ZeroToNine[j] = 0;
        }
        for (int j = 0; j < 9; j++)
        {
            for (int k = 0; k < 9; k++)
            {
                cin >> Matrix[j][k];
            }
        }
        //getline(cin, tmp);
        for (int j = 0; j < 9; j++)
        {
            for (int k = 0; k < 9; k++)
            {
                if (ZeroToNine[Matrix[j][k] - 1] != 0)
                {
                    //cout << "Wrong" << endl;
                    Answer[i] = 0;
                    isRight = false;
                    break;
                }
                else
                {
                    ZeroToNine[Matrix[j][k] - 1] = 1;
                }
            }
            if (!isRight)
            {
                break;
            }
            for (int j = 0; j < 9; j++)
            {
                ZeroToNine[j] = 0;
            }
        }
        if (!isRight)
        {
            continue;
        }

        //for (int j = 0; j < 9; j++)
        //{
         //   ZeroToNine[j] = 0;
        //}

        for (int j = 0; j < 9; j++)
        {
            for (int k = 0; k < 9; k++)
            {
                if (ZeroToNine[Matrix[k][j] - 1] != 0)
                {
                    //cout << "Wrong" << endl;
                    Answer[i] = 0;
                    isRight = false;
                    break;
                }
                else
                {
                    ZeroToNine[Matrix[k][j] - 1] = 1;
                }
            }
            if (!isRight)
            {
                break;
            }
            for (int j = 0; j < 9; j++)
            {
                ZeroToNine[j] = 0;
            }
        }
        if (!isRight)
        {
            continue;
        }
        /*
        for (int j = 0; j < 9; j++)
        {
            ZeroToNine[j] = 0;
        }*/

        for (int j = 0; j < 3; j++)
        {
            for (int k = 0; k < 3; k++)
            {

                for (int p = 0; p < 3; p++)
                {
                    for (int q = 0; q < 3; q++)
                    {
                        //cout << Matrix[3*j + p][3*k + q] << endl;
                        //for (int t = 0; t < 9; t++)
                        //{
                         //   cout << ZeroToNine[t] << " ";
                        //}
                        if (ZeroToNine[Matrix[3*j + p][3*k + q] - 1] != 0)
                        {
                            //cout << "Wrong" << endl;
                            Answer[i] = 0;
                            isRight = false;
                            break;
                        }
                        else
                        {
                            ZeroToNine[Matrix[3*j + p][3*k + q] - 1] = 1;
                        }
                    }
                    if (!isRight)
                    {
                        break;
                    }
                }
                if (!isRight)
                {
                    break;
                }
                for (int j = 0; j < 9; j++)
                {
                    ZeroToNine[j] = 0;
                }
            }
            if (!isRight)
            {
                break;
            }
        }
        if (!isRight)
        {
            continue;
        }
        //cout << "Right" << endl;
        Answer[i] = 1;
    }

    for (int i = 0; i < Num; i++)
    {
        if (Answer[i] == 1)
        {
            cout << "Right" << endl;
        }
        else{
            cout << "Wrong" << endl;
        }
    }
    return 0;
}
