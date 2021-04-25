public class ArithmeticalOP {
    public static void main(String[] args) {
        // int a = 10;
        // int b = 20;
        // int c = 25;
        // int d = 25;
        // System.out.println("a + b = " + (a + b) );
        // System.out.println("a - b = " + (a - b) );
        // System.out.println("a * b = " + (a * b) );
        // System.out.println("b / a = " + (b / a) );
        // System.out.println("b % a = " + (b % a) );
        // System.out.println("c % a = " + (c % a) );
        // System.out.println("a++   = " +  (a++) );
        // System.out.println("a--   = " +  (a--) );
        // System.out.println("a  = " +  a );
        // // 查看  d++ 与 ++d 的不同
        // System.out.println("d++   = " +  (d++) );
        // // d++ means return d first, ant then +1
        // System.out.println("d  = " +  d );
        // System.out.println("++d   = " +  (++d) );
        // // ++d means +1 first, and then return d
        // System.out.println("d  = " +  d );

        System.out.println("\n***************************\n");

        // int i = 1;
        // i = i++;
        // System.out.println("i=" + i);
        // int j = i++;
        // System.out.println("i=" + i);
        // System.out.println("j=" + j);
        // int k = i + ++i * i++;
        // System.out.println("i="+i);
        // System.out.println("j="+j);
        // System.out.println("k="+k);

        int a = 5;
        int b = 5;
        int x = 2*++a;  // which means 2 x (a + 1) = 12, a = 6
        int y = 2*b++;  // which means 2 x b = 10, and then b + 1, b = 6
        System.out.println("自增运算符前缀运算后a="+a+",x="+x);
        System.out.println("自增运算符后缀运算后b="+b+",y="+y);
        
        System.out.println("\n***************************\n");
     }
}
