#include <iostream>

#include<bits/stdc++.h>

using namespace std;

#define ll long long int

template <typename T>istream &operator>>(istream &in,
vector<T> &a) {for (auto &x : a)in >> x; return in;};

template <typename T>ostream &operator<<(ostream &out,
vector<T> &a) {for (auto &x : a)out << x <<' '; return out;};

template <typename T1, typename T2>ostream
&operator<<(ostream &out, const pair<T1, T2> &x) { return out <<
x.ff<<' ' << xss; }
template <typename T1, typename T2>istream
&operator>>(istream &in, pair<T1, T2> &x) { return in >> x.ff >> x.ss;}

void solve(){
ll n;
cin>>n;
ll v = sqrt(n);
for (ll k = 2; k <= v; k++) {
ll x=1;
while (pow(k, x - 1) <= n) {
    x++;
}
for (ll i=1;i<=x+1;i++){
    ll m = (pow(k, i) - 1) / (k - 1);
    if (m==n) {
        cout << "YES" << endl;
        return;
    }
}
}
cout << "NO" << endl;
}
int main() {
int t;
cin>>t;
while(t--){
solve();
}
return 0;

}
