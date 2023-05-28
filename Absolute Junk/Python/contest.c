
#include<stdio.h>
int main()
{
    int t;
    scanf("%d",&t);
    while(t--){
        int n;
        scanf("%d",&n);
        int g=2,d=1;
        if(n%2==0){
            g=1; d=2;
        }
        long long arr[n+1];
        long long dp[n+3];
        dp[0]=0;dp[1]=0;
        for(int i=0;i<n;i++){
            scanf("%lld",&arr[i]);
            dp[i+2]=dp[i]+arr[i];
        }
        int m=-1;
        for(int j=2;j<n+2;j++){
            int num=arr[j-2];
            if(j%2==0){
                long odd=dp[j-1]+dp[n-g+2]-dp[j];
                long even=dp[j-2]-dp[j-1]+dp[n-d+2];
                if(odd==even){
                    if (m<num){
                        m=num;
                    }
                }
            }else{
                long even=dp[j-1]+dp[n-g+2]-dp[j];
                long odd=dp[j-2]-dp[j-1]+dp[n-d+2];
                if(odd==even){
                    if (m<num){
                        m=num;
                    }
                }
            }
        }
        printf("%d\n",m);
    }
}