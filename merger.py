import os
from pathlib import Path
from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Combinador de PDFs")
        self.root.geometry("600x400")
        self.root.configure(padx=20, pady=20)

        # Estilo
        style = ttk.Style()
        style.configure("TButton", padding=5)
        style.configure("TLabel", padding=5)

        # Variables
        self.input_dir = tk.StringVar()
        self.output_file = tk.StringVar()

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Sección de carpeta de entrada
        input_frame = ttk.LabelFrame(main_frame, text="Carpeta con PDFs", padding=10)
        input_frame.pack(fill=tk.X, pady=5)

        self.input_entry = ttk.Entry(input_frame, textvariable=self.input_dir)
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        ttk.Button(
            input_frame, text="Buscar Carpeta", command=self.select_input_dir
        ).pack(side=tk.RIGHT)

        # Sección de archivo de salida
        output_frame = ttk.LabelFrame(
            main_frame, text="Guardar PDF combinado como", padding=10
        )
        output_frame.pack(fill=tk.X, pady=5)

        self.output_entry = ttk.Entry(output_frame, textvariable=self.output_file)
        self.output_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        ttk.Button(
            output_frame, text="Guardar Como", command=self.select_output_file
        ).pack(side=tk.RIGHT)

        # Barra de progreso
        self.progress_var = tk.DoubleVar()
        self.progress = ttk.Progressbar(
            main_frame, variable=self.progress_var, maximum=100
        )
        self.progress.pack(fill=tk.X, pady=20)

        # Área de log
        log_frame = ttk.LabelFrame(main_frame, text="Estado", padding=10)
        log_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.log_text = tk.Text(log_frame, height=8, wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True)

        # Botón de combinar
        ttk.Button(main_frame, text="Combinar PDFs", command=self.merge_pdfs).pack(
            pady=10
        )

    def select_input_dir(self):
        directory = filedialog.askdirectory()
        if directory:
            self.input_dir.set(directory)

    def select_output_file(self):
        file = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
        )
        if file:
            self.output_file.set(file)

    def log(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update()

    def merge_pdfs(self):
        input_dir = self.input_dir.get()
        output_file = self.output_file.get()

        if not input_dir or not output_file:
            messagebox.showerror(
                "Error",
                "Por favor selecciona una carpeta de entrada y un archivo de salida",
            )
            return

        try:
            input_dir_path = Path(input_dir)
            merger = PdfMerger()

            # Buscar todos los archivos PDF en la carpeta
            pdf_files = sorted(input_dir_path.glob("*.pdf"))

            if not pdf_files:
                self.log("No se encontraron archivos PDF para unificar.")
                return

            self.log(f"Encontrados {len(pdf_files)} archivos PDF para combinar.")

            # Actualizar la barra de progreso
            total_files = len(pdf_files)
            for i, pdf in enumerate(pdf_files, 1):
                self.log(f"Agregando {pdf.name} al archivo combinado.")
                merger.append(str(pdf))
                progress = (i / total_files) * 100
                self.progress_var.set(progress)
                self.root.update()

            # Guardar el archivo combinado
            merger.write(output_file)
            merger.close()
            self.log(f"Archivo combinado guardado en: {output_file}")
            messagebox.showinfo("Éxito", "Los PDFs se han combinado correctamente!")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
