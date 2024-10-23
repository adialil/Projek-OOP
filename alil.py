# praktek ke-3
# Membuat sebuah sistem restoran sederhana menggunakan OOP
# Intraksi antar Objek

class MenuItem:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
        
    def __str__(self):
        return f"{self.nama} - ${self.harga:.2f}"
    
class Pelanggan:
    def __init__(self, nama):
        self.nama = nama
        self.pesanan = []
        
    def pesan(self, menu_item):
        self.pesanan.append(menu_item)
        print(f"{self.nama} memesan {menu_item}")
        
    def bayar(self):
        total = sum(item.harga for item in self.pesanan)
        return total
    
class Pelayan:
        def __init__(self, nama):
            self.nama = nama
            
        def ambil_pesanan(self, pelanggan):
            print(f"{self.nama} mengambil pesanan dari {pelanggan.nama}")
            
        def ambil_pesanan(self, pelanggan):
            total = pelanggan.bayar()
            print(f"{self.nama} mengantarkan pesanan kepada {pelanggan.nama}")
            print(f"Total tagihan: ${total:.2f}")
            
class Dapur:
    def __init__(self):
        self.menu ={
        "Piszaa": MenuItem("Piszaa", 50.00),
        "Bakso" : MenuItem("Bakso", 10.00),
        "Mie" : MenuItem("Mie", 12.00),
        }
    def siapkan_pesanan(self, pesanan):
        for item in pesanan:
            if item.nama in self.menu:
                print("fMenyediakan {item} dengan harga ${item.harga:.2f}")
            else:
                print(f"{item.nama} tidak ada dalam menu")
                
                
                pelanggan = Pelanggan("Nopal")
                pelayan = Pelayan("Adi")
                dapur = Dapur()
            
                Bakso = MenuItem("Bakso", 10.00)
                Piszaa= MenuItem("Piszaa", 50.00)
                
                Pelanggan.pesan(Bakso)