from tabulate import tabulate

data_pasien = [
    [1, "BUDI", "L", "DEMAM", "Dr. RINI", "UMUM", "SELESAI"],
    [2, "ANI", "P", "FLU", "Dr. SYAFII", "BPJS", "BERJALAN"],
    [3, "CITRA", "P", "PUSING", "Dr. RAMA", "BPJS", "SELESAI"],
    [4, "DIKA", "L", "BATUK", "Dr. RINI", "UMUM", "BERJALAN"]
]

def read():
    while True:
        print("\n~~~Menu Read~~~")
        print("1. Tampilkan Semua Data")
        print("2. Tampilkan Data berdasarkan ID")
        print("3. Kembali ke Menu Utama")
        choice = input("Pilih cara tampilan (1-3): ")

        if choice == "1":
            if not data_pasien :
                print("\nTidak Ada data Pasien\n")
            else:
                headers = ["ID", "Nama", "Jenis Kelamin", "Keluhan", "Dokter", "Status BPJS", "Status Pelayanan"]
                print(tabulate(data_pasien,headers=headers,tablefmt="grid"))
        elif choice == "2":
            while True:
                try:    
                 index = int(input("Masukkan id pasien yang ingin dilihat: "))
                 break
                except ValueError:
                    print("\n !!!Data ID Pasien Hanya Berupa Angka!!!\n Coba lagi\n")
            found = False
            for pasien in data_pasien:
                if pasien[0]== index:
                    found = True
                    headers = ["ID", "Nama", "Jenis Kelamin", "Keluhan", "Dokter", "Status BPJS", "Status Pelayanan"]
                    print(tabulate([pasien],headers=headers,tablefmt="grid"))
                    break
                else  :
                    print(f"\nData dengan ID pasien {index} tidak ditemukan\n")
        elif choice == "3":
            break
        else:
            print("\n +++ Pilihan tidak valid. Silakan coba lagi. +++\n")

def create():
    while True:
        print("\n~~~Menambahkan Data Pasien~~~")
        print("1. Masukkan Data Pasien ")
        print("2. Kembali ke Menu Utama")
        choice = input("Pilih menu: ")

        if choice == '1':
            ##ID PASIEN
            while True:
                try:    
                    index = int(input("Masukkan ID Pasien (Hanya Berupa Angka): "))
                    if any(pasien[0]==index for pasien in data_pasien):
                        print("\nID Pasien Sudah Ada\nSilahkan Masukkan ID Lain\n")
                        break
                    else:
                        break
                except ValueError:
                    print("\n !!!Data ID Pasien Hanya Berupa Angka!!!\n Coba lagi\n ")
            ##NAMA
            while True:
                nama = input("Masukkan Nama Pasien: ")
                if nama.isalpha():
                    break
                else:
                    print("\nNama harus berupa huruf. Masukkan Nama Lagi.\n")
            ## JENIS KELAMIN
            while True:
                jenis_kelamin = input("Masukkan Jenis Kelamin (L/P): ")
                if jenis_kelamin in ['L','l','p','P'] and jenis_kelamin.isalpha():
                    break
                else:
                    print(("\nJenis kelamin hanya bisa diisi dengan 'L' atau 'P'.\n "))
            ##KELUHAN
            while True:
                keluhan = input("Masukkan Keluhan Pasien: ")
                if len(keluhan)>= 3 and keluhan.isalpha():
                    break
                else:
                    print(("\nMasukkan keluhan Pasien yang Benar\n"))
            ##DOKTER
            while True:
                dokter = input("Masukkan Nama Dokter (Tanpa Gelar): ")
                if dokter.isalpha():
                    break
                else:
                    print("\nNama harus berupa huruf. Masukkan Nama Lagi.\n")
            dokter= 'Dr. '+dokter
            ##STATUSBPJS
            while True:
                status_bpjs = input("Masukkan Status BPJS (BPJS/UMUM): ").lower()
                if status_bpjs in ['umum','bpjs'] and status_bpjs.isalpha():
                    break
                else:
                    print(("\nStatus BPJS hanya bisa diisi dengan 'BPJS' atau 'UMUM'.\n "))
            ##STATUS PELAYANAN
            while True:
                status_pelayanan = input("Masukkan Status Pelayanan Pasien (Selesai/Berjalan): ").lower()
                if status_pelayanan in ['selesai','Berjalan'] and status_pelayanan.isalpha():
                    break
                else:
                    print(("\nStatus Pelayanan hanya bisa diisi dengan 'Berjalan' atau 'Selesai'. \n"))
 
            data_pasien.append([index, nama.upper(), jenis_kelamin.upper(), keluhan.upper(), dokter.upper(), status_bpjs.upper(), status_pelayanan.upper()])
            
            while True:
                save_choice = input("Apakah Anda Ingin Menyimpan Data? (Y/N): ") 
                if save_choice.lower() == 'y'and 'Y':
                    print("Data berhasil ditambahkan.")
                    break
                elif save_choice.lower() == 'n' and 'N':
                    break
                else:
                    print("\nMasukkan huruf Y/N\n")
        elif choice == '2':
            break
        else:
            print("\n +++ Pilihan tidak valid. Silakan coba lagi. +++\n")
        
