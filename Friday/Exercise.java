public class Exercise {
    public static void main(String[] args) {

        System.out.println("================================================ Initial Values ================================================");
        int a = 10;
        int b = 20;
        
        System.out.println("Initial A: " + a);
        System.out.println("Initial B: " + b);

        System.out.println("================================================ After Swapping ================================================");
        
        int c = a; 
        a = b;
        b = c;

        System.out.println("Value A: " + a);
        System.out.println("Value B: " + b);
    }
}