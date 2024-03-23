class Kosmetik:
    def __init__(self, nama, harga_supplier):
        self.nama = nama
        self.harga_supplier = harga_supplier
        self.harga_jual = harga_supplier * 1.1  # Harga jual = harga supplier + 10%

    def hitung_modal(self, jumlah):
        return self.harga_supplier * jumlah

    def hitung_laba(self, jumlah):
        return (self.harga_jual - self.harga_supplier) * jumlah

def hitung_total_modal(kosmetik_list, jumlah_list):
    total_modal = sum(kosmetik.hitung_modal(jumlah) for kosmetik, jumlah in zip(kosmetik_list, jumlah_list))
    return total_modal

def hitung_total_laba(kosmetik_list, jumlah_list):
    total_laba = sum(kosmetik.hitung_laba(jumlah) for kosmetik, jumlah in zip(kosmetik_list, jumlah_list))
    return total_laba

def main():
    kosmetik_list = [
        Kosmetik("Lipstik", 50000),
        Kosmetik("Bedak", 75000),
        Kosmetik("Maskara", 60000)
    ]
    jumlah_list = [10, 20, 15]  # Jumlah barang yang dibeli dari masing-masing jenis kosmetik

    total_modal = hitung_total_modal(kosmetik_list, jumlah_list)
    total_laba = hitung_total_laba(kosmetik_list, jumlah_list)

    print(f"Total modal yang dikeluarkan: Rp {total_modal:,.2f}")
    print(f"Total laba yang didapat: Rp {total_laba:,.2f}")

if __name__ == "__main__":
    main()
