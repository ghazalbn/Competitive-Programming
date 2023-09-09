#include <bits/stdc++.h>
using namespace std;

#define int long long 
#define ll int
#define F first
#define S second
#define pii pair<ll, ll>
#define pb push_back
#define endl '\n'
#define ENDL " \n"[i == n - 1]
#define migmig ios::sync_with_stdio(false), cin.tie(0), cout.tie(0);
#define file_io freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout)
#define RESET   "\033[0m"
#define RESET   "\033[0m"
#define BLACK   "\033[30m"      /* Black */
#define RED     "\033[31m"      /* Red */
#define GREEN   "\033[32m"      /* Green */
#define YELLOW  "\033[33m"      /* Yellow */
#define BLUE    "\033[34m"      /* Blue */
#define MAGENTA "\033[35m"      /* Magenta */
#define CYAN    "\033[36m"      /* Cyan */
#define WHITE   "\033[37m"      /* White */

const ll maxn = 1e5 +10;
ll mark[maxn];

int32_t main()
{
  //Dont Forget The ''Map''  :)
  
  migmig;
  
  ll t;
  cin >> t;
  while(t--)
  {
    ll n, is[2] = {0, 0};
    vector <pii> v;
    cin >> n;
    pii a[n];
    for(int i = 0; i < n; i++)
    {
      cin >> a[i].F;
      a[i].F == 1 ? is[0]++ : is[1]++;
      a[i].S = i + 1;
    }
    if(is[0] && is[1])
      cout << -1 << endl;
    else
    {
      sort(a, a + n);
      while(a[0].F != a[n - 1].F)
      {
        a[n - 1].F = a[n - 1].F / a[0].F + (a[n - 1].F % a[0].F != 0);
        v.pb({a[n - 1].S, a[0].S});
        sort(a, a + n);
      }
      cout << v.size() << endl;
      for(auto i : v) cout << i.F << ' ' << i.S << endl;
    }

  } 
}