import tkinter as tk
from tkinter import ttk
from tkinter import font

class NutrisiKalkulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Pengukur Berat Badan dan Nutrisi")
        self.root.geometry("600x400")

        
        self.helvetica_font = font.Font(family='Helvetica', size=12)

        self.buat_widget()

    def buat_widget(self):
        
        self.label_berat_badan = ttk.Label(self.root, text="Berat Badan (kg):", font=self.helvetica_font)
        self.label_berat_badan.grid(row=0, column=0, padx=10, pady=10, sticky="W")
        self.entry_berat_badan = ttk.Entry(self.root, font=self.helvetica_font)
        self.entry_berat_badan.grid(row=0, column=1, padx=10, pady=10)

        
        self.label_tinggi_badan = ttk.Label(self.root, text="Tinggi Badan (cm):", font=self.helvetica_font)
        self.label_tinggi_badan.grid(row=1, column=0, padx=10, pady=10, sticky="W")
        self.entry_tinggi_badan = ttk.Entry(self.root, font=self.helvetica_font)
        self.entry_tinggi_badan.grid(row=1, column=1, padx=10, pady=10)

        
        self.button_hitung = ttk.Button(self.root, text="Hitung", command=self.hitung_nutrisi, style='TButton', cursor="hand2")
        self.button_hitung.grid(row=2, column=0, columnspan=2, pady=10)

        
        self.label_hasil = ttk.Label(self.root, text="", font=self.helvetica_font)
        self.label_hasil.grid(row=3, column=0, columnspan=2, pady=10)

      
        self.label_waktu_makan = ttk.Label(self.root, text="Rekomendasi Waktu Makan:", font=self.helvetica_font)
        self.label_waktu_makan.grid(row=4, column=0, padx=10, pady=10, sticky="W")
        self.entry_waktu_makan = ttk.Entry(self.root, state="readonly", font=self.helvetica_font)
        self.entry_waktu_makan.grid(row=4, column=1, padx=10, pady=10)

    def hitung_nutrisi(self):
        try:
            berat_badan = float(self.entry_berat_badan.get())
            tinggi_badan = float(self.entry_tinggi_badan.get()) / 100  
            hasil = self.hitung_bmi(berat_badan, tinggi_badan)
            deskripsi_nutrisi = self.deskripsi_nutrisi(hasil)
            waktu_makan = self.rekomendasi_waktu_makan(deskripsi_nutrisi)
            
            self.tampilkan_hasil(hasil, deskripsi_nutrisi, waktu_makan)
        except ValueError:
            self.label_hasil.config(text="Masukkan berat badan dan tinggi badan yang valid.")

    def hitung_bmi(self, berat_badan, tinggi_badan):
        bmi = berat_badan / (tinggi_badan ** 2)
        return bmi

    def deskripsi_nutrisi(self, hasil):
        if hasil < 18.5:
            return "Anda termasuk dalam kategori Ectomorph. Disarankan untuk meningkatkan asupan kalori dan protein."
        elif 18.5 <= hasil < 24.9:
            return "Anda termasuk dalam kategori Normal. Pertahankan pola makan sehat dan seimbang."
        else:
            return "Anda termasuk dalam kategori Endomorph. Disarankan untuk mengontrol asupan kalori dan fokus pada latihan aerobik."

    def rekomendasi_waktu_makan(self, deskripsi):
        if "Ectomorph" in deskripsi:
            return "Rekomendasi waktu makan untuk Ectomorph adalah lebih sering dalam porsi kecil, minimal 6 kali sehari."
        elif "Endomorph" in deskripsi:
            return "Rekomendasi waktu makan untuk Endomorph adalah dalam porsi lebih sedikit tetapi lebih sering, minimal 5-6 kali sehari."
        else:
            return "Tidak ada rekomendasi waktu makan khusus untuk kategori ini."

    def tampilkan_hasil(self, hasil, deskripsi, waktu_makan):
        kategori = ""
        if hasil < 18.5:
            kategori = "Berat Badan Kurang"
        elif 18.5 <= hasil < 24.9:
            kategori = "Berat Badan Normal"
        else:
            kategori = "Berat Badan Berlebih"

        self.label_hasil.config(text=f"Indeks Massa Tubuh (BMI): {hasil:.2f}\nKategori: {kategori}\n{deskripsi}", font=self.helvetica_font)
        self.entry_waktu_makan.config(state="normal")
        self.entry_waktu_makan.delete(0, tk.END)
        self.entry_waktu_makan.insert(0, waktu_makan)
        self.entry_waktu_makan.config(state="readonly")


if __name__ == "__main__":
    root = tk.Tk()

    
    style = ttk.Style()
    style.configure('TButton', font=('Helvetica', 12))

    aplikasi = NutrisiKalkulator(root)
    root.mainloop()
