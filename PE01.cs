using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Diagnostics;

namespace ProjectEuler
{
    /* Problem 1
       If we list all the natural numbers below 10 that are multiples of 3 or 5,
       we get 3, 5, 6 and 9. The sum of these multiples is 23.

       Find the sum of all the multiples of 3 or 5 below 1000.*/

    // Answer: 233168
    class PE01
    {
        static void Main(string[] args)
        {
            Stopwatch timer = new Stopwatch();
            timer.Start();
            int limit = 1000;

            int sum = Enumerable.Range(1, limit - 1).Where(n => (n % 3 == 0) || (n % 5 == 0)).Sum();
            timer.Stop();
            Console.WriteLine(sum);
            Console.WriteLine("Time elapsed: " + timer.Elapsed.ToString());
            Console.ReadKey();
        }
    }
}
