using System;

namespace PackageExpress
{
    class Program
    {
        static void Main(string[] args)
        {
            // Display welcome message
            Console.WriteLine("Welcome to Package Express. Please follow the instructions below.");

            // Prompt user for package weight
            Console.Write("Please enter the package weight: ");
            double weight = Convert.ToDouble(Console.ReadLine());

            // Check if weight is greater than 50
            if (weight > 50)
            {
                Console.WriteLine("Package too heavy to be shipped via Package Express. Have a good day.");
                return; // End the program
            }

            // Prompt user for package dimensions
            Console.Write("Please enter the package width: ");
            double width = Convert.ToDouble(Console.ReadLine());

            Console.Write("Please enter the package height: ");
            double height = Convert.ToDouble(Console.ReadLine());

            Console.Write("Please enter the package length: ");
            double length = Convert.ToDouble(Console.ReadLine());

            // Check if dimensions total is greater than 50
            double dimensionTotal = width + height + length;
            if (dimensionTotal > 50)
            {
                Console.WriteLine("Package too big to be shipped via Package Express.");
                return; // End the program
            }

            // Calculate the quote
            double quote = (width * height * length * weight) / 100.0;

            // Display the quote
            Console.WriteLine($"Your estimated total for shipping this package is: ${quote:F2}");
            Console.WriteLine("Thank you!");
        }
    }
}
