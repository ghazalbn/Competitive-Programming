#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
int t;
cin>>t;

while (t> 0) {
string s;
cin>>s;

vector<vector<int>> pos(10);
vector<int> idx(10, 0);
for(int i = 0; i < s.length(); i++) {
    int digit = s[i] - '0';
    pos[digit].push_back(i);
}

int m;
cin>>m;
string Ir, rr;
cin >>Ir>>rr;
int cpos = 0;
for (int i=0;i<m;i++){
for (int j=0;j< 10; j++) {
while (idx[j] < pos[j].size() && pos[j][idx[j]] < cpos) {
idx[j]++;
}
}

int pck = cpos;
for (int j = Ir[i] - '0'; j <= rr[i]-'0'; j++) {
if (idx[j] >= pos[j].size()) {
pck = s.length();
}else{
pck = max(pck, pos[j][idx[j]]);
}
}

cpos = pck +1;
}

if (cpos >= s.length() + 1) {
cout << "YES" << endl;
}else{
cout << "NO" << endl;

}

t--;
}

return 0;
}