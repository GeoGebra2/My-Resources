#include <iostream>
#include <stack>
#include <sstream>

using namespace std;

void inToSufForm(char *inStr, char *sufStr)
{
    stack<char> s;
    int i, j;
    char topCh;
    s.push('#');
    while(inStr[i] != '@')
    {
        if ((inStr[i] >= '0') && (inStr[i] <= '9'))
        {
            sufStr[j++] = inStr[i++];
        }
        else
        {
            switch (inStr[i])
            {
                case '(':s.push('('); break;
                case ')': topCh = s.top();
                        s.pop();
                        while (topCh!='(')
                        {
                            sufStr[j++] = topCh;
                            topCh = s.top(); s.pop();
                        }
                         break;
                case '*':
                case '/': topCh = s.top();
                        while ((topCh=='*')||(topCh=='/'))
                                //*、/为左结合，故后来者优先级低
                        {
                            s.pop();
                            sufStr[j++] = topCh;
                            topCh = s.top();
                        }
                        s.push(inStr[i]);
                        break;
                case '+':
                case '-':topCh = s.top();
                        while ((topCh!='(')&&(topCh!='#'))
                                //只有左括号和底垫优先级比+、-低
                        {
                            s.pop();
                            sufStr[j++] = topCh;
                            topCh = s.top();
                        }
                        s.push(inStr[i]);
                        break;
            }
        }
    }
}

int main()
{
    //char inStr[10000], sufStr[10000];
    //char temp;
    int leftKH = -1, right_KH = -2, sum = -3, minu = -4, multiple = -5, slash = -6;
    int tmp, i = 0, j = 0, topCh;
/*
    for (int i = 0; i < 10000; i++)
    {
        cin >> temp;
        inStr[i] = temp;
        if (temp == '@')
        {
            break;
        }
    }*/
    string inStr;
    getline(cin, inStr);
    //cout << inStr << endl;
    stack<int> s;
    int sufStr[inStr.size()+1] = {0};
    //cout << inStr.size()+1 << endl;
    s.push(0);
    //i = 0;
    while(inStr[i]!='@')
    {
        //cout << inStr[i] << endl;
        if (inStr[i] == '.')
        {
            i++;
            continue;
        }
        else if ((inStr[i]>='0')&&(inStr[i]<='9'))
        {
            //cout << "number" << endl;
            string number = "";
            while (inStr[i] != '.')
            {
                number += inStr[i];
                i++;
            }
            std::istringstream ss(number);
            ss >> tmp;
            sufStr[j++] = tmp;
        }
        else
        {
            //cout << "op" << endl;
            switch (inStr[i])
            {
                case '(':s.push(leftKH); break;
                case ')': topCh = s.top();
                        s.pop();
                        while (topCh!=leftKH)
                        {
                            sufStr[j++] = topCh;
                            topCh = s.top();
                            s.pop();
                        }
                         break;
                case '*':
                case '/': topCh = s.top();
                        while ((topCh==multiple)||(topCh==slash))
                        {
                            s.pop();
                            sufStr[j++] = topCh;
                            topCh = s.top();
                        }
                        if (inStr[i] == '*')
                        {
                            s.push(multiple);
                        }
                        else
                        {
                            s.push(slash);
                        }

                        break;
                case '+':
                case '-':topCh = s.top();
                        while ((topCh!=leftKH)&&(topCh!=0))
                        {
                            s.pop();
                            sufStr[j++] = topCh;
                            topCh = s.top();
                        }
                        if (inStr[i] == '+')
                        {
                            s.push(sum);
                        }
                        else
                        {
                            s.push(minu);
                        }
                        break;
            }
            i++;
        }
    }
    while(s.top() != 0)
    {
        sufStr[j++] = s.top();
        s.pop();
    }
    //cout << j << endl;
    sufStr[j] = -7;
    for (int k = 0; k <= inStr.size()+1; k++)
    {
        if (sufStr[k] == -7)
        {
            cout << '@' << endl;
            break;
        }
        else if (sufStr[k] >= 0)
        {
            cout << sufStr[k] << '.';
        }
        else
        {
            switch(sufStr[k])
            {
                case -1:cout << '('; break;
                case -2:cout << ')'; break;
                case -3: cout << '+'; break;
                case -4: cout << '-'; break;
                case -5: cout << '*'; break;
                case -6: cout << '/'; break;
            }
        }
    }

    return 0;
}
