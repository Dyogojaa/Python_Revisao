import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import subprocess

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Configurações de estilo
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Segoe UI", 12), foreground="#444444", background="#e0e0e0", padding=8, width=20)
        self.style.map("TButton", background=[("active", "#c4c4c4")])

        # Botão de seleção de pasta
        self.select_folder_btn = ttk.Button(self, text="Selecionar pasta", command=self.select_folder)
        self.select_folder_btn.pack(pady=10)

        # Botão de iniciar
        self.start_btn = ttk.Button(self, text="Iniciar", command=self.start_execution)
        self.start_btn.pack(pady=10)

        # Botão de parar
        self.stop_btn = ttk.Button(self, text="Parar", state="disabled", command=self.stop_execution)
        self.stop_btn.pack(pady=10)

        # Barra de progresso
        self.progressbar = ttk.Progressbar(self, orient="horizontal", length=400, mode="indeterminate")

    def select_folder(self):
        # Abre o explorador de arquivos para seleção da pasta
        folder_path = filedialog.askdirectory()

        # Exibe o caminho da pasta selecionada
        messagebox.showinfo("Pasta selecionada", f"Pasta selecionada:\n{folder_path}")

    def start_execution(self):
        # Desabilita o botão de seleção e habilita o botão de parar
        self.select_folder_btn["state"] = "disabled"
        self.start_btn["state"] = "disabled"
        self.stop_btn["state"] = "normal"

        # Inicia a animação de progresso
        self.progressbar.pack(pady=10)
        self.progressbar.start()

        # Executa os executáveis
        self.current_process = subprocess.Popen(["programa1.exe"])
        self.current_process = subprocess.Popen(["programa2.exe"])
        self.current_process = subprocess.Popen(["programa3.exe"])

        # Espera os processos terminarem
        while True:
            # Verifica se o botão de parar foi pressionado
            if self.current_process.poll() is not None:
                break

        # Para a animação de progresso
        self.progressbar.stop()
        self.progressbar.pack_forget()

        # Desabilita o botão de parar e habilita os botões de seleção e início
        self.stop_btn["state"] = "disabled"
        self.select_folder_btn["state"] = "normal"
        self.start_btn["state"] = "normal"

    def stop_execution(self):
        # Mata o processo atual
        self.current_process.kill()

        # Para a animação de progresso
        self.progressbar.stop()
        self.progressbar.pack_forget()

        # Desabilita o botão de parar e habilita os botões de seleção e início
        self.stop_btn["state"] = "disabled"
        self.select_folder_btn["state"] = "normal"
        self.start_btn["state"] = "normal"


# Cria a janela principal
root = tk.Tk()
app = Application(master=root)
app.mainloop()
