import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

def inicializar_banco():
    conexao = sqlite3.connect("meu_banco.db")
    cursor = conexao.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tarefas(
            id_tarefa INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            descricao TEXT
        )
    """
    )
    conexao.commit()
    conexao.close()

def conectar_banco():
    return sqlite3.connect("meu_banco.db")

def obter_tarefas():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tarefas")
    registros = cursor.fetchall()
    conexao.close()
    return registros

def adicionar_tarefas(nome, descricao):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO tarefas (nome, descricao) VALUES (?, ?)", (nome, descricao)
    )
    conexao.commit()
    conexao.close()

def remover_tarefa(id_tarefa):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id_tarefa = ?", (id_tarefa,))
    linhas_afetadas = cursor.rowcount
    conexao.commit()
    conexao.close()
    return linhas_afetadas > 0

class ScheduleManagerApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Todoo! Aplication")
        self.root.geometry("950x550")
        self.root.minsize(1050, 550)
        self.root.resizable(False, False)

        fonte_negrito = ("Segoe UI", 10, "bold")

        frame_entradas = tk.Frame(self.root, padx=10, pady=10)
        frame_entradas.pack(fill=tk.X)

        tk.Label(frame_entradas, text="Nome da Tarefa (máx 20):", font=fonte_negrito).grid(row=0, column=0, sticky="w")
        self.entry_nome = tk.Entry(frame_entradas, width=30)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_entradas, text="Descrição (Máx 50):",font=fonte_negrito).grid(row=1, column=0, sticky="w")
        self.entry_descricao = tk.Entry(frame_entradas, width=45)
        self.entry_descricao.grid(row=1, column=1, padx=5, pady=5)

        frame_tabela = tk.Frame(self.root, padx=10, pady=5)
        frame_tabela.pack(fill=tk.BOTH, expand=True)

        colunas = ("id", "nome", "data", "descricao")
        self.tabela = ttk.Treeview(frame_tabela, columns=colunas, show="headings")

        self.tabela.heading("id", text="ID")
        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("data", text="Data")
        self.tabela.heading("descricao", text="Descrição")

        self.tabela.column("id", width=50, anchor="center")
        self.tabela.column("nome", width=50)
        self.tabela.column("data", width=50)
        self.tabela.column("descricao", width=250)

        self.tabela.pack(fill=tk.BOTH, expand=True)
        frame_acoes = tk.Frame(self.root, padx=10, pady=10)
        frame_acoes.pack(fill=tk.X)

        botao_adicionar = tk.Button(frame_entradas, text="Adicionar Tarefa",font=fonte_negrito, command=self.botao_adicionar_clicado, bg="#6fe3eb") # ciano claro
        botao_adicionar.grid(row=0, column=2, rowspan=2, padx=250, ipady=10, stick="w")

        botao_remover = tk.Button(frame_acoes, text="Remover Tarefa Selecionada",font=fonte_negrito, command=self.botao_remover_clicado, bg="#ff9696") #coral claro
        botao_remover.pack(side=tk.LEFT)

        botao_atualizar = tk.Button(frame_acoes, text="Atualizar Lista",font=fonte_negrito, command=self.atualizar_tabela, bg="#ba95ff") #violeta claro
        botao_atualizar.pack(side=tk.RIGHT)

        self.atualizar_tabela()

    def botao_adicionar_clicado(self):
        nome = self.entry_nome.get().strip()
        descricao = self.entry_descricao.get().strip()

        if not nome or not descricao:
            messagebox.showwarning("Aviso", "Nome e Descrição não podem ficar vazios!")
        elif len(descricao) > 50 and len(nome) > 20:
            messagebox.showwarning("Aviso", "Ambos nome e descrição ultrapassam o limite de caractreres!")
        elif len(nome) > 20:
            messagebox.showwarning("Aviso", "O nome precisa ter no máximo 20 caracteres!")
        elif len(descricao) > 50:
            messagebox.showwarning("Aviso", "A descrição não deve passar de 50 caracteres!")
        else:
            adicionar_tarefas(nome, descricao)
            messagebox.showinfo("Sucesso", f"'{nome}' adicionado com sucesso!")
            self.entry_nome.delete(0, tk.END)
            self.entry_descricao.delete(0, tk.END)
            self.atualizar_tabela()

    def botao_remover_clicado(self):
        item_selecionado = self.tabela.selection()
        if not item_selecionado:
            messagebox.showwarning("Aviso", "Selecione uma tarefa na tabela para remover.")
            return

        id_tarefa = self.tabela.item(item_selecionado[0])["values"][0]

        if remover_tarefa(id_tarefa):
            messagebox.showinfo("Sucesso",f"Tarefa '{id_tarefa}' removida com sucesso!",)
            self.atualizar_tabela()
        else:
            messagebox.showerror("Erro", "Id não localizado, tarefa inexistente!")

    def atualizar_tabela(self):
        for item in self.tabela.get_children():
            self.tabela.delete(item)
        registros = obter_tarefas()
        for i in registros:
            self.tabela.insert("", tk.END, values=i)


if __name__ == "__main__":
    inicializar_banco()
    root = tk.Tk()
    app = ScheduleManagerApp(root)
    root.mainloop()