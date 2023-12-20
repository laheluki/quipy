from random import sample
from constants import soal_umum, soal_ipa, soal_pkn


class Soal:
    def __init__(self, tipe_soal, jumlah):
        self.__tipe_soal = tipe_soal
        self.__jumlah = jumlah

    def __acak_soal(self, tipe, jumlah):
        return sample(tipe, jumlah)

    def __bikin_soal_random(self):
        soumum = self.__acak_soal(soal_umum, 10 // 3)
        soipa = self.__acak_soal(soal_ipa, 10 // 3)
        sopkn = self.__acak_soal(soal_pkn, 10 // 3)
        hasil = soumum + soipa + sopkn
        return hasil

    def __tentukan_soal(self):
        if (self.__tipe_soal == 1):
            return soal_umum
        elif (self.__tipe_soal == 2):
            return soal_ipa
        elif (self.__tipe_soal == 3):
            return soal_pkn
        else:
            return self.__bikin_soal_random()

    def init_soal(self):
        soal = self.__tentukan_soal()
        return self.__acak_soal(soal, self.__jumlah)
