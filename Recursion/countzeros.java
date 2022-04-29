import java.util.Scanner;

public class countzeros {
    static int count=0;
    static int zeros(int a,int count){
        if(a==0){
            return count;
        }
        int re=a%10;
        if(re==0){
            return zeros(a/10,count+1);
        }
        else{
        return zeros(a/10, count);
        }

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a= sc.nextInt();
        System.out.println( zeros(a, count));
        
    }
    
}
