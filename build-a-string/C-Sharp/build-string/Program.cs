using System;
using System.Collections.Generic;
using System.IO;

namespace build_string
{
    #region Comment
    // public class Solution1
    // {
    //     static string s = "";
    //     static int STRING_MAX_LENGTH = 0;
    //     static int minCost = 99999999;
    //     static int a_dollar = 0;
    //     static int b_dollar = 0;
    //     static int MAX_VALUE_CONST = 99999999;
    //     static int REDUCE_LENGTH = 0;
    //     static string MAX_SUBSTRING = "";
    //     static bool do_not_process = false;

    //     static Dictionary<string, int> memDict = new Dictionary<string, int>();
    //     public static Dictionary<int, string> subStringDict = new Dictionary<int, string>();

    //     static void int_dictionary()
    //     {
    //         int start = 0;//STRING_MAX_LENGTH - REDUCE_LENGTH;
    //         int end = STRING_MAX_LENGTH - 2;
    //         for (int i = start; i < end; i++)
    //         {
    //             string sb = s.Substring(0, i + 1);

    //             string tempStr = "";
    //             for (int j = i + 1; j < STRING_MAX_LENGTH; j++)
    //             {
    //                 string lstr = tempStr + s[j].ToString();
    //                 if (sb.IndexOf(lstr) > -1)
    //                 {
    //                     tempStr = lstr;
    //                     continue;
    //                 }
    //                 else
    //                 {
    //                     break;
    //                 }
    //             }
    //             if (tempStr.Length > 1)
    //             {
    //                 subStringDict[i] = tempStr;
    //             }
    //         }
    //     }
    //     static void findMaxSubString()
    //     {
    //         string maxSubString = "";
    //         for (int i = 0; i < STRING_MAX_LENGTH; i++)
    //         {
    //             string sb = s.Substring(0, i + 1);
    //             if ((i + 1 + maxSubString.Length) < STRING_MAX_LENGTH)
    //             {
    //                 string tempStr = s.Substring(i + 1, maxSubString.Length + 1);

    //                 if (sb.IndexOf(tempStr) > -1)
    //                 {
    //                     for (int k = i + maxSubString.Length + 2; k < STRING_MAX_LENGTH; k++)
    //                     {
    //                         string localStr = tempStr + s[k].ToString();
    //                         if (sb.IndexOf(localStr) > -1)
    //                         {
    //                             tempStr = localStr;
    //                         }
    //                         else
    //                             break;
    //                     }
    //                     if (tempStr.Length > maxSubString.Length)
    //                     {
    //                         maxSubString = tempStr;
    //                         //Console.WriteLine(i + "=max=" + maxSubString);
    //                     }
    //                 }
    //             }

    //         }
    //         MAX_SUBSTRING = maxSubString;
    //         Console.WriteLine("max=" + maxSubString);

    //     }

    //     public static int min_cost(List<string> path)
    //     {
    //         int cost = 0;
    //         foreach (string substring in path)
    //         {
    //             if (substring.Length == 1)
    //             {
    //                 cost += a_dollar;
    //             }
    //             else
    //             {
    //                 cost += b_dollar;
    //             }
    //             Console.Write(substring + ",");
    //         }
    //         Console.WriteLine();
    //         return cost;
    //     }
    //     public static int buildString(int a, int b, string s1)
    //     {
    //         /*
    //          * Write your code here.
    //          */
    //         memDict = new Dictionary<string, int>();
    //         minCost = MAX_VALUE_CONST;
    //         s = s1.Replace("\n", "");
    //         STRING_MAX_LENGTH = s.Length;
    //         a_dollar = a;
    //         b_dollar = b;
    //         REDUCE_LENGTH = STRING_MAX_LENGTH;
    //         subStringDict = new Dictionary<int, string>();
    //         do_not_process = false;
    //         MAX_SUBSTRING = "";
    //         //int_dictionary();
    //         //findMaxSubString();
    //         List<string> path = new List<string>();
    //         minCost = find_cost("", "path", 0, 1, "");
    //         return minCost;//find_cost("", path, 0, 1, ""); //minCost;
    //     }
    //     static int Counter = 0;
    //     static int find_cost(string sb, string path, int lcost, int l, string node)
    //     {
    //         int total_cost = 0;
    //         //Console.WriteLine(Counter++);
    //         if (do_not_process)
    //         {
    //             return lcost;
    //         }
    //         if (memDict.ContainsKey(sb))
    //         {
    //             return memDict[sb];
    //         }
    //         if (lcost > 0 && lcost >= minCost)
    //         {
    //             return lcost;
    //         }


