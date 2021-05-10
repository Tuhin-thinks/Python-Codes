import java.util.Arrays;
import java.util.Scanner;

public class factorial {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        while (T-- > 0){
            Solution obj = new Solution();
            int N;

            N = sc.nextInt();

            System.out.println(obj.factorial(N));
        }
    }
}
class Solution{
    int multiply(int x, int[] res, int res_size){
        int carry = 0;
        for (int i=0; i < res_size; i++){
            int prod = res[i] * x + carry;
            res[i] = prod % 10;
            carry = prod/10;
        }

        while (carry != 0){
            res[res_size] = carry % 10;
            carry /= 10;
            res_size ++;
        }
        return res_size;
    }

    public long factorial(int N){
        int[] res = new int[1000];

        res[0] = 1;
        int res_size = 1;

        for (int x=2; x<= N; x++){
            res_size = multiply(x, res, res_size);
        }

        long fact = 0;
        for (int index = res_size - 1; index >= 0; index--){
            fact = (long) Math.pow(10,index) * res[index] + fact;
        }
        return fact;
    }
}