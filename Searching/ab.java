import java.util.*;
public class Main {
    public static int findMax(int[] g, int[] h, int firs, int sec, int[][] dp){
        if(h.length == sec){
            return 0;
        }
        if(g.length == firs){
            return 0;
        }

        if(dp[firs][sec] != -1){
            return dp[firs][sec];
        }
        int a=0, b=0, c=0;
        if(g[firs] == h[sec]){
            return findMax(g,h,firs+1,sec+1, dp)+1;
        }
            a = findMax(g,h,firs+1,sec,dp);
            b = findMax(g,h,firs,sec+1,dp);
        

        return dp[firs][sec] = Math.max(a,b);
    }
    public static void main (String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] x = new int[n];
        int[] y = new int[m];
        for(int i=0;i<n;i++){
            x[i] = sc.nextInt();
        }
        for(int j=0;j<m;j++){
            y[j] = sc.nextInt();
        }

        int[][] dp = new int[n][m];
        for(int arr[]: dp){
            Arrays.fill(arr,-1);
        }

        System.out.println(findMax(x,y,0,0,dp));
        

    }
}