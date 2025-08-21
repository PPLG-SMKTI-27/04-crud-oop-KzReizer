class Buku:
    def __init__(self, isbn, judul, pengarang, jumlah, terpinjam=0):
        self.isbn = str(isbn)
        self.judul = judul
        self.pengarang = pengarang
        self.jumlah = jumlah
        self.terpinjam = terpinjam

class records:
    def __init__(self, isbn, status, tanggalpinjam, tanggalkembali):
        self.isbn = str(isbn)
        self.status = status
        self.tanggalpinjam = tanggalpinjam
        self.tanggalkembali = tanggalkembali


# data buku
books = [
    {"isbn":"9786237121144", "judul":"Kumpulan Solusi ", "pengarang":"Budi Rrjo", "jumlah":6, "terpinjam":0},
    {"isbn":"9786231800718", "judul":"Dasar-Dasar  ", "pengarang":"Okta Pawan", "jumlah":15, "terpinjam":0},
    {"isbn":"9786026163905", "judul":"Analisis ", "pengarang":"Adi Sulisyo ", "jumlah":2, "terpinjam":1},
    {"isbn":"9786022912828", "judul":"Animal Farm", "pengarang":"George ", "jumlah":4, "terpinjam":0}
]

# data peminjaman
records = [
    {"isbn":"9786022912828", "status":"Selesai", "tanggalpinjam":"2025-03-21", "tanggalkembali":"2025-03-28"},
    {"isbn":"9786026163905", "status":"Belum", "tanggalpinjam":"2025-07-22", "tanggalkembali":""}
]

def tampilkan_data():
    print(f"{'NO':<3} {'ISBN':<15} {'Judul Buku':<25} {'Pengarang':<25} {'Jumlah':<7} {'Terpinjam':<9}")
    for i, b in enumerate(books, 1):
        print(f"{i:<3} {str(b['isbn']):<15} {b['judul']:<25} {b['pengarang']:<25} {b['jumlah']:<7} {b['terpinjam']:<9}")
    

def tambah_data():
    isbn = int(input("Masukan Isbn: "))
    Judul = input("Masukan judulnya ")
    pengarang = input("Masukan nama pengarangnya: ")
    jumblah = int(input("Masukan jumblah buku: "))
    terpinjam = int(input("Masukan jumblah buku yang terpinjam: "))
    bukubaru = {"isbn": isbn, "judul": Judul, "pengarang": pengarang, "jumlah": jumblah, "terpinjam": terpinjam}
    books.append(bukubaru)
    print("buku berhasil ditambahkan")
    

def edit_data():
    tampilkan_data()
    print("\n=== Selamat Datang Di Menu Ganti Buku ===")
    nomor = int(input("masukan nomor buku yang ingin diganti: ")) -1
    books[nomor]["isbn"] = int(input("masukan nomor isbn yang baru: "))
    books[nomor]["judul"] = input("masukan judul buku yang baru: ")
    books[nomor]["pengarang"] = input("masukan pengarang buku yang baru: ")
    books[nomor]["jumlah"] = int(input("masukan jumblah buku yang baru: "))
    books[nomor]["terpinjam"] = int(input("masukan jumblah buku yang terpinjam: "))
    print("buku berhasil diganti")


def hapus_data():
    tampilkan_data()
    print("\n=== Selamat Datang Di Menu Hapus Buku ===")    
    nomor = int(input("masukan nomor buku yang ingin dihapus: ")) -1
    books.pop(nomor)
    print("buku berhasil dihapus")
    

def tampilkan_peminjaman():
    print(f"{'NO':<3} {'ISBN':<15} {'Status':<10} {'Tanggal Pinjam':<15} {'Tanggal Kembali':<15}")
    for i, r in enumerate(records, 1):
        print(f"{i:<3} {str(r['isbn']):<15} {r['status']:<10} {r['tanggalpinjam']:<15} {r['tanggalkembali']:<15}")

def tampilkan_belum():
    print(f"{'NO':<3} {'ISBN':<15} {'Status':<10} {'Tanggal Pinjam':<15} {'Tanggal Kembali':<15}")
    no = 1
    for r in records:
        if r['status'].lower() == "belum":
            print(f"{no:<3} {str(r['isbn']):<15} {r['status']:<10} {r['tanggalpinjam']:<15} {r['tanggalkembali']:<15}")
            no += 1
    if no == 1:
        print("Tidak ada peminjaman yang belum kembali.")

def peminjaman():
    print("\n=== Selamat Datang Di Menu Peminjaman Buku ===")
    tampilkan_data()
    isbn = input("Masukan ISBN buku yang ingin dipinjam: ")
    tanggalpinjam = input("Masukan tanggal peminjaman: ")
    for b in books:
        if str(b['isbn']) == str(isbn):
            if b['jumlah'] > b['terpinjam']:
                b['terpinjam'] += 1
                records.append({
                    "isbn": str(isbn),
                    "status": "Belum",
                    "tanggalpinjam": tanggalpinjam,
                    "tanggalkembali": ""
                })
                print("Buku berhasil dipinjam.")
                return
            else:
                print("Stok buku habis, tidak bisa dipinjam.")
                return
    print("Buku tidak ditemukan.")

def pengembalian():
    print("\n=== Selamat Datang Di Menu Pengembalian Buku ===")
    isbn = input("Masukan ISBN buku yang ingin dikembalikan: ")
    tanggalkembali = input("Masukan tanggal pengembalian: ")
    for r in records:
        if str(r['isbn']) == str(isbn) and r['status'].lower() == "belum":
            r['status'] = "Selesai"
            r['tanggalkembali'] = tanggalkembali
            for b in books:
                if str(b['isbn']) == str(isbn):
                    if b['terpinjam'] > 0:
                        b['terpinjam'] -= 1
                    print("Buku berhasil dikembalikan.")
                    return
            print("Data buku tidak ditemukan.")
            return
    print("Data peminjaman tidak ditemukan atau sudah dikembalikan.")
    

status = True
while status:
    print("---=== MENU ===---")
    print("[1] Tampilkan Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("------------------")
    print("[5] Tampilkan Semua Peminjaman")
    print("[6] Tampilkan Peminjaman Belum Kembali")
    print("[7] Peminjaman")
    print("[8] Pengembalian")
    print("[X] Keluar")

    menu = input("Masukkan pilihan menu (1-8 atau x): ")

    match menu:
            case "1":
                tampilkan_data()
                
            case "2":
                tambah_data()
                
            case "3":
                edit_data()
                
            case "4":
                hapus_data()
            case "5":
                tampilkan_peminjaman()
            case "6":
                tampilkan_belum()
            case "7":
                peminjaman()
            case "8":
                pengembalian()
            case "x" | "X":
                print("anda keluar")
                print("=== Terima Kasih  ===")
                status = False
            case _:
                print("Pilihan tidak valid, silakan coba lagi.")