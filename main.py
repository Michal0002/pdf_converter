import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from fpdf import FPDF

class ImageToPDFApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Converter")
        self.root.geometry("400x200")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        self.file_path = ""
        self.create_widgets()

    def create_widgets(self):
        button_font = ("Arial", 12)
        label_font = ("Arial", 10)
        button_bg = "#4CAF50"
        button_fg = "#FFFFFF"

        self.upload_button = tk.Button(self.root, text="Insert JPG/PNG file", command=self.upload_file,
                                       font=button_font, bg=button_bg, fg=button_fg)
        self.upload_button.pack(pady=10)

        self.file_label = tk.Label(self.root, text="Selected file: None", font=label_font, bg="#f0f0f0", wraplength=350, justify="left")
        self.file_label.pack(pady=5)

        self.generate_button = tk.Button(self.root, text="Generate PDF", command=self.generate_pdf,
                                         font=button_font, bg=button_bg, fg=button_fg)
        self.generate_button.pack(pady=10)

    def upload_file(self):
        file_types = [("Image files", "*.png;*.jpg;*.jpeg")]
        self.file_path = filedialog.askopenfilename(filetypes=file_types)

        if self.file_path:
            self.file_label.config(text=f"Selected file: {self.file_path}")
            messagebox.showinfo("File selected", f"Selected file: {self.file_path}")
        else:
            messagebox.showwarning("No file", "No file selected!")

    def generate_pdf(self):
        if not self.file_path:
            messagebox.showwarning("No file", "Upload a file to do this step")
            return

        try:
            image = Image.open(self.file_path)
            pdf = FPDF()
            pdf.add_page()

            pdf_image_path = self.file_path.rsplit('.', 1)[0] + '.jpg'
            image.save(pdf_image_path, "JPEG")

            pdf.image(pdf_image_path, x=10, y=10, w=190)
            pdf_output_path = self.file_path.rsplit('.', 1)[0] + ".pdf"
            pdf.output(pdf_output_path)
            messagebox.showinfo("PDF generated", f"PDF file generated: {pdf_output_path}")

        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToPDFApp(root)
    root.mainloop()
