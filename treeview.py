import tkinter as tk
from tkinter import ttk

# janela principal
janela = tk.Tk()
janela.title('Biblioteca')
janela.geometry("600x300")

# listbox
lista = tk.Listbox(janela)
lista.pack()

lista.insert(tk.END, 'Ana')
lista.insert(tk.END, 'Carlos')
lista.insert(tk.END, 'Maria')

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

livros = [Livro('1984'), Livro('O Hobbit')]

for livro in livros:
    lista.insert(tk.END, livro.titulo)

# treeview
tabela = ttk.Treeview(
    janela,
    columns=('titulo', 'autor'),
    show="headings"
)

tabela.heading("titulo", text="Título")
tabela.heading("autor", text="Autor")

tabela.insert("", tk.END, values=("Dom Casmurro", "Machado de Assis"))

tabela.pack()

janela.mainloop()