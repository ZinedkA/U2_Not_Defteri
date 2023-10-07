import tkinter as tk
from tkinter import filedialog

class NotDefterim:
    def __init__(self, root):
        self.root = root
        self.root.title("YEA Not Defteri")

        self.text_area = tk.Text(root, wrap="word")
        self.text_area.pack(expand="yes", fill="both")

        menu_bar = tk.Menu(root)
        root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Dosya", menu=file_menu)
        file_menu.add_command(label="Yeni", command=self.yeni_dosya)
        file_menu.add_command(label="Aç", command=self.dosya_ac)
        file_menu.add_command(label="Kaydet", command=self.dosya_kaydet)
        file_menu.add_separator()
        file_menu.add_command(label="Çıkış", command=self.cikis_sorgula)

        # Pencere kapatma işlemi için protocol ekleme
        root.protocol("WM_DELETE_WINDOW", self.cikis_sorgula)

    def yeni_dosya(self):
        self.yeni_pencere = tk.Toplevel(self.root)
        self.yeni_pencere.title("Yeni Dosya")

        text_area_new = tk.Text(self.yeni_pencere, wrap="word")
        text_area_new.pack(expand="yes", fill="both")

        menu_bar_new = tk.Menu(self.yeni_pencere)
        self.yeni_pencere.config(menu=menu_bar_new)

        file_menu_new = tk.Menu(menu_bar_new, tearoff=0)
        menu_bar_new.add_cascade(label="Dosya", menu=file_menu_new)
        file_menu_new.add_command(label="Yeni", command=self.yeni_dosya)
        file_menu_new.add_command(label="Aç", command=self.dosya_ac)
        file_menu_new.add_command(label="Kaydet", command=self.dosya_kaydet)
        file_menu_new.add_separator()
        file_menu_new.add_command(label="Çıkış", command=self.yeni_pencere.destroy)

    def dosya_ac(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            self.yeni_pencere = tk.Toplevel(self.root)
            self.yeni_pencere.title("Dosya Aç")

            text_area_new = tk.Text(self.yeni_pencere, wrap="word")
            text_area_new.pack(expand="yes", fill="both")
            text_area_new.insert(tk.END, content)

            menu_bar_new = tk.Menu(self.yeni_pencere)
            self.yeni_pencere.config(menu=menu_bar_new)
           
            file_menu_new = tk.Menu(menu_bar_new, tearoff=0)
            menu_bar_new.add_cascade(label="Dosya", menu=file_menu_new)
            file_menu_new.add_command(label="Yeni", command=self.yeni_dosya)
            file_menu_new.add_command(label="Aç", command=self.dosya_ac)
            file_menu_new.add_command(label="Kaydet", command=self.dosya_kaydet)
            file_menu_new.add_separator()
            file_menu_new.add_command(label="Çıkış", command=self.yeni_pencere.destroy)

    def dosya_kaydet(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Metin Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)

    def cikis_sorgula(self):
        self.yeni_pencere = tk.Toplevel(self.root)
        self.yeni_pencere.title("Emin misiniz?")

        # Etiket
        etiket = tk.Label(self.yeni_pencere, text="Çıkış Yapmak Üzeresiniz")
        etiket.pack(pady=(self.yeni_pencere.winfo_reqheight() - etiket.winfo_reqheight()) // 2)
        etiket.pack(pady=(self.yeni_pencere.winfo_reqwidth() - etiket.winfo_reqwidth()) // 2)

        # Evet ve Hayır düğmeleri
        evet_dugme = tk.Button(self.yeni_pencere, text="Devam", command=self.root.destroy)
        evet_dugme.pack(side=tk.LEFT, padx=10)

        hayir_dugme = tk.Button(self.yeni_pencere, text="İptal", command=self.yeni_pencere.destroy)
        hayir_dugme.pack(side=tk.RIGHT, padx=10)

if __name__ == "__main__":
    root = tk.Tk()
    not_defteri = NotDefterim(root)
    root.mainloop()
