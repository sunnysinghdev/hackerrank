using System;

namespace build_string
{
    public class Factorial
    {
        static double factorial(double n, int a)
        {
            Console.WriteLine(a);
            if (n == 0 || n == 1)
            {
                return 1;
            }
            return n * factorial(n - 1, a + 1);
        }
        static double factorialTR(double n, double b, int a)
        {
            Console.WriteLine(a);
            if (n == 0 || n == 1)
            {
                return b;
            }
            return factorialTR(n - 1, n + b, a + 1);
        }
    }
}