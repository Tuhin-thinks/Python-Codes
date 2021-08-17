package com.company;

import java.util.Scanner;

import static java.lang.System.in;

/**
 *The Newton-Raphson method (also known as Newton's method) is a way to quickly find a good approximation for the
 *  root of a real-valued function f(x)=0f(x) = 0f(x)=0.
 * It uses the idea that a continuous and differentiable function can be approximated by a straight line tangent to it.
 */
public class Main {
    public static double EPSILON= 0.0001;

    double Func(double x){
        return (x*x*x) - (3*x) - 5;
    }

    double derivFunc(double x){
        return 3 * (x * x) - 3;
    }

    public static void main(String[] args) {
	// write your code here
        Main obj = new Main();

        double x_n, x_n1;

        System.out.print("Enter initial value of x (x0)=");
        Scanner sc = new Scanner(in);
        String x_0 = sc.nextLine();
        x_n = Double.parseDouble(x_0);  // initial double value of X0
        x_n1 = x_n;

        int iteration_count=1;
        double h = obj.Func(x_n) / obj.derivFunc(x_n);
        while (Math.abs(h) >= EPSILON){
            h = obj.Func(x_n) / obj.derivFunc(x_n);
            x_n1 = x_n - h;
            x_n = x_n1;
            System.out.printf("x_%d=%.4f\n", iteration_count++ , x_n1);
        }
        System.out.printf("\nRoot of the equation (using Newton Raphson's method): %.4f", x_n1);
    }
}
