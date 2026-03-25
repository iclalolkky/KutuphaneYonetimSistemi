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

        class BasiliKitap(Kitap):
            def __init__(self, isim, yazar, sayfa_sayisi, tur, adet):
                super().__init__(isim, yazar, sayfa_sayisi, tur)
                self.adet = adet

            def odunc_al(self):
                if self.adet > 0:
                    self.adet -= 1
                    print(f"{self.isim} başarıyla ödünç alındı. Kalan adet: {self.adet}")
                else:
                    print(f"Maalesef {self.isim} adlı kitaptan stokta kalmadı.")

            def iade_et(self):
                self.adet += 1
                print(f"{self.isim} başarıyla iade edildi. Güncel adet: {self.adet}")

        class EKitap(Kitap):
            def __init__(self, isim, yazar, sayfa_sayisi, tur, dosya_boyutu_mb):
                super().__init__(isim, yazar, sayfa_sayisi, tur)
                self.dosya_boyutu_mb = dosya_boyutu_mb