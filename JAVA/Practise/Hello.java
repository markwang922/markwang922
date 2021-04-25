/*
修饰符 	当前类 	同一包内 	子孙类(同一包) 	子孙类(不同包) 	其他包
public 	Y 	Y 	Y 	Y 	Y
protected 	Y 	Y 	Y 	Y/N（说明） 	N
default 	Y 	Y 	Y 	N 	N
private 	Y 	N 	N 	N 	N
*/

public class Hello {
    
    public static void main(String[] args){
        System.out.println("Hello world...");

        System.out.println("\n******************** \n");

        System.out.println("请注意以下方法继承的规则\n" +
        
            "父类中声明为 public 的方法在子类中也必须为 public.\n" +
        
            "父类中声明为 protected 的方法在子类中要么声明为 protected，要么声明为 public，不能声明为 private。\n" +
        
            "父类中声明为 private 的方法，不能够被继承. \n");
    }
}