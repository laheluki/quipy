import random
from termcolor import colored
from constants import soal_ipa, soal_umum, soal_pkn


class Soal:
    def __acak_data_soal(self, tipe_soal, jumlah):
        hasil_acak = random.sample(tipe_soal, jumlah)
        return hasil_acak

    def __generate_soal_random(self, jumlah):
        print("Ini jumlah soal : ", jumlah)
        jumlah_soal = max(1, min(jumlah, 15))
        soumum = self.__acak_data_soal(soal_umum, 15 // 3)
        soipa = self.__acak_data_soal(soal_ipa, 15 // 3)
        sopkn = self.__acak_data_soal(soal_pkn, 15//3)

        hasil_soal = soumum + soipa + sopkn
        hasil_soal = self.__acak_data_soal(hasil_soal, jumlah_soal)

        return hasil_soal

    def __perulangan_soal(self, soal):
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

        nilai = Soal.__hitung_nilai(skor, len(soal))
        return (nilai, hasil_user)

    def __hitung_nilai(jawaban_benar, jumlah_soal):
        return round((jawaban_benar/jumlah_soal)*100)

    def init_soal(self, tipe_soal, jumlah_soal):
        # print(tipe_soal, jumlah_soal)

        if (tipe_soal == 1):
            soal = self.__acak_data_soal(soal_umum, jumlah_soal)
            response = self.__perulangan_soal(soal)
        elif (tipe_soal == 2):
            soal = self.__acak_data_soal(soal_ipa, jumlah_soal)
            response = self.__perulangan_soal(soal)
        elif (tipe_soal == 3):
            soal = self.__acak_data_soal(soal_pkn, jumlah_soal)
            response = self.__perulangan_soal(soal)
        elif (tipe_soal == 4):
            soal = self.__generate_soal_random(jumlah_soal)
            response = self.__perulangan_soal(soal)
        return response
