using System;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        string[] input = Console.ReadLine().Split();
        int n = int.Parse(input[0]);
        int m = int.Parse(input[1]);

        int[] b = new int[n + 1];

        for (int i = 0; i < m; i++)
        {
            input = Console.ReadLine().Split();
            int u = int.Parse(input[0]);
            int v = int.Parse(input[1]);
            b[u] |= 1 << v;
            b[v] |= 1 << u;
        }

        bool t = false;
        for (int i = 1; i <= n; i++)
        {
            for (int j = i + 1; j <= n; j++)
            {
                if (Convert.ToString(b[i] & b[j], 2).Count(c => c == '1') > 2)
                {
                    t = true;
                    break;
                }
            }
        }

        Console.WriteLine(t ? "YES" : "NO");
    }
}
