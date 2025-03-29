import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No se puede agregar una tarea vacía.")

def mark_completed():
    try:
        selected_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_index)
        task_listbox.delete(selected_index)
        task_listbox.insert(selected_index, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x450")
root.configure(bg="#567e8f")

# Estilos
button_bg = "#4CAF50"
button_fg = "white"
button_font = ("Arial", 12, "bold")

title_label = tk.Label(root, text="Lista de Tareas", font=("Arial", 16, "bold"), bg="#567e8f")
title_label.pack(pady=10)

# Campo de entrada y botones
task_entry = tk.Entry(root, width=40, font=("Arial", 12))
task_entry.pack(pady=5)
task_entry.bind("<Return>", add_task)  # Permitir agregar con Enter

button_frame = tk.Frame(root, bg="#567e8f")
button_frame.pack(pady=5)

add_button = tk.Button(button_frame, text="Añadir", bg=button_bg, fg=button_fg, font=button_font, command=add_task)
add_button.grid(row=0, column=0, padx=5)

mark_button = tk.Button(button_frame, text="Completada", bg=button_bg, fg=button_fg, font=button_font, command=mark_completed)
mark_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Eliminar", bg="#FF5733", fg=button_fg, font=button_font, command=delete_task)
delete_button.grid(row=0, column=2, padx=5)

# Lista de tareas
task_listbox = tk.Listbox(root, width=50, height=15, font=("Arial", 12), selectbackground="#D3D3D3")
task_listbox.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()