def update():
    while True:
        print("\n~~Mengedit Data Pasien")
        print("1. Masukkan Data Pasien ")
        print("2. Kembali ke Menu Utama")
        choice = input("Pilih menu: ")

        if choice == '1':
            while True:
                index_input = input("Masukkan Index Pasien yang Ingin Diubah: ")
                for pasien in data_pasien:
                    if str(pasien[0]) == index_input:
                        headers = ["ID", "Nama", "Jenis Kelamin", "Keluhan", "Dokter", "Status BPJS", "Status Pelayanan"]
                        print(tabulate([pasien], headers=headers, tablefmt="grid"))
                        confirm = input("Apakah Anda ingin mengubah data pasien ini? (Y/N): ")
                        if confirm.lower() == 'y':
                            while True:
                                column_name = input("Masukkan nama kolom yang ingin diubah: ")
                                if column_name.lower() in ["ID", "nama", "jenis kelamin", "keluhan", "dokter", "status bpjs", "status pelayanan"]:
                                    new_data = input(f"Masukkan data baru untuk {column_name.capitalize()}: ")
                                    ##UBAH NO ID
                                    if column_name.lower() == "ID":
                                        try:
                                            new_data = int(new_data)
                                            if any(pasien[0] == new_data for pasien in data_pasien):
                                                print("\nID Pasien Sudah Ada\nSilahkan Masukkan ID Lain\n")
                                                continue
                                            else:
                                                pasien[0] = new_data
                                                break
                                        except ValueError:
                                            print("\n !!!Data ID Pasien Hanya Berupa Angka!!!\n Coba lagi\n ")
                                            continue
                                    ##UBAH NAMA
                                    elif column_name.lower() == "nama":
                                        if new_data.isalpha():
                                            pasien[1] = new_data.upper()
                                            break
                                        else:
                                            print("\nNama harus berupa huruf. Masukkan Nama Lagi.\n")
                                            continue
                                    ##UBAH JENIS KELAMIN
                                    elif column_name.lower() == "jenis kelamin":
                                        if new_data.lower() in ['l', 'p']:
                                            pasien[2] = new_data.upper()
                                            break
                                        else:
                                            print("\nJenis kelamin hanya bisa diisi dengan 'L' atau 'P'.\n ")
                                            continue
                                    ##UBAH KELUHAN
                                    elif column_name.lower() == "keluhan":
                                        if len(new_data) >= 3 and new_data.isalpha():
                                            pasien[3] = new_data.capitalize()
                                            break
                                        else:
                                            print("\nMasukkan keluhan Pasien yang Benar\n")
                                            continue
                                    ##UBAH DOKTER
                                    elif column_name.lower() == "dokter":
                                        if new_data.isalpha():
                                            pasien[4] = "Dr. " + new_data.capitalize()
                                            break
                                        else:
                                            print("\nNama harus berupa huruf. Masukkan Nama Lagi.\n")
                                            continue
                                    ##UBAH STATUS BPJS
                                    elif column_name.lower() == "status bpjs":
                                        if new_data.lower() in ['bpjs', 'umum']:
                                            pasien[5] = new_data.upper()
                                            break
                                        else:
                                            print("\nStatus BPJS hanya bisa diisi dengan 'BPJS' atau 'UMUM'.\n ")
                                            continue
                                    ##UBAH STATUS PELAYANAN
                                    elif column_name.lower() == "status pelayanan":
                                        if new_data.lower() in ['selesai', 'berjalan']:
                                            pasien[6] = new_data.capitalize()
                                            break
                                        else:
                                            print("\nStatus Pelayanan hanya bisa diisi dengan 'Berjalan' atau 'Selesai'. \n")
                                            continue
                                else:
                                    print("\nNama kolom tidak valid.\n")
                                    continue
                            print("Data berhasil diupdate.")
                        elif confirm.lower() == 'n':
                            print("\nUpdate dibatalkan.\n")
                        else:
                            print("\nPilihan tidak valid.\n")
                        break
                else:
                    print(f"Data dengan index {index_input} tidak ditemukan.")
                break
        elif choice == '2':
            break
        else:
            print("\nInputan Tidak Tersedia\n")

