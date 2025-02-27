import os
import time
import tkinter as tk
from tkinter import filedialog

class File:
    def __init__(self, path=""):
        if path:
            self.set_path(path)
            info = os.stat(path)
            
            self.name, self.size = os.path.split(path)
            self.path = path
            self.last_modified = time.ctime(info.st_mtime)
            self.last_accessed = time.ctime(info.st_atime)
            self.created = time.ctime(info.st_ctime)
        
        else:
            self.path = ""
    
    def get_path(self):
        return self.path


    def set_path(self, new_path):
        self.path = new_path


    def search_file(self, text_place):
      """Abre um arquivo e insere o conteúdo na área de texto"""
      file_path = filedialog.askopenfilename(filetypes=[
          ("Arquivos Python", "*.py"),
          ("Arquivos de Texto", "*.txt"),
          ("Todos os Arquivos", "*.*")
      ])

      if file_path:
          with open(file_path, "r") as read_file:
              text_place.delete("1.0", tk.END) 
              text_place.insert(tk.END, read_file.read())
          
          self.set_path(file_path)  # Atualiza o caminho do arquivo


    def save_file(self, text_place):
        """Salva o conteúdo da área de texto no arquivo atual"""
        path = self.get_path()

        if path:
            with open(path, "w") as write_file:
                write_file.write(text_place.get("1.0", tk.END))
        else:
            self.save_as_file()  # Se não há caminho, pede para salvar como novo arquivo


    def save_as_file(self, text_place):
        """Abre um diálogo para salvar o arquivo"""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[
            ("Arquivos Python", "*.py"),
            ("Arquivos de Texto", "*.txt"),
            ("Todos os Arquivos", "*.*")
        ])
        
        if file_path:
            self.set_path(file_path)
            self.save_file(text_place)
