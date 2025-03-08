#include <iostream>
#include <sstream>

using namespace std;

class seqStack
{
private:
    int *CalArray;
    int Top;
    int maxSize;

public:
    seqStack(int initSize = 100);
    bool isEmpty() { return ( Top == -1 ); } ;
    bool isFull() { return (Top == maxSize-1); };
    int top();
    void push (const int &e );
    void pop();
    seqStack(){ delete []CalArray;};
};

seqStack::seqStack(int initSize)
{
    CalArray = new int[initSize];
	Top=-1;
	maxSize=initSize;
}

int seqStack::top()
{
    if (isEmpty()){
        cout << "Stack is Empty" << endl;
        return 0;
    }
    return CalArray[Top];
}

void seqStack::push(const int &e)
{
    if (isFull())
    {
        cout << "Stack is full" << endl;
    }
     CalArray[++Top] = e;
}

void seqStack::pop()
{
    if (Top==-1)
    {
        cout << "Stack is empty" << endl;
        return;
    }
    Top--;
    return;
}

int main()
{

    int op1, op2, op;
    int tmp, i;

    string sufStr;
    getline(cin, sufStr);
    seqStack s(sufStr.size());
    i = 0;
    while (sufStr[i]!='@')
    {
        if (sufStr[i] == '.')
        {
            continue;
        }

        if ((sufStr[i]>='0')&&(sufStr[i]<='9'))
        {
            string number = "";
            while (sufStr[i] != '.')
            {
                number += sufStr[i];
                i++;
            }
            std::istringstream ss(number);
            ss >> tmp;
            s.push(tmp);
        }
        else
        {
            op2 = s.top();
            s.pop();
            op1 = s.top();
            s.pop();
            switch (sufStr[i])
            {   case '*': op = op1*op2; break;
                case '/': op = op1/op2; break;
                case '+': op = op1+op2; break;
                case '-': op = op1-op2; break;
            };
            s.push(op);
        }
        i++;
    }
    op = s.top();
    s.pop();
    cout << op << endl;
    return 0;
}
