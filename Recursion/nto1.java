class nto1{
    static void n(int x){
        if (x==0){
            return ;
        }
        System.out.println(x);
        n(x-1);
    }
    public static void main(String[] args)  {
     n(10);
    }
    
}