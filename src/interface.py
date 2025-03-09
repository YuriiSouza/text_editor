import tkinter as tk
from file import File

class Interface:
    def __init__(self, size):
        self.root = tk.Tk()
        self.size = size
        self.files = []
        
        self.file_1 = File()
        self.files.append(self.file_1)
        
        self.setup_window()
        self.setup_text_area()
        self.setup_menu()

    def setup_window(self):
        """Configura a janela principal"""
        self.root.geometry(self.size)
        self.update_title(self.file_1.name)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.quit()
        
    def setup_text_area(self):
        """Cria e configura a área de texto"""
        self.text_place = tk.Text(self.root)
        self.text_place.pack(expand=True, fill="both", padx=5, pady=5)

    def setup_menu(self):
        """Cria a barra de menu"""
        menu_bar = tk.Menu(self.root)

        arquivo_menu = tk.Menu(menu_bar, tearoff=0)
        arquivo_menu.add_command(label="Abrir", command=lambda: [self.file_1.search_file(self.text_place), self.update_title(self.file_1.name)])
        arquivo_menu.add_command(label="Salvar", command=lambda: [self.file_1.save_file(self.text_place), self.update_title(self.file_1.name)])
        arquivo_menu.add_command(label="Salvar Como", command=lambda: [self.file_1.save_as_file(self.text_place), self.update_title(self.file_1.name)])
        arquivo_menu.add_separator()
        arquivo_menu.add_command(label="Sair", command=lambda: self.quit())

        menu_bar.add_cascade(label="Arquivo", menu=arquivo_menu)
        self.root.config(menu=menu_bar)

    def quit(self):
      #se o texto estiver igual ao salvo, so fechar
      for file in self.files:
        text_area = self.text_place.get("1.0", tk.END).strip()
        saved = file.is_saved(text_area)
        
        if not saved:
          top = tk.Toplevel(self.root)
          top.title(f"Salvar {file.name}")
          
          label = tk.Label(top, text=f"Deseja salvar o arquivo {file.name} da pagina.")
          label.pack(padx=20, pady=10)
          
          confirm_button = tk.Button(top, text="Sim", command=lambda: self.save_and_close(top, file))
          confirm_button.pack(side="left", padx=10, pady=10)
          
          cancel_button = tk.Button(top, text="Não", command=top.destroy)
          cancel_button.pack(side="right", padx=10, pady=10)
          
        
        top = tk.Toplevel(self.root)
        top.title("Sair")
        
        label = tk.Label(top, text=f"Deseja sair?")
        label.pack(padx=20, pady=10)
        
        confirm_button = tk.Button(top, text="Sim", command=self.exit_application)
        confirm_button.pack(side="left", padx=10, pady=10)
        
        cancel_button = tk.Button(top, text="Não", command=top.destroy)
        cancel_button.pack(side="right", padx=10, pady=10)
        
          
    def save_and_close(self, top, file):
      """Salva o arquivo e fecha o pop-up"""
      file.save_file(self.text_place)
      top.destroy()  # Fecha a janela de confirmação
      self.root.quit()  # Fecha a janela principal
      
    def exit_application(self):
      self.root.quit()
      
    def update_title(self, file_name):
        """Atualiza o título da janela"""
        self.root.title(f"Code Editor - {file_name}")
      
    def run(self):
        """Executa a interface gráfica"""
        self.root.mainloop()
