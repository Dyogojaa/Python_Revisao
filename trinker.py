import tkinter as tk
from tkinter import messagebox

class CrudApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CRUD App")
        self.root.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        # Label e Entry para o nome
        tk.Label(self.root, text="Nome:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)

        # Label e Entry para a idade
        tk.Label(self.root, text="Idade:").grid(row=1, column=0)
        self.age_entry = tk.Entry(self.root)
        self.age_entry.grid(row=1, column=1)

        # Botão para adicionar um novo item
        add_button = tk.Button(self.root, text="Adicionar", command=self.add_item)
        add_button.grid(row=2, column=0)

        # Botão para atualizar um item existente
        update_button = tk.Button(self.root, text="Atualizar", command=self.update_item)
        update_button.grid(row=2, column=1)

        # Botão para remover um item existente
        remove_button = tk.Button(self.root, text="Remover", command=self.remove_item)
        remove_button.grid(row=2, column=2)

        # Lista para exibir os itens
        self.item_list = tk.Listbox(self.root, width=40)
        self.item_list.grid(row=3, column=0, columnspan=3)

        self.load_items()

    def add_item(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        if name and age:
            item = f"{name} - {age}"
            self.item_list.insert(tk.END, item)
            self.name_entry.delete(0, tk.END)
            self.age_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    def update_item(self):
        selected_item = self.item_list.curselection()
        if selected_item:
            name = self.name_entry.get()
            age = self.age_entry.get()
            if name and age:
                item = f"{name} - {age}"
                self.item_list.delete(selected_item)
                self.item_list.insert(selected_item, item)
                self.name_entry.delete(0, tk.END)
                self.age_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        else:
            messagebox.showerror("Erro", "Por favor, selecione um item para atualizar.")

    def remove_item(self):
        selected_item = self.item_list.curselection()
        if selected_item:
            self.item_list.delete(selected_item)
            self.name_entry.delete(0, tk.END)
            self.age_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Por favor, selecione um item para remover.")

    def load_items(self):
        self.item_list.delete(0, tk.END)
        items = ["João - 25", "Maria - 30", "Pedro - 40"]
        for item in items:
            self.item_list.insert(tk.END, item)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = CrudApp()
    app.run()
