import time
import sys
import random
from termcolor import colored
from constants import soal_ipa, soal_umum, soal_pkn


def green_line(length=43):
    print(colored("="*length, "green"))


def loading(words):
    color = "white"
    for i in range(101):
        time.sleep(0.1)

        if (i > 25):
            color = "blue"

        if (i > 50):
            color = "magenta"

        if (i > 75):
            color = "green"

            color = "blue"
        sys.stdout.write(
            colored(f"\r {words} %d%%" % i, color))
        sys.stdout.flush()


def hitung_nilai(jawaban_benar, jumlah_soal):
    return round((jawaban_benar/jumlah_soal)*100)


def perulangan_soal(soal):
    skor = 0
    hasil_user = {}
    for no, pertanyaan in enumerate(soal, 1):
        print(f"{no}. {pertanyaan['soal']}")
        jawaban = input("Jawaban = ").lower()

        if (jawaban == pertanyaan["jawaban"]):
            print(colored("Jawaban benar", "green"))
            hasil_user[no] = {"soal": pertanyaan['soal'],
                              "jawaban_user": jawaban, "jawaban_data": pertanyaan['jawaban']}
            skor += 1
        else:
            print(colored("Jawaban Salah", "red"))
            hasil_user[no] = {"soal": pertanyaan['soal'],
                              "jawaban_user": jawaban, "jawaban_data": pertanyaan['jawaban']}
            # skor = max(0, skor - 1)

    nilai = hitung_nilai(skor, len(soal))
    return (nilai, hasil_user)


def acak_data_soal(tipe_soal, jumlah):
    hasil_acak = random.sample(tipe_soal, jumlah)
    return hasil_acak


def generate_soal_random(jl):
    jumlah_soal = max(1, min(jl, 15))
    soumum = acak_data_soal(soal_umum, 15 // 3)
    soipa = acak_data_soal(soal_ipa, 15 // 3)
    sopkn = acak_data_soal(soal_pkn, 15//3)

    hasil_soal = soumum + soipa + sopkn
    hasil_soal = acak_data_soal(hasil_soal, jumlah_soal)

    return hasil_soal


def init_soal(pl, jl):
    if (pl == 1):
        soal = acak_data_soal(soal_umum, jl)
        response = perulangan_soal(soal)
    elif (pl == 2):
        soal = acak_data_soal(soal_ipa, jl)
        response = perulangan_soal(soal)
    elif (pl == 3):
        soal = acak_data_soal(soal_pkn, jl)
        response = perulangan_soal(soal)
    elif (pl == 4):
        soal = generate_soal_random(jl)
        response = perulangan_soal(soal)
    return response


def main():
    green_line()
    print(colored(
        "✌️  Selamat Datang di QuiPy - Kelompok 6 ✌️ \n\t Aplikasi Quiz Sederhana", "red"))
    green_line()

    print("1. UMUM")
    print("2. IPA")
    print("3. PKN")
    green_line(26)

    tipe_soal = int(input("Masukkan Pilihan (default acak) : ") or "4")
    jumlah_soal = int(input("Masukkan jumlah soal (default 15) : ") or "15")

    quiz = init_soal(tipe_soal, jumlah_soal)
    print("{:<2} {:<50} {:<20} {:<20}".format(
        "No",
        "Soal",
        "Jawaban User",
        "Jawaban Data"
    ))
    print("-" * 80)
    for nomor, data in quiz[1].items():

        print("{:<2} {:<50} {:<30} {:<20}".format(
            nomor,
            data['soal'],
            colored(data['jawaban_user'], 'green' if (
                data['jawaban_user'] == data['jawaban_data'])else 'red'),
            data['jawaban_data']
        ))


main()
