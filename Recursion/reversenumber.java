import java.util.Scanner;

class reversenumber{
    static int sum=0;
    static void reverse(int a){
        if (a==0){
            return ;
        }
        int re=a%10;
        sum=sum*10+re;
        reverse(a/10);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a= sc.nextInt();
        reverse(a);
        System.out.println(sum);     
    }
    
}