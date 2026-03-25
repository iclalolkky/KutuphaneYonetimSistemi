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
            print(f"{self.isim} ödünç alındı. Kalan adet: {self.adet}")
        else:
            print(f"{self.isim} adlı kitap stokta yok.")

    def iade_et(self):
        self.adet += 1
        print(f"{self.isim} iade edildi. Güncel adet: {self.adet}")


class EKitap(Kitap):
    def __init__(self, isim, yazar, sayfa_sayisi, tur, dosya_boyutu_mb):
        super().__init__(isim, yazar, sayfa_sayisi, tur)
        self.dosya_boyutu_mb = dosya_boyutu_mb


while True:
    print("\n1- Kitap Ekle")
    print("2- Kitapları Listele")
    print("3- Kitap Ödünç Al")
    print("4- Kitap İade Et")
    print("5- Çıkış")

    secim = input("Seçim: ")

    if secim == '1':
        isim = input("Kitap adı: ")
        yazar = input("Yazar: ")
        sayfa_sayisi = input("Sayfa sayısı: ")

        print("Tür Seçimi:")
        print("1- Basılı Kitap")
        print("2- E-Kitap")
        tur_secim = input("Tür (1 veya 2): ")

        if tur_secim == '1':
            tur = "Basılı Kitap"
            adet = int(input("Adet: "))
            yeni_kitap = BasiliKitap(isim, yazar, sayfa_sayisi, tur, adet)
            yeni_kitap.kitap_ekle()
        elif tur_secim == '2':
            tur = "E-Kitap"
            boyut = input("Dosya boyutu (MB): ")
            yeni_kitap = EKitap(isim, yazar, sayfa_sayisi, tur, boyut)
            yeni_kitap.kitap_ekle()
        else:
            print("Geçersiz tür.")

    elif secim == '2':
        for kitap in Kitap.kutuphane_envanteri:
            print(f"Kitap Adı: {kitap.isim}, Yazar: {kitap.yazar}, Tür: {kitap.tur}")

    elif secim == '3':
        aranan = input("Ödünç almak istediğiniz kitabın adı: ")
        bulundu = False
        for kitap in Kitap.kutuphane_envanteri:
            if kitap.isim == aranan and isinstance(kitap, BasiliKitap):
                kitap.odunc_al()
                bulundu = True
                break
        if not bulundu:
            print("Kitap bulunamadı.")

    elif secim == '4':
        aranan = input("İade etmek istediğiniz kitabın adı: ")
        bulundu = False
        for kitap in Kitap.kutuphane_envanteri:
            if kitap.isim == aranan and isinstance(kitap, BasiliKitap):
                kitap.iade_et()
                bulundu = True
                break
        if not bulundu:
            print("Kitap bulunamadı.")

    elif secim == '5':
        print("Sistemden çıkılıyor...")
        break

    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")