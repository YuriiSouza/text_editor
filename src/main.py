import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def search_file():
  file = filedialog.askopenfilename(filetypes=[("Arquivos Python", "*.py"), ("Arquivos de Texto", "*.txt"), ("Todos os Arquivos", "*.*")])
  
  if file:
    with open(file, "r") as read_file:
      text_place.insert(tk.END, read_file.read())
  
  print(file)
  
#iniciando app
root = tk.Tk()
root.geometry("1280x720")
root.title("Code Editor")

#colocando area de texto
text_place = tk.Text(root, height=1920, width=1080)
text_place.grid(row=0, column=0)

#criando barra de menu
menu_bar = tk.Menu(root)

arquivo_menu = tk.Menu(menu_bar, tearoff=0)
arquivo_menu.add_command(label="Abrir", command=search_file)
arquivo_menu.add_command(label="Salvar")
arquivo_menu.add_separator()
arquivo_menu.add_command(label="Sair", command=root.quit)

menu_bar.add_cascade(label="Arquivo", menu=arquivo_menu)
root.config(menu=menu_bar)

  

root.mainloop()
        
    