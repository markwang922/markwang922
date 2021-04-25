public class ByteOp {
    public static void main(String[] args){
        // int a = 60; /* 60 = 0011 1100 */ 
        // int b = 13; /* 13 = 0000 1101 */
        // int c = 0;

        // c = a & b;
        // System.out.println(c);

        // c = a | b;
        // System.out.println(c);  // 00111101

        // c = a ^ b;
        // System.out.println(c);  // 00110001

        // c = ~ a;
        // System.out.println(c);  

        // a = a >> 1;
        // System.out.println(a);

        // a = a << 1;
        // System.out.println(a);

        /*
        当使用与逻辑运算符时，在两个操作数都为true时，结果才为true;
        但是当得到第一个操作为false时，其结果就必定是false，这时候就不会再判断第二个操作了。
        */

        // int a = 5;//定义一个变量；
        // boolean b = (a<4)&&(a++<10);
        // System.out.println("使用短路逻辑运算符的结果为"+b);
        // System.out.println("a的结果为"+a);  // cause a<4, a++<10 would not be operated, a = 5 still.

        // variable x = (expression) ? value if true : value if false

        int a , b;
        a = 10;
        // 如果 a 等于 1 成立，则设置 b 为 20，否则为 30
        b = (a == 1) ? 20 : 30;
        System.out.println( "Value of b is : " +  b );
   
        // 如果 a 等于 10 成立，则设置 b 为 20，否则为 30
        b = (a == 10) ? 20 : 30;
        System.out.println( "Value of b is : " + b );
    }
}
