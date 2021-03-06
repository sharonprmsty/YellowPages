# from tkinter import Y
import uuid

menu = ['1. Daftar Kontak ',
        '2. Tambah Kontak Baru',
        '3. Edit Kontak',
        '4. Hapus Kontak',
        '5. Keluar'
        ]

kontak = [{'UID': uuid.uuid4().hex[:8].upper(),
           'Nama': 'Budi',
           'NoTelp': '0888876543210',
           'Email': 'beubudeidibudi@gmail.com',
           'Alamat': 'Jalan Terus Gg. Jadian'}]


def show_kontak():
    show = True
    while show != '3':
        print('\n----------DAFTAR KONTAK @YELLOWPAGES----------')
        print('1. Lihat Daftar Seluruh Kontak')
        print('2. Lihat Kontak Pilihan')
        print('3. Kembali ke Menu Utama')
        show = input('Pilihan Anda [1-3] : ')
        if show == '1':
            if len(kontak) != 0:
                print('\n**Daftar Kontak**')
                for i, j in enumerate(kontak):
                    print(
                        f"{i+1}. UID : {j['UID']}, Nama : {j['Nama']}, No.Telp : {j['NoTelp']}, Email : {j['Email']}, Alamat : {j['Alamat']}")
                continue
            else:
                print('\n**YELLOWPAGES KOSONG!**\n')
            continue
        elif show == '2':
            if len(kontak) != 0:
                cari = input('Pencarian Nama : ').upper()
                print('\n**Hasil Pencarian Data Kontak', cari, '**')
                for i, j in enumerate(kontak):
                    if cari in j['Nama'].upper() or cari == j['Nama']:
                        print(
                            f"{i+1}. UID : {j['UID']}, Nama : {j['Nama']}, No.Telp : {j['NoTelp']}, Email : {j['Email']}, Alamat : {j['Alamat']}")
                        continue
                    elif i == len(kontak)-1 :
                        print(cari, 'TIDAK DITEMUKAN!')
                        break
            else:
                print('\n**YELLOWPAGES KOSONG!**')
        elif show == '3':
            main()
        else:
            print('\n**Masukkan Pilihan Menu yang Valid!**')
            show_kontak()


def add_kontak():
    add = True
    while add != '2':
        print('\n----------TAMBAH KONTAK BARU @YELLOWPAGES----------')
        print('1. Tambah Kontak Baru')
        print('2. Kembali ke Menu Utama')
        add = input('Pilihan Anda [1-2] : ')
        if add == '1':
            new = {}
            new['UID'] = uuid.uuid4().hex[:8].upper()
            new['Nama'] = input('Nama : ')
            new['NoTelp'] = input('Nomor Telepon : ')
            new['Email'] = input('Email : ')
            new['Alamat'] = input('Alamat : ')
            while add == '1':
                save = input('Apakah kontak akan disimpan? [Y/N]  ').lower()
                if save == 'y':
                    kontak.append(new)
                    print('\n**KONTAK BARU BERHASIL DISIMPAN!**')
                    break
                elif save == 'n':
                    print('\n**KONTAK BARU TIDAK DISIMPAN!**')
                    break
        elif add == '2':
            main()
        else:
            print('\n**Masukkan Pilihan Menu yang Valid!**')
            add_kontak()


