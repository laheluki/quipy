import time
from termcolor import colored
from prettytable import PrettyTable


def pfrint(kata, warna):
    print(colored(kata, warna))


def line(p, warna):
    print(colored("="*p, warna))


def loading(kalimat):
    for i in range(101):
        time.sleep(.1)

        print(colored(f"\r{kalimat} : {i}%", "white"), end="\r")


def hitung_skor(skor, jumlah_soal):
    return int(skor / jumlah_soal * 100)


def filter_jawaban(jawaban, soal):
    if (jawaban == "A"):
        jwb = soal[0].split(".")[1]
    elif (jawaban == "B"):
        jwb = soal[1].split(".")[1]
    elif (jawaban == "C"):
        jwb = soal[2].split(".")[1]
    elif (jawaban == "D"):
        jwb = soal[3].split(".")[1]
    return jwb


def panjang_soal(data):
    return len(data['soal'])


def table(data):
    tabel = PrettyTable()
    tabel.field_names = ["No", "Soal", "Jawaban User", "Data Jawaban"]

    for no, res in enumerate(data, 1):
        tabel.add_row(
            [no, res['soal'], colored(res['jawaban_user'], "green" if (res["jawaban_user"] == res["data_jawaban"])else "red"), res['data_jawaban']])
    length_table = len(tabel.get_string().split("\n")[0])
    return tabel, length_table
