class Kitap:

    kutuphane_envanteri = []

    def __init__(self, isim, yazar, sayfa_sayisi, tur):
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur

    def kitap_ekle(self):
        Kitap.kutuphane_envanteri.append(self)
        print("Kitap başarıyla eklendi.")