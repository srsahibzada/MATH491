import java.util.Random;
import java.util.ArrayList;

public class EuclideanAlg{	
    public static int gcd(int p, int q) {
        int i = 0;
        while (q != 0) {
            int temp = q;
            q = p % q;
            p = temp;
            i++;
        }
        return i;
    }
    
    public static void main(String[] args) {
    	Random rand = new Random();
		
        int p = rand.nextInt(100) + 1;
        int q = rand.nextInt(100) + 1;
        int d  = gcd(p, q);
        System.out.println("Number of iterations for " + "gcd(" + p + ", " + q + "): " + d);
    }
}