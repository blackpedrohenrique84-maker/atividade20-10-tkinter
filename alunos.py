import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# classe de Aluno
class Aluno:
    def __init__(self, nome, idade, serie):
        self._nome = nome
        self._idade = idade
        self.serie = serie

    @property
    def idade(self):
        return self._nome

    @idade.setter
    def idade(self, valor):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("A idade está errada")
        self._quantidade = valor
        
# criar página
janela = tk.Tk()
janela.title('Alunos')
janela.geometry("600x300")

# título
rotulo = tk.Label(
    janela,
    text="Cadastro de alunos",
    font=("Arial", 18)
)

rotulo.pack()


# 1- entrada do nome do aluno
rotulo = tk.Label(
    janela,
    text="nome do aluno:",
    font=("Arial", 12)
)

rotulo.pack()

# Entrada dos dados do 1
campo_nome = tk.Entry(janela)
campo_nome.pack()

# 2- entrada da idade
rotulo = tk.Label(
    janela,
    text="Idade do aluno:",
    font=("Arial", 12)
)

rotulo.pack()

# Entrada dos dados do 2
campo_idade = tk.Entry(janela)
campo_idade.pack()

# 3- entrada da série
rotulo = tk.Label(
    janela,
    text="série:",
    font=("Arial", 12)
)

rotulo.pack()

# Entrada dos dados do 3
campo_serie = tk.Entry(janela)
campo_serie.pack()


# dados do Aluno
dados_do_aluno = []

# cadastro função
def cadastrar():
    dados_do_aluno = [campo_nome.get(), campo_idade.get(), campo_serie.get()]

# mensagem q mostra o sucesso
def sucesso():
    messagebox.showinfo("sucesso!!", "o nome já está registrado!")

botao = tk.Button(
    janela,
    text='Cadastrar',
    command=cadastrar
    )

# treeview
tabela = ttk.Treeview(
    janela,
    columns=('aluno', 'idade', 'serie'),
    show="headings"
)

tabela.heading("aluno", text="Aluno:")
tabela.heading("idade", text="Idade")
tabela.heading("serie", text="Série")

tabela.insert("", tk.END, values=(dados_do_aluno[0], dados_do_aluno[1], dados_do_aluno[2]))

janela.mainloop()
