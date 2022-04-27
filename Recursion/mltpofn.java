class mltpofn{
    public static void main(String[] args) {
        System.out.println(mltp(10));
    }
    static int mltp(int x){
        if(x==0){
            return 1;
        }
        return x*mltp(x-1);
    }
}