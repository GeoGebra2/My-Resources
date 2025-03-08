#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main()
{
    vector<string> code, origin;
    string str = "a";
    bool HaveFind = false;
    while(str != "$")
    {
        cin >> str;
        origin.push_back(str);
    }
    str = "a";
    while(str != "$")
    {
        cin >> str;
        code.push_back(str);
    }
    for (int i = 0; i < origin.size()-code.size()+1; i++)
    {
        map<string, string> Hashi;
        for (int j = i; j < i + code.size(); j++)
        {

            if (code[j-i] == "$")
            {
                HaveFind = true;
                cout << i+1;
                break;
            }
            map<string, string>::iterator it = Hashi.find(code[j-i]);
            if (it == Hashi.end())
            {
                //cout << "create" << endl;
                //cout << code[j-i] << " " << origin[j] << endl;
                Hashi[code[j-i]] = origin[j];
                Hashi.insert(pair<string ,string>(code[j-i],origin[i]));

            }
            else
            {
                //cout << "compare" << endl;
                //cout << Hashi[code[j-i]] << " " << origin[j] << endl;
                if (Hashi[code[j-i]] != origin[j])
                {
                    break;
                }
                else
                {
                    continue;
                }
            }
        }
        if (HaveFind)
        {
            break;
        }
    }
    return 0;
}
