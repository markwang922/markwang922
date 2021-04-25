

public class MathAndNumber {
    public static void main(String[] args){
        System.out.println(Math.PI);
        System.out.println(Math.toDegrees((Math.PI / 2)));

        double[] nums = { 1.4, 1.5, 1.6, -1.4, -1.5, -1.6 };   
        for (double num : nums) {   
            test(num);   
            }   
        }
  
    private static void test(double num) {   
        System.out.println("Math.floor(" + num + ")=" + Math.floor(num));   
        System.out.println("Math.round(" + num + ")=" + Math.round(num));   
        System.out.println("Math.ceil(" + num + ")=" + Math.ceil(num));  
    }
}
