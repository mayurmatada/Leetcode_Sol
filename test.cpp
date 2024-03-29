#include<iostream>
using namespace std;

#define l1 long long
#define ar array

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin>>t;
	while(t--)
	{
        int count = 0;
        long long n, f, a, b;
        vector<long long>m;
        cin>>n>>f>>a>>b;
        for(long long i=0;i<n;i++)
        {
            cin>>m[i];
        }
        if(a*m[0]>=b)
        {
            f = f - b;
            if(f<=0)
                    {
                        cout<<"NO\n";
                        continue;
                    }

        }
        else
        {
            f = f - a*m[0];
            if(f<=0)
                    {
                        cout<<"NO\n";
                        continue;
                    }
        }
        for(long long i = 0;i<n-1;i++)
        {
            if(n!=1)
            {
                if(a*(m[i+1]-m[i])>=b)
                {
                    f = f - b;
                    if(f<=0)
                    {
                        cout<<"NO\n";
                        break;
                    }
                }
                else if(a*(m[i+1]-m[i])<b)
                {
                    f = f - a*(m[i+1]-m[i]);
                    if(f<=0)
                    {
                        cout<<"NO\n";
                        break;
                    }
                }
            }

        }
        if(f>0)
        {
            cout<<"YES\n";
            continue;
        }

        }
}