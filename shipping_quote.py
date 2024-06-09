using System;

namespace PackageExpress
{
    class Program
    {
        static void Main(string[] args)
        {
            // Display the welcome message
            Console.WriteLine("Welcome to Package Express. Please follow the instructions below.");

            // Prompt the user for the package weight and convert it to a double
            Console.Write("Please enter the package weight: ");
            double weight = Convert.ToDouble(Console.ReadLine());

            // Check if the weight is greater than 50
            if (weight > 50)
            {
                // Display an error message and end the program if the package is too heavy
                Console.WriteLine("Package too heavy to be shipped via Package Express. Have a good day.");
            }
            else
            {
                // Prompt the user for the package width and convert it to a double
                Console.Write("Please enter the package width: ");
                double width = Convert.ToDouble(Console.ReadLine());

                // Prompt the user for the package height and convert it to a double
                Console.Write("Please enter the package height: ");
                double height = Convert.ToDouble(Console.ReadLine());

                // Prompt the user for the package length and convert it to a double
                Console.Write("Please enter the package length: ");
                double length = Convert.ToDouble(Console.ReadLine());

                // Check if the sum of the dimensions is greater than 50
                if ((width + height + length) > 50)
                {
                    // Display an error message and end the program if the package is too big
                    Console.WriteLine("Package too big to be shipped via Package Express.");
                }
                else
                {
                    // Calculate the quote using the provided formula
                    double quote = (width * height * length * weight) / 100;

                    // Display the calculated quote to the user formatted to two decimal places
                    Console.WriteLine($"Your estimated total for shipping this package is: ${quote:F2}");
                    Console.WriteLine("Thank you!");
                }
            }
        }
    }
}