def edit_kontak():
    edit = True
    while edit != '2':
        print('\n----------EDIT KONTAK @YELLOWPAGES----------')
        print('1. Edit Kontak Tersimpan')
        print('2. Kembali ke Menu Utama')
        edit = input('Pilihan Anda [1-2] : ')
        if edit == '1':
            cari = input('Masukkan Nama/UID Kontak untuk Diedit : ').upper()
            for i, j in enumerate(kontak):
                if cari == j['Nama'].upper() or cari == j['UID'].upper():
                    print(f"UID : {j['UID']}, Nama : {j['Nama']}, No.Telp : {j['NoTelp']}, Email : {j['Email']}, Alamat : {j['Alamat']}")
                    while edit == '1':
                        edit_deal = input('Apakah pengeditan kontak akan dilanjutkan? [Y/N] ').lower()
                        if edit_deal == 'y':
                            kolom = input(
                                'Masukkan Kolom yang Akan Diedit [Nama/NoTelp/Email/Alamat] : ').upper()
                            if kolom == 'NAMA':
                                nama = input('Masukkan Nama Baru : ')
                                while edit == '1':
                                    save = input('Apakah hasil pengeditan akan disimpan? [Y/N] ').lower()
                                    if save == 'y':
                                        j['Nama'] = nama
                                        print(f"{j['Nama']} - {j['NoTelp']} - {j['Email']} - {j['Alamat']}")
                                        print('\n**PENGEDITAN BERHASIL DISIMPAN**')
                                        break
                                    elif save == 'n':
                                        print('\n**PENGEDITAN DIBATALKAN!**')
                                        break
                                break
                            elif kolom == 'NOTELP' or kolom == 'NOMOR' or kolom == 'NOMORTELP':
                                notelp = input('Masukkan No.Telp Baru : ')
                                while edit == '1':
                                    save = input('Apakah hasil pengeditan akan disimpan? [Y/N] ').lower()
                                    if save == 'y':
                                        j['NoTelp'] = notelp
                                        print(f"{j['Nama']} - {j['NoTelp']} - {j['Email']} - {j['Alamat']}")
                                        break
                                    elif save == 'n':
                                        print('\n**PENGEDITAN DIBATALKAN!**')
                                        break
                                break
                            elif kolom == 'EMAIL':
                                email = input('Masukkan Email Baru : ')
                                while edit == '1':
                                    save = input('Apakah hasil pengeditan akan disimpan? [Y/N] ').lower()
                                    if save == 'y':
                                        j['Email'] = email
                                        print(f"{j['Nama']} - {j['NoTelp']} - {j['Email']} - {j['Alamat']}")
                                        break
                                    elif save == 'n':
                                        print('\n**PENGEDITAN DIBATALKAN!**')
                                        break
                                break
                            elif kolom == 'ALAMAT':
                                alamat = input('Masukkan Alamat Baru : ')
                                while edit == '1':
                                    save = input('Apakah hasil pengeditan akan disimpan? [Y/N] ').lower()
                                    if save == 'y':
                                        j['Alamat'] = alamat
                                        print(f"{j['Nama']} - {j['NoTelp']} - {j['Email']} - {j['Alamat']}")
                                        break
                                    elif save == 'n':
                                        print('\n**PENGEDITAN DIBATALKAN!**')
                                        break
                                break
                            else:
                                print('\n**Masukkan Kolom yang Valid!**')
                            break
                        elif edit_deal == 'n':
                            print('\n**PENGEDITAN KONTAK DIBATALKAN!**')
                            break
                elif i==len(kontak)-1 and (cari!=j['Nama'].upper() or cari!=j['UID'].upper()):
                    print('\n**TIDAK ADA KONTAK YANG COCOK!**')
        elif edit == '2':
            main()
        else:
            print('\n**Masukkan Pilihan Menu yang Valid!**')
            edit_kontak()


def delete_kontak():
    delete = True
    while delete != '2':
        print('\n----------HAPUS KONTAK @YELLOWPAGES----------')
        print('1. Hapus Kontak Tersimpan')
        print('2. Kembali ke Menu Utama')
        delete = input('Pilihan Anda [1-2] : ')
        if delete == '1':
            cari = input('Masukkan Nama Kontak untuk Dihapus : ').upper()
            for i, j in enumerate(kontak):
                if cari == j['Nama'].upper():
                    print(
                        f"{j['Nama']} - {j['NoTelp']} - {j['Email']} - {j['Alamat']} ditemukan.")
                    while delete == '1':
                        del_deal = input('Apakah Anda yakin menghapus kontak tersebut? [Y/N] ').lower()
                        if del_deal == 'y':
                            del kontak[i]
                            print('\n**KONTAK BERHASIL DIHAPUS!**')
                            break
                        elif del_deal == 'n':
                            print('\n**PENGHAPUSAN KONTAK DIBATALKAN!**')
                            break
                    break
                elif i == len(kontak)-1 and cari != j['Nama'].upper():
                    print('\n**TIDAK ADA KONTAK YANG COCOK!**\n')
                    break
        elif delete == '2':
            main()
        else:
            print('\n**Masukkan Pilihan Menu yang Valid!**')
            delete_kontak()


def main():
    main_menu = True
    while main_menu == True:
        print('\n----------SELAMAT DATANG @YellowPages!----------')
        print(*menu, sep='\n')
        main_menu = input('Silakan Pilih Main_Menu [1-5] : ')
        if main_menu == '1':
            show_kontak()
            break
        elif main_menu == '2':
            add_kontak()
            break
        elif main_menu == '3':
            edit_kontak()
            break
        elif main_menu == '4':
            delete_kontak()
            break
        elif main_menu == '5':
            print('\n**Sampai Jumpa Lagi @YellowPages!**\n')
            main_menu=False
        else:
            print('\n**Masukkan Pilihan Menu yang Valid!**')
            main()
    
if __name__ == "__main__":
    main()
