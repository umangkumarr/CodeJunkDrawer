#include<iostream>
using namespace std;

long long mux(int a, int b , long long m){
    if(m> )
}

int main(){
    int t; cin>>t;
    while(t--){
        int n; cin>>n;
        int arr[n];
        long long int m = 0
        cin>>arr[0];
        for(int i=1;i<n;i++){
            cin>>arr[i];
            if(m< (arr[i-1]*arr[i])){
                m=arr[i-1]*arr[i];
            }
        }
        cout<<m<<endl;
    }
}