def delete():
    while True:
        print("\n~~~~Menghapus Data Pasien~~~~")
        print("1. Hapus Data berdasarkan ID")
        print("2. Hapus Semua Data Pasien")
        print("3. Kembali ke Menu Utama")
        choice = input("Pilih menu: ")
        if choice == '1':
            while True:
                indexInput = (input("pilih ID Pasien yang ingin di hapus: "))
                if indexInput.isdigit():
                    index = int(indexInput)
                    pasien= next((pasien for pasien in data_pasien if pasien[0]== index), None)
                    if pasien:
                        headers = ["ID", "Nama", "Jenis Kelamin", "Keluhan", "Dokter", "Status BPJS", "Status Pelayanan"]
                        print(tabulate([pasien],headers=headers,tablefmt='grid'))
                        confirm = input("Apakah Data di Atas Ingin Dihapus?(Y/N): ")
                        if confirm.lower()== 'y' and 'Y':
                            data_pasien.remove(pasien)
                            print("Data Berhasil Dihapus")
                            break
                        elif confirm.lower() == 'n' and 'N':
                            break
                        else: 
                            print("\nMasukkan Y/N\n")
                    else:
                        print(f"\nData Pasien dengan ID {index} tidak ada\n")
                        break
                else:
                    print("\n Input Berupa Angka.\nSilahkan Coba Lagi.\n")
                        
        elif choice == '2':
            confirm = input("Apakah yakin ingin menghapus seluruh data?(Y/N): ")
            if confirm.lower() == 'y':
                data_pasien.clear()
                print("Seluruh Data Pasien Telah Dihapus")
                break
            elif confirm.lower() == 'n' and 'N':
                break
            else: 
                print("\nMasukkan Y/N")
                delete()
    
        elif choice == '3':
            break
        else:
            print("\n +++ Pilihan tidak valid. Silakan coba lagi. +++\n")

def main():
    while True:
        print("\n\t~~~Pendataan Pasien Rumah Sakit Harapan Bangsa~~~")
        print("1. Melihat data Pasien")
        print("2. Menambahkan data pasien")
        print("3. Merubah data pasien")
        print("4. Hapus data pasien")
        print("5. Exit")
        choice = input("Pilih operasi (1-5): ")

        ##SUB MENU
        if choice == "1":
            read()            
        elif choice == "2":
            create()
        elif choice == "3":
           update()
        elif choice == "4":
            delete()
        elif choice == "5":
            print("\n ****Anda Telah keluar Aplikasi**** ")
            break
        else:
            print("\n +++ Pilihan tidak valid. Silakan coba lagi. +++")
main()