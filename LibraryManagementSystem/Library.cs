using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LibraryManagementSystem
{
    public class Library
    {
        private List<Book> books = new List<Book>();

        public void AddBook(Book b)
        {
            books.Add(b);
        }

        public void ListBooks()
        {
            Console.WriteLine();
            if (books.Count == 0)
            {
                Console.WriteLine("The library is empty.");
            }
            else
            {
                foreach (Book b in books)
                {
                    Console.WriteLine(b);
                }
            }
        }

        public void SearchByTitle(string keyword)
        {
            var result = books.Where(b => b.Title.ToLower().Contains(keyword.ToLower()));
            foreach (Book b in result)
            {
                Console.WriteLine(b);
            }
        }

        public void FilterByGenre(string genre)
        {
            var result = books.Where(b => b.Genre.ToLower() == genre.ToLower());
            foreach (Book b in result)
            {
                Console.WriteLine(b);
            }
        }

        public void RemoveBookById(int id)
        {
            var bookToRemove = books.FirstOrDefault(b => b.Id == id);
            if (bookToRemove != null)
            {
                books.Remove(bookToRemove);
                Console.WriteLine("Book removed.");
            }
            else
            {
                Console.WriteLine("Book not found.");
            }
        }
    }
}
