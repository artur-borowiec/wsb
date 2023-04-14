using System;

enum Choice
{
    Rock,
    Paper,
    Scissors
}

class Program
{
    static int totalScorePlayer = 0;
    static int totalScoreCPU = 0;
    
    static void Main(string[] args)
    {
        bool playAgain = true;

        while (playAgain)
        {
            // losowanie dla komputera
            Random random = new Random();
            Choice computerChoice = (Choice)random.Next(0, 3);

            // wybor gracza
            Console.Write("Kamien, papier czy nozyce? ");
            string input = Console.ReadLine().ToLower();
            Choice playerChoice;

            switch (input)
            {
                case "kamien":
                    playerChoice = Choice.Rock;
                    break;
                case "papier":
                    playerChoice = Choice.Paper;
                    break;
                case "nozyce":
                    playerChoice = Choice.Scissors;
                    break;
                default:
                    Console.WriteLine("Nieprawidlowy wybor.");
                    continue;
            }

            // sprawdzanie wygranego
            if (playerChoice == computerChoice)
            {
                Console.WriteLine("Remis! ");
                printScore();
            }
            else if ((playerChoice == Choice.Rock && computerChoice == Choice.Scissors) ||
                     (playerChoice == Choice.Paper && computerChoice == Choice.Rock) ||
                     (playerChoice == Choice.Scissors && computerChoice == Choice.Paper))
            {
                totalScorePlayer++;
                Console.WriteLine("Wygrales! ");
                printScore();
            }
            else
            {
                Console.WriteLine("Komputer wygrywa! ");
                totalScoreCPU++;
                printScore();
            }

            Console.Write("Jeszcze raz? (t/n) ");
            string playAgainInput = Console.ReadLine().ToLower();

            if (playAgainInput != "t")
            {
                playAgain = false;
            }
        }
    }
    
    static void printScore() {
        Console.WriteLine(" Wynik to: " + totalScorePlayer + ":" + totalScoreCPU + ". ");
    }
}
