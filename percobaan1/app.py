from termcolor import colored
from constants import soal_ipa, soal_umum, soal_pkn
from prettytable import PrettyTable
from utils import line
from soal import Soal


def main():
    soal = Soal()
    while True:
        line(43, "green")
        print(colored(
            "✌️  Selamat Datang di QuiPy - Kelompok 6 ✌️ \n\t Aplikasi Quiz Sederhana", "red"))
        line(43, "green")

        print("1. UMUM")
        print("2. IPA")
        print("3. PKN")
        line(26, "green")

        while True:
            try:
                tipe_soal = int(
                    input("Masukkan Pilihan (default acak) : ") or "4")
                jumlah_soal = int(
                    input("Masukkan jumlah soal (default 10) : ") or "10")
                break
            except:
                print(colored("Data tidak valid silahkan ulangi inputan", "red"))

        nama_user = input("Masukkan Nama Anda : ")
        nim_user = input("Masukkan Nim Anda : ")

        quiz = soal.init_soal(tipe_soal, jumlah_soal)

        tabel = PrettyTable()
        tabel.field_names = ["No", "Soal", "Jawaban User", "Jawaban Data"]
        jawaban_benar = 0
        jawaban_salah = 0
        for nomor, data in quiz[1].items():
            if (data["jawaban_user"] == data["jawaban_data"]):
                jawaban_benar += 1
            else:
                jawaban_salah += 1
            tabel.add_row(
                [nomor, data['soal'], colored(data['jawaban_user'], "green" if (data["jawaban_user"] == data["jawaban_data"])else "red"), data['jawaban_data']])

        tabel.align["No"] = "c"
        tabel.align["Soal"] = "l"
        tabel.align["Jawaban User"] = "c"
        tabel.align["Jawaban Data"] = "c"

        length_tabel = len(tabel.get_string().split("\n")[0])
        print(length_tabel)
        line(length_tabel, "green")
        print("{:^{}}".format(
            "Universitas Bina Sarana Informatika", length_tabel))
        print("{:^{}}".format(
            "Hasil Quiz Sederhana", length_tabel))
        line(length_tabel, "green")
        lebar_setengah = length_tabel // 2
        print(f"Nama User : {nama_user:<{lebar_setengah}} Jumlah Soal : {
            jumlah_soal:<{lebar_setengah}}")
        print(f"Nim User  : {nim_user:<{lebar_setengah}} Jumlah Benar: {jawaban_benar:<{
            lebar_setengah}}")
        print(f"{' ' * (length_tabel // 2 + 12)
                 } Jumlah Salah: {jawaban_salah:>0}")
        print(f"{' ' * (length_tabel // 2 + 12)} Total Nilai : {quiz[0]:>0}")
        print(tabel)

        ulangi = input("Apakah anda ingin mencoba lagi? (y/n)").lower()
        if (ulangi != "y"):
            print("Terimakasih sudah mencoba, Sampai Jumpa!")
            break


main()
