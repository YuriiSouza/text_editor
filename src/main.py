import tkinter as tk
from file import File

# Criando a janela principal
root = tk.Tk()
root.geometry("1280x720")
root.title("Code Editor")

# Criando a área de texto
text_place_1 = tk.Text(root)
text_place_1.pack(expand=True, fill="both")

file_1 = File()

# Criando a barra de menu
menu_bar = tk.Menu(root)

arquivo_menu = tk.Menu(menu_bar, tearoff=0)
arquivo_menu.add_command(label="Abrir", command=lambda: file_1.search_file(text_place_1))
arquivo_menu.add_command(label="Salvar", command=lambda: file_1.save_file(text_place_1))
arquivo_menu.add_command(label="Salvar Como", command=lambda: file_1.save_as_file(text_place_1))
arquivo_menu.add_separator()
arquivo_menu.add_command(label="Sair", command=root.quit)

menu_bar.add_cascade(label="Arquivo", menu=arquivo_menu)
root.config(menu=menu_bar)

root.mainloop()
