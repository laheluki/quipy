from utils import line, loading, pfrint, hitung_skor, filter_jawaban, table
from soal import Soal


def Main():
    while True:
        line(43, "green")
        pfrint(
            "✌️  Selamat Datang di QuiPy - Kelompok 6 ✌️ \n\t Aplikasi Quiz Sederhana", "red")
        line(43, "green")
        print("1. UMUM")
        print("2. IPA")
        print("3. PKN")
        line(33, "green")

        while True:
            try:
                tipe_soal = int(
                    input("Masukkan Pilihan (default acak) : ") or "4")
                jumlah_soal = int(
                    input("Masukkan jumlah soal (default 10) : ") or "10")
                if 1 <= tipe_soal <= 4:
                    if 1 <= jumlah_soal <= 10:
                        break
                    else:
                        print("Maksimal 10 soal.")
                else:
                    pfrint("*Data tidak valid silahkan ulangi inputan", "red")
            except:
                pfrint("*Data tidak valid silahkan ulangi inputan", "red")

        loading("Tunggu ya soal sedang disiapkan...")
        print("\n")

        soal = Soal(tipe_soal, jumlah_soal)
        soal = soal.init_soal()
        skor = 0
        hasil = []
        for i in range(len(soal)):
            print(f"{i+1}. {soal[i]['soal']}")
            for j in soal[i]['pilihan']:
                print(f"   {j}")
            jawaban = input("Jawaban : ").upper()
            if (jawaban == soal[i]['jawaban']):
                pfrint("Jawaban Benar", "green")
                skor += 1
            else:
                pfrint("Jawaban Salah", "red")

            jawaban_user = filter_jawaban(jawaban, soal[i]['pilihan'])
            data_jawaban = filter_jawaban(
                soal[i]['jawaban'], soal[i]['pilihan'])

            hasil.append({"soal": soal[i]['soal'],
                         "jawaban_user": jawaban_user,
                          "data_jawaban": data_jawaban
                          })

            line(43, "green" if jawaban == soal[i]['jawaban'] else "red")

        loading("Tunggu ya sedang di akumulasi...")

        tabel, length_table = table(hasil)
        print("\n")
        line(length_table, "green")
        print(f"{"Universitas Bina Sarana Informatika":^{length_table}}")
        print(f"{"Penilaian Quiz Sederhana":^{length_table}}")
        line(length_table, "green")
        print(tabel)
        skor = f"Skor : {hitung_skor(skor, len(soal))}"
        print(f"{skor:>{length_table}}")

        ulangi = input("Apakah anda ingin mencoba lagi? (y/n)").lower()
        if (ulangi != "y"):
            print("Terimakasih sudah mencoba, Sampai Jumpa!")
            break


Main()
