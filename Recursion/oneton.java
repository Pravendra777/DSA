class oneton{

    public static void main(String[] args) {
        n(10);
    }
    static void n(int x){
        if(x==0){
            return;
        }
        n(x-1);
        System.out.println(x);
    }



}