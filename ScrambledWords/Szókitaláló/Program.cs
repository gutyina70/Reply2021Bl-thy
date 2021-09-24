using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Security.Cryptography;
using System.Text;

namespace Szókitaláló
{
  public class Program
  {
    static void Main()
    {
      List<string> dictionary = File.ReadAllLines("dictionary.txt").ToList();
      List<string> scrambleds = File.ReadAllLines("scrambled-words.txt").ToList();
      List<string> unscrambleds = new List<string>();
      foreach (string scrambled in scrambleds)
      {
        string unscrambled = Unscramble(scrambled, dictionary);
        Console.WriteLine($"{scrambled} -> {unscrambled}");
        unscrambleds.Add(unscrambled);
      }

      string unscrambledConcat = string.Join("", unscrambleds).ToLower();
      File.WriteAllText("unscrambled.txt", unscrambledConcat);
      string hash = Sha256(unscrambledConcat);
      Console.WriteLine($"Hash: {hash}");
      File.WriteAllText("flag.txt", $"{{FLG:{hash}}}");

      Console.ReadKey();
    }

    static string Sha256(string randomString)
    {
      var crypt = new SHA256Managed();
      string hash = String.Empty;
      byte[] crypto = crypt.ComputeHash(Encoding.ASCII.GetBytes(randomString));
      foreach (byte theByte in crypto)
      {
        hash += theByte.ToString("x2");
      }
      return hash;
    }

    static string Unscramble(string scrambled, List<string> dictionary)
    {
      var scrambledChars = GetCharsFromWord(scrambled);
      var result = dictionary
        .Where(x => x.Length == scrambled.Length)
        .Where(x => Enumerable.SequenceEqual(scrambledChars, GetCharsFromWord(x))).ToList();

      return result.FirstOrDefault();
    }

    static List<char> GetCharsFromWord(string word)
    {
      var result = word.ToCharArray().ToList();
      result.Sort();
      return result;
    }
  }
}
