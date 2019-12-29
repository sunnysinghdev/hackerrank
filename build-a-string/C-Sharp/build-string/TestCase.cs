using System;
using System.Collections.Generic;
using System.IO;

namespace build_string
{
    public class TestCase
    {
        public static void tes_case0()
        {
            printv(4, 5, "aabaacaba", 26);
            printv(8, 9, "bacbacacb", 42);

        }
        public static void test_case1()
        {
            string case1 = "caaahqcqes";
            printv(2, 3, case1, 20);
            case1 = "acbbqbbqbb";
            printv(1, 4, case1, 10);
            case1 = "cbabecbahe";
            printv(2, 4, case1, 18);
        }
        
        public static void test_case5()
        {
            string case1 = "caackncaacknggikncaacknggaacknggikncaackggikncaacknggaacknggikncakqoaacknggikncacggihikncaomhikncaom";
            printv(2709, 2712, case1, 65040);

            case1 = "acbcrsjcrscrsjcrcbcrsjcrscrsjccbcrsjcrscrsjcrcbcrsjrscrsjcrcbcrsjcrscrsjccbcrsjcrscrsjcrcbcsbcbcrsjh";
            printv(7890, 7891, case1, 126246);

            case1 = "abbciabbcabciabbcmabbciabbcahlbchgcmabbcmggcmababciabbcagerafrciabbcsrhgcmcabciabbchgcmabbcmsfabcmsr";
            printv(7078, 7078, case1, 268964);
        }
        public static void test_case20()
        {
            string case1 = "";
            case1 = getString("..\\..\\case20.txt");
            printv(6647, 6650, case1, 771187);

            case1 = getString("..\\..\\case20_a.txt");
            printv(7246, 7246, case1, 2514362);

            case1 = getString("..\\..\\case20_b.txt");
            printv(3195, 3198, case1, 24025545);
        }
        public static void test_case11()
        {
            int[] ot = { 400809, 729904, 32225646 };
            string line = "";
            try
            {
                System.IO.StreamReader file = new System.IO.StreamReader("..\\..\\case11.txt");

                line = file.ReadLine().Replace("\n", "");
                int num = int.Parse(line);
                for (int i = 0; i < num; i++)
                {
                    string[] nums = file.ReadLine().Split(' ');
                    line = file.ReadLine();
                    printv(int.Parse(nums[1]), int.Parse(nums[2]), line, ot[i]);
                }


                file.Close();
            }
            catch (System.Exception ex)
            {

                Console.WriteLine(ex);
            }

        }
        
        public static string getString(string filePath)
        {
            string line = "";
            try
            {
                System.IO.StreamReader file = new System.IO.StreamReader(filePath);

                line = file.ReadLine();
                file.Close();
            }
            catch (System.Exception ex)
            {

                Console.WriteLine(ex);
            }

            //Console.WriteLine(line.Length);
            return line;
        }
        public static void printv(int aCost, int bCost, string input, int expected)
        {
            var timerStart = DateTime.Now;
            timerStart = DateTime.Now;
            int result = Solution.buildString(aCost, bCost, input);
            Console.WriteLine(string.Format("Cost A ={0} B={1}", aCost, bCost));

            Console.WriteLine(string.Format("Result = {0} Out = {1} Time={2}", result, expected, DateTime.Now - timerStart));
        }
    }
}