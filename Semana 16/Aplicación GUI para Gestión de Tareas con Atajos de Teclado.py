import tkinter as tk
from tkinter import messagebox

class DarkToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 Mis Tareas")
        self.root.geometry("420x520")
        self.root.configure(bg="#1e1e1e")  # Fondo gris oscuro

        self.tasks = []

        # --- Widgets ---
        self.entry = tk.Entry(root, font=("Helvetica", 14), bg="#333333", fg="#ffffff", insertbackground="white", relief="flat")
        self.entry.pack(pady=15, padx=20, fill=tk.X)
        self.entry.focus()

        self.button_frame = tk.Frame(root, bg="#1e1e1e")
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="➕ Añadir", bg="#555555", fg="white", activebackground="#777777", relief="flat", command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.complete_button = tk.Button(self.button_frame, text="✔️ Completada", bg="#555555", fg="white", activebackground="#777777", relief="flat", command=self.complete_task)
        self.complete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="🗑️ Eliminar", bg="#555555", fg="white", activebackground="#777777", relief="flat", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

        self.listbox = tk.Listbox(root, font=("Helvetica", 14), selectmode=tk.SINGLE,
                                  bg="#2b2b2b", fg="#dddddd", selectbackground="#444444", selectforeground="white", relief="flat")
        self.listbox.pack(pady=15, padx=20, fill=tk.BOTH, expand=True)

        # --- Binds ---
        self.entry.bind("<Return>", lambda event: self.add_task())
        self.listbox.bind("<Delete>", lambda event: self.delete_task())
        self.listbox.bind("<d>", lambda event: self.delete_task())
        self.listbox.bind("<c>", lambda event: self.complete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text:
            self.tasks.append({"text": task_text, "completed": False})
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("⚠️ Aviso", "La tarea no puede estar vacía.")

    def complete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_listbox()
        else:
            messagebox.showinfo("ℹ️ Info", "Selecciona una tarea para completar.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()
        else:
            messagebox.showinfo("ℹ️ Info", "Selecciona una tarea para eliminar.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            text = task["text"]
            if task["completed"]:
                text = f"✔️ {text}"
            else:
                text = f"☐ {text}"  # Reemplazamos el reloj de arena por la casilla sin marcar
            self.listbox.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    app = DarkToDoApp(root)
    root.mainloop()
