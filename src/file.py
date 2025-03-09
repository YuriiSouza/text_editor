import os
import time
import tkinter as tk
from tkinter import filedialog

class File:
    def __init__(self, path=""):
        if not path:
            path = "../cache/undefined.txt"
            os.makedirs(os.path.dirname(path), exist_ok=True)
            if not os.path.exists(path):
                with open(path, "w", encoding="utf-8") as f:
                    f.write("")
        
        self.set_path(path)

    def get_path(self):
        return self.path

    def set_path(self, new_path):
        """Atualiza o caminho e as informações do arquivo"""
        self.path = new_path
        self.name = os.path.basename(new_path)
        self.size = os.path.getsize(new_path)
        info = os.stat(new_path)
        self.last_modified = time.ctime(info.st_mtime)
        self.last_accessed = time.ctime(info.st_atime)
        self.created = time.ctime(info.st_ctime)

    def search_file(self, text_place):
        """Abre um arquivo e insere o conteúdo na área de texto"""
        file_path = filedialog.askopenfilename(filetypes=[
            ("Python Files", "*.py"),
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ])

        if file_path:
            with open(file_path, "r", encoding="utf-8") as read_file:
                text_place.delete("1.0", tk.END)
                text_place.insert(tk.END, read_file.read())
            self.set_path(file_path)  # Atualiza o caminho do arquivo

    def save_file(self, text_place):
        """Salva o conteúdo da área de texto no arquivo atual"""
        path = self.get_path()
        
        if path:
            with open(path, "w", encoding="utf-8") as write_file:
                write_file.write(text_place.get("1.0", tk.END).strip())
        else:
            self.save_as_file(text_place)

    def save_as_file(self, text_place):
        """Abre um diálogo para salvar o arquivo"""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[
            ("Python Files", "*.py"),
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ])
        
        if file_path:
            self.set_path(file_path)
            self.save_file(text_place)

    def take_content(self):
      content = ""
      with open (self.path, "r", encoding="utf-8") as read_file:
        for i in read_file:
          content = content + i
        
      return content 
      
    def is_saved(self, text_area):
      content_saved = self.take_content()
      content = text_area
      
      hash1 = hash(content_saved)
      hash2 = hash(content)
      
      return hash1 == hash2
    
file = File("src/test.txt")

content = file.take_content()

print(content)