    //         if (sb == s)
    //         {
    //             //int cost = min_cost(path);


    //             if (lcost < minCost && !do_not_process)
    //             {

    //                 minCost = lcost;

    //                 if (a_dollar == b_dollar)
    //                 {
    //                     do_not_process = true;
    //                 }

    //             }
    //             return 0;
    //         }
    //         //Concat
    //         int substringLength = sb.Length;
    //         char nextch = s[substringLength];
    //         string nextchar = nextch.ToString();

    //         string concatStr = "";
    //         int start = STRING_MAX_LENGTH - REDUCE_LENGTH;

    //         for (int i = substringLength; i < STRING_MAX_LENGTH; i++)
    //         {
    //             string temp_str = concatStr + s[i];
    //             if (sb.IndexOf(temp_str) > -1)
    //             {
    //                 concatStr = temp_str;
    //                 continue;
    //             }
    //             else
    //             {
    //                 break;
    //             }
    //         }


    //         int concat_cost = MAX_VALUE_CONST;
    //         int add_cost = 0;
    //         List<string> _path;
    //         if (concatStr.Length > 1 && concatStr.Length >= (b_dollar - a_dollar))
    //         {
    //             if (concatStr.Length > 1)
    //             {
    //                 //path.Add(concatStr);
    //                 //_path = new List<string>(path); //path + (concatStr,)
    //                 concat_cost = find_cost(sb + concatStr, "_path", lcost + b_dollar, l + 1, concatStr);
    //                 concat_cost = b_dollar + concat_cost;
    //             }
    //             //path.Add(nextchar);
    //             //_path = new List<string>(path); //#path + (nextchar,)
    //             add_cost = find_cost(sb + nextchar, "_path", lcost + a_dollar, l + 1, nextchar);
    //             add_cost = a_dollar + add_cost;

    //         }
    //         else
    //         {
    //             //path.Add(nextchar);
    //             //_path = new List<string>(path); //#path + (nextchar,)
    //             add_cost = find_cost(sb + nextchar, "_path", lcost + a_dollar, l + 1, nextchar);
    //             add_cost = a_dollar + add_cost;

    //             if (concatStr.Length > 1)
    //             {
    //                 //path.Add(concatStr);
    //                 //_path = new List<string>(path); //#path + (nextchar,)
    //                 concat_cost = find_cost(sb + concatStr, "_path", lcost + b_dollar, l + 1, concatStr);
    //                 concat_cost = b_dollar + concat_cost;
    //                 if(concatStr == MAX_SUBSTRING){
    //                     do_not_process = true;
    //                 }
    //             }
    //         }
    //         if (concat_cost == MAX_VALUE_CONST)
    //             total_cost = add_cost;
    //         else if (concatStr.Length > 1 && b_dollar == a_dollar)
    //             total_cost = concat_cost;
    //         else
    //         {
    //             if (add_cost > concat_cost)
    //                 total_cost = concat_cost;
    //             else
    //                 total_cost = add_cost;
    //         }

    //         memDict[sb] = total_cost;
    //         return total_cost;
    //     }
    // }
    #endregion
    class Program
    {

        static void Main(string[] args)
        {
            Console.WriteLine(sizeof(double));
            //Console.WriteLine(factorial(13000, 0));
            //Console.WriteLine(factorialTR(13000, 0, 0));
            TestCase.tes_case0();
            TestCase.test_case1();
            TestCase.test_case5();

            TestCase.test_case20();
            TestCase.test_case11();
            foreach (var item in Solution.subStringDict)
            {
                //Console.WriteLine(item.Key.ToString().PadLeft(4) + "=" + Solution.subStringDict[item.Key]);
            }


            Console.Read();

        }
        static int buildString(int a, int b, string s)
        {
            return Solution.buildString(a, b, s);

        }

        

        
    }
}


