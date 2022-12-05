#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		int a[n];
		for(int i=0;i<n;i++)
			cin>>a[i];
		int max=a[n-1];
		for(int i=n-2;i>=0;i--)
		{
			if(a[i]>=max)
				max=a[i];
			else
				a[i]=-1;
		}
		for(int i=0;i<n;i++)
			if(a[i]!=-1)
				cout<<a[i]<<" ";
		cout<<endl;
	}
	return 0;
}