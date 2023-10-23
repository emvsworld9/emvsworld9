import tkinter as tk
from tkinter import messagebox
#########################################
class LibraryManagmentSystem():
    def __init__(self,root):
        self.root = root
        self.root.title("library managment system")
        self.books = []
        ###########################################
        #UI design
        self.title_label = tk.Label(root,text = "Book Title",font=15)
        self.title_label.grid(row = 0,column = 0)
        self.title_entery = tk.Entry(root)
        self.title_entery.grid(row=0,column=1)

        self.author_label = tk.Label(root,text = "Author Name",font=15)
        self.author_label.grid(row = 1,column = 0)
        self.author_entery = tk.Entry(root)
        self.author_entery.grid(row=1,column=1)

        self.add_button = tk.Button(root,text="Add book",command=self.add_book)
        self.add_button.grid(row=2,column=0,columnspan=2)

        self.add_button = tk.Button(root,text="Display book",command=self.display_book)
        self.add_button.grid(row=3,column=0,columnspan=2)

        self.add_button = tk.Button(root,text="Borrow book",command=self.borrow_book)
        self.add_button.grid(row=4,column=0,columnspan=2)

        self.add_button = tk.Button(root,text="Return book",command=self.return_book)
        self.add_button.grid(row=5,column=0,columnspan=2)

        self.output_label = tk.Label(root,text = "",font=10)
        self.output_label.grid(row=6,column=0,columnspan=2)
    #########################################################################################
        

    def add_book(self):
        title = self.title_entery.get()
        author = self.author_entery.get()

        if title and author:
            found = False
            for book in self.books:
                if book["title"] == title and book["author"] == author:
                    book["count"] += 1
                    found = True
                    break

            if not found:
                self.books.append({"title": title, "author": author, "count": 1, "available": True})

            self.title_entery.delete(0, "end")
            self.author_entery.delete(0, "end")
            self.output_label.config(text=f"{title} by {author} has been added to the library")

        else:
            messagebox.showwarning("Warning", "Please enter both title and author")
    def display_book(self):
        books_list = ""
        for book in self.books:
            availability = "available" if book["count"] > 0 else "Not available"
            books_list += f"{book['title']} by {book['author']} - Count: {book['count']} - {availability}\n"
        self.output_label.config(text=books_list)

    def borrow_book(self):
        title = self.title_entery.get()
        author = self.author_entery.get()
        for book in self.books:
            if book["title"] == title and book["author"] == author and book["count"] > 0:
                book["count"] -= 1
                self.title_entery.delete(0, "end")
                self.author_entery.delete(0, "end")
                self.output_label.config(text=f"You have borrowed {title} by {author}. Enjoy your reading")
                return

        self.output_label.config(text=f"Sorry, {title} by {author} is either unavailable or doesn't exist")

    def return_book(self):
        title = self.title_entery.get()
        author = self.author_entery.get()
        for book in self.books:
            if book["title"] == title and book["author"] == author:
                book["count"] += 1
                self.output_label.config(text=f"Thank you for returning {title}.")
                self.title_entery.delete(0, "end")
                self.author_entery.delete(0, "end")
                return

        self.output_label.config(text=f"{title} was not found in the library.")

root = tk.Tk()
lms = LibraryManagmentSystem(root)
root.mainloop()

