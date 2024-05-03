import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import ImageTk, Image

class QRCodeGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("QR")

        self.label = tk.Label(self.master, text="Введи ссылку для которой ты хочешь создать QR код:")
        self.label.pack()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.button = tk.Button(self.master, text="Создать QR-код", command=self.generate_qr_code)
        self.button.pack()

        self.image_label = tk.Label(self.master)
        self.image_label.pack()

    def generate_qr_code(self):
        data = self.entry.get()

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        self.qr_img = ImageTk.PhotoImage(img)
        self.image_label.config(image=self.qr_img)

def main():
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
