using System;
using System.Collections.Generic;
using System.IO;

namespace build_string
{
    public class Solution
    {
        static string s = "";
        static int STRING_MAX_LENGTH = 0;
        static int minCost = 99999999;
        static int a_dollar = 0;
        static int b_dollar = 0;
        static int MAX_VALUE_CONST = 99999999;
        static int REDUCE_LENGTH = 0;
        static string MAX_SUBSTRING = "";
        static bool do_not_process = false;

        static Dictionary<string, int> memDict = new Dictionary<string, int>();
        public static Dictionary<int, string> subStringDict = new Dictionary<int, string>();


        public static int buildString(int a, int b, string s1)
        {
            /*
             * Write your code here.
             */
            memDict = new Dictionary<string, int>();
            minCost = MAX_VALUE_CONST;
            s = s1.Replace("\n", "");
            STRING_MAX_LENGTH = s.Length;
            a_dollar = a;
            b_dollar = b;
            REDUCE_LENGTH = STRING_MAX_LENGTH;
            subStringDict = new Dictionary<int, string>();
            do_not_process = false;
            MAX_SUBSTRING = "";
            //int_dictionary();
            //findMaxSubString();
            minCost = find_cost("", "", 0, 1, "");
            return minCost;//find_cost("", path, 0, 1, ""); //minCost;
        }
        static int Counter = 0;
        static int find_cost(string sb, string path, int lcost, int l, string node)
        {
            int total_cost = 0;
            if (do_not_process)
            {
                return lcost;
            }
            if (memDict.ContainsKey(sb))
            {
                return memDict[sb];
            }
            if (lcost > 0 && lcost >= minCost)
            {
                return lcost;
            }


            if (sb == s)
            {
                //int cost = min_cost(path);
                ///Console.WriteLine(path);

                if (lcost < minCost && !do_not_process)
                {

                    minCost = lcost;

                    if (a_dollar == b_dollar)
                    {
                        do_not_process = true;
                    }

                }
                return 0;
            }
            //Console.WriteLine((Counter++).ToString().PadLeft(4) +" " + sb.PadLeft(100) +" " +node);

            //Concat
            int substringLength = sb.Length;
            char nextch = s[substringLength];
            string nextchar = nextch.ToString();

            string concatStr = "";

            for (int i = substringLength; i < STRING_MAX_LENGTH; i++)
            {
                string temp_str = concatStr + s[i];
                if (sb.Contains(temp_str))
                {
                    concatStr = temp_str;
                    continue;
                }
                else
                {
                    break;
                }
            }


            int concat_cost = MAX_VALUE_CONST;
            int add_cost = 0;
            if (concatStr.Length > 1 && concatStr.Length >= (b_dollar - a_dollar))
            {
                if (concatStr.Length > 1)
                {
                    concat_cost = find_cost(sb + concatStr, path + "-" + concatStr, lcost + b_dollar, l + 1, concatStr);
                    concat_cost = b_dollar + concat_cost;
                }
                add_cost = find_cost(sb + nextchar, path + "-" + nextchar, lcost + a_dollar, l + 1, nextchar);
                add_cost = a_dollar + add_cost;

            }
            else
            {
                add_cost = find_cost(sb + nextchar, path + "-" + nextchar, lcost + a_dollar, l + 1, nextchar);
                add_cost = a_dollar + add_cost;

                if (concatStr.Length > 1)
                {
                    concat_cost = find_cost(sb + concatStr, path + "-" + concatStr, lcost + b_dollar, l + 1, concatStr);
                    concat_cost = b_dollar + concat_cost;
                    if (concatStr == MAX_SUBSTRING)
                    {
                        do_not_process = true;
                    }
                }
            }
            if (concat_cost == MAX_VALUE_CONST)
                total_cost = add_cost;
            else if (concatStr.Length > 1 && b_dollar == a_dollar)
                total_cost = concat_cost;
            else
            {
                if (add_cost > concat_cost)
                    total_cost = concat_cost;
                else
                    total_cost = add_cost;
            }

            memDict[sb] = total_cost;
            return total_cost;
        }
        
        #region exTra
        static void int_dictionary()
        {
            int start = 0;//STRING_MAX_LENGTH - REDUCE_LENGTH;
            int end = STRING_MAX_LENGTH - 2;
            for (int i = start; i < end; i++)
            {
                string sb = s.Substring(0, i + 1);

                string tempStr = "";
                for (int j = i + 1; j < STRING_MAX_LENGTH; j++)
                {
                    string lstr = tempStr + s[j].ToString();
                    if (sb.IndexOf(lstr) > -1)
                    {
                        tempStr = lstr;
                        continue;
                    }
                    else
                    {
                        break;
                    }
                }
                if (tempStr.Length > 1)
                {
                    subStringDict[i] = tempStr;
                }
            }
        }
        static void findMaxSubString()
        {
            string maxSubString = "";
            for (int i = 0; i < STRING_MAX_LENGTH; i++)
            {
                string sb = s.Substring(0, i + 1);
                if ((i + 1 + maxSubString.Length) < STRING_MAX_LENGTH)
                {
                    string tempStr = s.Substring(i + 1, maxSubString.Length + 1);

                    if (sb.IndexOf(tempStr) > -1)
                    {
                        for (int k = i + maxSubString.Length + 2; k < STRING_MAX_LENGTH; k++)
                        {
                            string localStr = tempStr + s[k].ToString();
                            if (sb.IndexOf(localStr) > -1)
                            {
                                tempStr = localStr;
                            }
                            else
                                break;
                        }
                        if (tempStr.Length > maxSubString.Length)
                        {
                            maxSubString = tempStr;
                            //Console.WriteLine(i + "=max=" + maxSubString);
                        }
                    }
                }

            }
            MAX_SUBSTRING = maxSubString;
            Console.WriteLine("max=" + maxSubString);

        }

        public static int min_cost(List<string> path)
        {
            int cost = 0;
            foreach (string substring in path)
            {
                if (substring.Length == 1)
                {
                    cost += a_dollar;
                }
                else
                {
                    cost += b_dollar;
                }
                Console.Write(substring + ",");
            }
            Console.WriteLine();
            return cost;
        }
        #endregion
    }
}