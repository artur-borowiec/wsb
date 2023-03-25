using System;
using System.Text.RegularExpressions;

namespace ConsoleApp1
{
    class Program
    {
        static string znaki = "Wikipedia – wielojęzyczna encyklopedia internetowa działająca zgodnie z zasadą otwartej treści. Funkcjonuje w oparciu " +
                "o oprogramowanie MediaWiki (haw. wiki – „szybko”, „prędko”), wywodzące się z koncepcji WikiWikiWeb, umożliwiające edycję każdemu " +
                "użytkownikowi odwiedzającemu stronę i aktualizację jej treści w czasie rzeczywistym. Słowo Wikipedia jest neologizmem powstałym " +
                "w wyniku połączenia wyrazów wiki i encyklopedia. Slogan Wikipedii brzmi: „Wolna encyklopedia, którą każdy może redagować”. Serwis był " +
                "notowany w rankingu Alexa na miejscu 13[1]. Wikipedia powstała 15 stycznia 2001 roku jako projekt pomocniczy pisanej przez ekspertów i " +
                "nieistniejącej już Nupedii. Od 2003 jej właścicielem jest organizacja non - profit Wikimedia Foundation. W pierwszych latach istnienia " +
                "Wikipedia zdobywała szybko rosnącą popularność, a Wikimedia Foundation uruchomiła różne projekty siostrzane.Wikipedia jest jedną z " +
                "najczęściej odwiedzanych stron internetowych, a wiele stron uruchomiło jej mirrory lub forki. ";

        static void autor(string name) {
            linia(name);
            Console.WriteLine();
        }

        static void k1_lancuch() {
            Console.WriteLine($"Wprowadzony tekst to: {znaki}");
            Console.WriteLine($"Długośc tekstu to: {znaki.Length}");
            Console.WriteLine($"Pierwszy znak to: {znaki[0]}");
            Console.WriteLine($"Ostatni znak to: {znaki[znaki.Length - 1]}");

            for (int i = 0; i < znaki.Length; i++)
                Console.Write(znaki[i]);
            for (int i = znaki.Length-1; i >= 0; i--)
                Console.Write(znaki[i]);

        }
        
        static void linia(string zm) {
            Console.WriteLine("Autor:" + zm);
            for (int i=0; i <= 70; i++)
                Console.WriteLine("=");
            Console.WriteLine();
        }

        // znaki parzyste jeden kolor, znaki nieparzyste drugi kolor
        static void kolory(string zm)
        {
            for (int i = 0; i < znaki.Length; i++)
            {
                ConsoleColor color;
                if (i % 2 == 0)
                    color = ConsoleColor.Red;
                else
                    color = ConsoleColor.Green;
                Console.ForegroundColor = color;
                Console.Write(znaki[i]);
            }
        }

        static void licz_zdania(string zm)
        {
            Console.WriteLine($"Liczba zdan: { zm.Split(". ").Length }");
        }
        
        static void licz_cyfry(string zm)
        {

        }

        // Liczba wielkich: Wielkie litery to:
        static void licz_wielkie(string zm)
        {

        }
        
        // Wylosuj 10 znakow
        static void wylosuj_znaki(string zm)
        {
            Random r = new Random();
            int i = r.Next(zm.Length);
            Console.WriteLine($"{zm[i]} ");
        }

        // 10 slow
        static void wylosuj_slowa(string zm)
        {
            Random r = new Random();
            int i = r.Next(zm.Length);
        }

        // zlicz kazdą literę
        static void licz_litery(string zm)
        {

        }


        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            autor("Artur Borowiec");

            //k1_lancuch();
            kolory(znaki);
        }
    }
}
