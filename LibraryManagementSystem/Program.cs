using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LibraryManagementSystem
{
    internal class Program 
    {
        static Library library = new Library();
        static int bookID = 1;

        static void Main(string[] args)
        {
            while (true)
            {
                ShowMenu();
                string input = Console.ReadLine();

                switch (input)
                {
                    case "1": AddBook(); break;
                    case "2": library.ListBooks(); break;
                    case "3": SearchBook(); break;
                    case "4": FilterByGenre(); break;
                    case "5": RemoveBook(); break;
                    case "0": return;
                    default: Console.WriteLine("Invalid option."); break;
                }
            }
        }

        static void ShowMenu()
        {
            Console.WriteLine();
            Console.WriteLine("------ Library System ------");
            Console.WriteLine("1. Add new book");
            Console.WriteLine("2. List all books");
            Console.WriteLine("3. Search by title");
            Console.WriteLine("4. Filter by genre");
            Console.WriteLine("5. Remove book by ID");
            Console.WriteLine("0. Exit");
            Console.Write("Choose an option: ");
        }

        static void AddBook()
        {
            Console.WriteLine();
            Console.Write("Title: ");
            string title = Console.ReadLine();
            Console.Write("Author: ");
            string author = Console.ReadLine();
            Console.Write("Genre: ");
            string genre = Console.ReadLine();
            Book addedBook = new Book(bookID++, title, author, genre);
            library.AddBook(addedBook);
            Console.WriteLine("Book added.");
        }

        static void SearchBook()
        {
            Console.WriteLine();
            Console.Write("Enter keyword in title: ");
            string keyword = Console.ReadLine();
            library.SearchByTitle(keyword);
        }

        static void FilterByGenre()
        {
            Console.WriteLine();
            Console.Write("Enter genre to filter: ");
            string genre = Console.ReadLine();
            library.FilterByGenre(genre);
        }

        static void RemoveBook()
        {
            Console.WriteLine();
            Console.Write("Enter book ID to remove: ");
            int id = int.Parse(Console.ReadLine());
            library.RemoveBookById(id);
        }
    }
    
}
