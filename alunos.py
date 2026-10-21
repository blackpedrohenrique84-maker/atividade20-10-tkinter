import tkinter as tk
from tkinter import ttk

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

# dados do Aluno
dados_do_aluno = []

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

# cadastro
def cadastrar():
    for dados in range(3):
        dados_do_aluno  

# classe de Aluno
class Aluno:
    def __init__(self, nome, idade, serie):
        self._nome = nome
        self._idade = idade
        self.serie = serie

janela.mainloop()