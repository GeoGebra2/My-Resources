#include <iostream>

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
    int StackNum, NumberNum;
    int current, present;
    cin >> StackNum;
    int Answer[StackNum];
    for (int i = 0; i < StackNum; i++)
    {
        //cout << "round: " << i << endl;
        int ClockNum = 0;
        bool isFalse = false;
        cin >> NumberNum;
        seqStack* InputNum = new seqStack(NumberNum+1);
        present = 0;
        for (int j = 0; j < NumberNum; j++)
        {
            cin >> current;
            //cout << "current: " << current << endl;
            if (isFalse)
            {
                continue;
            }
            if (current > present)
            {
                //cout << "here" << endl;
                for (int k = ClockNum+1; k <= current; k++)
                {
                    InputNum->push(k);
                }
                //cout << "top: " << InputNum->top() << " clock: " << ClockNum << endl;
                InputNum->pop();
                ClockNum = current;
                present = current;
                //
                /*
                while(!InputNum->isEmpty())
                {
                    if(InputNum->top() != ClockNum)
                    {
                        //cout << "top: " << InputNum->top() << " clock: " << ClockNum << endl;
                        Answer[i] = 0;
                        isFalse = true;
                        break;
                    }

                    InputNum->pop();
                    ClockNum++;
                }
                if (!isFalse)
                {
                    InputNum->push(current);
                    present = current;
                }*/

            }
            else
            {
                //cout << "here else" << endl;
                //cout << "top: " << InputNum->top() << " current: " << current << endl;
                if (current != InputNum->top())
                {
                    Answer[i] = 0;
                    isFalse = true;
                    //break;
                }
                InputNum->pop();
            }
        }
        if (!isFalse)
        {
            Answer[i] = 1;
        }

    }

    for(int i = 0; i < StackNum; i++)
    {
        if (Answer[i] == 0)
        {
            cout << "No" << endl;
        }
        else
        {
            cout << "Yes" << endl;
        }
    }
    return 0;
}
